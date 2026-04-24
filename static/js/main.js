/**
 * GK Photos & Video - Dynamic Frontend Logic
 * Refactored for JSON-driven content rendering.
 */

// --- State and UI Selectors ---
const state = {
    team: [],
    portfolio: [],
    testimonials: []
};

const selectors = {
    menuToggle: document.querySelector(".menu-toggle"),
    siteNav: document.querySelector(".site-nav"),
    navOverlay: document.querySelector(".nav-overlay"),
    portfolioGrid: document.querySelector(".portfolio-grid"),
    portfolioFilters: document.querySelector(".portfolio-filters"),
    teamWrapper: document.querySelector(".team-layout-wrapper"),
    testimonialsGrid: document.querySelector(".google-reviews-grid"),
    contactForm: document.querySelector(".message-form"),
    formStatus: document.getElementById("form-status"),
    pricingToggle: document.querySelector(".pricing-toggle")
};

// --- Initialization ---
document.addEventListener("DOMContentLoaded", async () => {
    try {
        await fetchData();
        renderSections();
        initCoreInteractions();
    } catch (error) {
        console.error("Initialization failed:", error);
    }
});

/**
 * Fetch all content data from local JSON files
 * Future: Replace these with API calls to a backend
 */
async function fetchData() {
    const [teamRes, portRes, testRes] = await Promise.all([
        fetch('/static/data/team.json'),
        fetch('/static/data/portfolio.json'),
        fetch('/static/data/testimonials.json')
    ]);

    state.team = await teamRes.json();
    state.portfolio = await portRes.json();
    state.testimonials = await testRes.json();
}

/**
 * Orchestrate the dynamic rendering of sections
 */
function renderSections() {
    renderPortfolio();
    renderTeam();
    renderTestimonials();
}

// --- Rendering Logic ---

function renderPortfolio() {
    if (!selectors.portfolioGrid) return;

    selectors.portfolioGrid.innerHTML = state.portfolio.map(item => {
        const isSlider = item.images && item.images.length > 1;

        let mediaHtml = '';
        if (isSlider) {
            mediaHtml = `
                <div class="image-slider">
                    ${item.images.map(img => `<img src="${img}" alt="${item.title}" loading="lazy">`).join('')}
                </div>
            `;
        } else {
            mediaHtml = `
                <div class="portfolio-image">
                    <img src="${item.images[0]}" alt="${item.title}" loading="lazy">
                </div>
            `;
        }

        return `
            <article class="portfolio-card" data-category="${item.category}">
                ${mediaHtml}
                <div class="portfolio-overlay">
                    <span>${item.category}</span>
                    <strong>${item.title}</strong>
                </div>
            </article>
        `;
    }).join('');

    initPortfolioInteractions();
}

function renderTeam() {
    if (!selectors.teamWrapper) return;

    const renderCard = (member) => `
        <article class="team-card ${member.name.toLowerCase() === 'gokul' || member.name.toLowerCase() === 'likitha' ? 'team-owner' : ''}">
            <div class="team-img-wrapper">
                <img src="${member.image}" alt="${member.name}" 
                     class="team-img ${member.class || ''}" loading="lazy">
            </div>
            <div class="team-info">
                <h3 class="team-name">${member.name}</h3>
                <p class="team-role">${member.role}</p>
            </div>
        </article>
    `;

    const owners = state.team.slice(0, 2);
    const gridMembers = state.team.slice(2, 12);
    const lastRowMembers = state.team.slice(12);

    const html = `
        <div class="team-container">
            <div class="team-owners">
                ${owners.map(renderCard).join('')}
            </div>
            <div class="team-grid">
                ${gridMembers.map(renderCard).join('')}
                <div class="last-row">
                    ${lastRowMembers.map(renderCard).join('')}
                </div>
            </div>
        </div>
    `;
    selectors.teamWrapper.innerHTML = html;

    // Initialize Intersection Observer for staggered animation
    const teamObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                teamObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.team-card').forEach(card => teamObserver.observe(card));
}

function renderTestimonials() {
    if (!selectors.testimonialsGrid) return;

    selectors.testimonialsGrid.innerHTML = state.testimonials.map(item => `
        <article class="google-review-card">
            <div class="gr-card-head">
                <div class="gr-user">
                    <span class="gr-avatar" style="background-color: ${item.color}">${item.initial}</span>
                    <div class="gr-info">
                        <strong>${item.name}</strong>
                        <span class="gr-time">${item.time}</span>
                    </div>
                </div>
                <div class="gr-google-icon">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Verified">
                </div>
            </div>
            <div class="gr-card-rating">
                ${'★'.repeat(item.rating)}
            </div>
            <p class="gr-review-text">${item.text}</p>
        </article>
    `).join('');
}

// --- Interaction Logic ---

function initCoreInteractions() {
    initNavigation();
    initPricing();
    initCinematicInteractions();
    initContactForm();
    initScrollAnimations();
    initScrollToTop();
}

function initNavigation() {
    const { menuToggle, siteNav, navOverlay } = selectors;
    if (!menuToggle || !siteNav) return;

    const navLinks = siteNav.querySelectorAll("a");

    const toggleMenu = (forceState) => {
        const isOpen = typeof forceState === "boolean" ? forceState : !siteNav.classList.contains("is-open");
        siteNav.classList.toggle("is-open", isOpen);
        if (navOverlay) navOverlay.classList.toggle("is-visible", isOpen);
        menuToggle.setAttribute("aria-expanded", String(isOpen));
        if (window.innerWidth <= 1024) {
            document.body.style.overflow = isOpen ? "hidden" : "";
        }
    };

    menuToggle.addEventListener("click", () => toggleMenu());
    if (navOverlay) navOverlay.addEventListener("click", () => toggleMenu(false));
    navLinks.forEach(link => link.addEventListener("click", () => toggleMenu(false)));

    // Active Link Logic
    const header = document.querySelector(".site-header");
    const sections = document.querySelectorAll("section[id]");
    const handleNavbarStyles = () => {
        if (header) header.classList.toggle("is-scrolled", window.scrollY > 50);
        let current = "";
        sections.forEach((section) => {
            if (window.scrollY >= section.offsetTop - 180) {
                current = section.getAttribute("id");
            }
        });
        navLinks.forEach((link) => {
            link.classList.toggle("is-active", link.getAttribute("href") === `#${current}`);
        });
    };
    window.addEventListener("scroll", handleNavbarStyles, { passive: true });
}

function initPortfolioInteractions() {
    const filterButtons = document.querySelectorAll(".filter-chip");
    const cards = document.querySelectorAll(".portfolio-card");

    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const filter = button.dataset.filter;
            filterButtons.forEach(btn => btn.classList.toggle("is-active", btn === button));
            cards.forEach(card => {
                const visible = filter === "All" || card.dataset.category === filter;
                card.hidden = !visible;
            });
        });
    });

    // Slider Logic
    cards.forEach((card) => {
        const slider = card.querySelector(".image-slider");
        if (!slider) return;

        let index = 0;
        const total = slider.children.length;
        let interval;

        const startSlider = () => {
            interval = setInterval(() => {
                index = (index + 1) % total;
                slider.style.transform = `translateX(-${index * 100}%)`;
            }, 3000);
        };
        const stopSlider = () => clearInterval(interval);

        startSlider();
        card.addEventListener("mouseenter", stopSlider);
        card.addEventListener("mouseleave", startSlider);
    });
}

function initPricing() {
    const { pricingToggle } = selectors;
    const buttons = document.querySelectorAll(".pricing-toggle-button");
    const panels = document.querySelectorAll(".pricing-panel");
    const wrap = document.querySelector(".pricing-panels");

    const setHeight = () => {
        const active = wrap?.querySelector(".pricing-panel.is-active");
        if (active && wrap) wrap.style.height = `${active.offsetHeight}px`;
    };

    if (pricingToggle) {
        buttons.forEach(btn => {
            btn.addEventListener("click", () => {
                const target = btn.dataset.panelTarget;
                buttons.forEach(b => b.classList.toggle("is-active", b === btn));
                pricingToggle.dataset.active = target;
                panels.forEach(p => p.classList.toggle("is-active", p.dataset.panel === target));
                requestAnimationFrame(setHeight);
            });
        });
        window.addEventListener("resize", setHeight);
        setHeight();
    }
}

function initCinematicInteractions() {
    const heroVideo = document.getElementById("heroVideo");
    const soundBtn = document.getElementById("soundToggle");
    if (heroVideo && soundBtn) {
        soundBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            heroVideo.muted = !heroVideo.muted;
            soundBtn.innerText = heroVideo.muted ? "🔇" : "🔊";
        });
        heroVideo.addEventListener("click", () => {
            heroVideo.muted = false;
            soundBtn.innerText = "🔊";
        });
    }

    const secondaryVideoFrame = document.querySelector(".secondary-video-frame");
    if (secondaryVideoFrame) {
        const video = secondaryVideoFrame.querySelector("video");
        const overlay = secondaryVideoFrame.querySelector(".video-controls-overlay");
        secondaryVideoFrame.addEventListener("click", () => {
            if (video.paused) { video.play(); overlay.style.opacity = "0"; }
            else { video.pause(); overlay.style.opacity = "1"; }
        });
    }

    // Map Tabs
    const mapTabs = document.querySelectorAll(".map-tab-btn");
    const mapContainers = document.querySelectorAll(".map-container");
    mapTabs.forEach(tab => {
        tab.addEventListener("click", () => {
            mapTabs.forEach(btn => btn.classList.toggle("is-active", btn === tab));
            mapContainers.forEach(c => c.classList.toggle("is-visible", c.id === `map-${tab.dataset.mapId}`));
        });
    });
}

function initContactForm() {
    const { contactForm, formStatus } = selectors;
    if (!contactForm) return;

    contactForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerText;

        submitBtn.disabled = true;
        submitBtn.innerText = "Sending...";

        emailjs.sendForm("service_u0uki69", "template_ohczo0g", contactForm)
            .then(() => {
                submitBtn.innerText = originalText;
                submitBtn.disabled = false;
                if (formStatus) {
                    formStatus.innerText = "Message sent! Redirecting to WhatsApp...";
                    formStatus.className = "form-status success";
                }
                const data = new FormData(contactForm);
                const whatsappMessage = `Hey GK\n\nJust submitted the enquiry form from your website.\n\nName: ${data.get("name")}\nPhone: ${data.get("phone")}\n\nMessage:\n${data.get("message")}`;
                const whatsappUrl = `https://wa.me/919740689946?text=${encodeURIComponent(whatsappMessage)}`;
                contactForm.reset();
                setTimeout(() => window.open(whatsappUrl, "_blank"), 1500);
            }, (err) => {
                submitBtn.innerText = originalText;
                submitBtn.disabled = false;
                if (formStatus) {
                    formStatus.innerText = "Failed. Try again later.";
                    formStatus.className = "form-status error";
                }
            });
    });
}

function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                if (entry.target.classList.contains("stats-grid")) {
                    entry.target.querySelectorAll(".stat-number").forEach(startCounter);
                }
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll(".reveal-on-scroll, .stats-grid, .pricing-reveal").forEach(el => observer.observe(el));
}

function startCounter(el) {
    const target = parseInt(el.dataset.target);
    const suffix = el.innerText.includes("+") ? "+" : "";
    let count = 0;
    const increment = target / (1500 / (1000 / 60));
    const counter = setInterval(() => {
        count += increment;
        if (count >= target) { el.innerText = target + suffix; clearInterval(counter); }
        else { el.innerText = Math.floor(count) + suffix; }
    }, 1000 / 60);
}

function initScrollToTop() {
    const btn = document.getElementById("scroll-to-top");
    if (!btn) return;
    window.addEventListener("scroll", () => btn.classList.toggle("is-visible", window.scrollY > 300));
    btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
}



