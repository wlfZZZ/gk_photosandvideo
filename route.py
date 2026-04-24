from datetime import date

from flask import Flask, render_template


app = Flask(__name__)


PAGE_CONTENT = {
    "site_name": "GK Photos & Video",
    "navigation": ["Home", "Portfolio", "Pricing", "About", "Contact"],
    "hero": {
        "heading": "Let’s Snap Your Memories",
        "subtext": "Capturing timeless moments through cinematic storytelling",
        "button": "View Portfolio",
        "image": "/static/images/hero-rings.webp",
    },
    "visual_showcase": {
        "title": "Visual Showcase",
        "text": (
            "A cinematic blend of moving frames and signature moments from the "
            "stories we capture."
        ),
        "columns": [
            [
                {
                    "title": "Ceremony Portrait",
                    "image": (
                        "https://images.unsplash.com/photo-1519741497674-611481863552"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Styled Couple Frame",
                    "image": (
                        "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Grand Entrance",
                    "image": (
                        "https://images.unsplash.com/photo-1511578314322-379afb476865"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Reception Lights",
                    "image": (
                        "https://images.unsplash.com/photo-1505236858219-8359eb29e329"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
            ],
            [
                {
                    "title": "Bride Detail",
                    "image": (
                        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Golden Hour Shoot",
                    "image": (
                        "https://images.unsplash.com/photo-1520854221256-17451cc331bf"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Editorial Pose",
                    "image": (
                        "https://images.unsplash.com/photo-1494790108377-be9c29b29330"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
                {
                    "title": "Celebration Dance",
                    "image": (
                        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),
                },
            ],
        ],
        "video": {
            "src": "https://res.cloudinary.com/dxmsz4akw/video/upload/q_auto/f_auto/v1776668611/gk_trailer_1_1_jw1byl.mp4",
            "poster": (
                "https://images.unsplash.com/photo-1511285560929-80b456fea0bc"
                "?auto=format&fit=crop&w=1400&q=80"
            ),
            "caption": "Watch Our Work",
        },
    },
    "portfolio_categories": ["All", "Weddings", "Portraits", "Events"],
    "portfolio_items": [
        {
            "title": "Wedding Ceremony",
            "category": "Weddings",
            "image": (
                "https://images.unsplash.com/photo-1519741497674-611481863552"
                "?auto=format&fit=crop&w=900&q=80"
            ),
        },
        {
            "title": "Candid Couple",
            "category": "Weddings",
            "image": (
                "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2"
                "?auto=format&fit=crop&w=900&q=80"
            ),
        },
        {
            "title": "Portrait Photography",
            "category": "Portraits",
            "image": (
                "https://images.unsplash.com/photo-1534528741775-53994a69daeb"
                "?auto=format&fit=crop&w=500&h=600&q=80"
            ),
        },
        {
            "title": "Reception Details",
            "category": "Events",
            "image": (
                "https://images.unsplash.com/photo-1520854221256-17451cc331bf"
                "?auto=format&fit=crop&w=900&q=80"
            ),
        },
    ],
    "stats": [
        {"label": "Clients", "value": "120+"},
        {"label": "Projects", "value": "600+"},
        {"label": "Awards", "value": "18"},
    ],
    "about": {
        "heading": "About Us",
        "subheading": "Capturing Moments That Matter",
        "text": [
            "At GK Photos and Video, we are passionate about preserving life's most valuable moments through exceptional photography and cinematic videography. With 6 years of successful experience in the industry and over 600 events covered since 2020, we have earned the trust of countless clients by consistently delivering quality, creativity, and professionalism.",
            "Every celebration has a unique story, and our mission is to capture it beautifully. From weddings, engagements, pre-wedding shoots, baby showers, and birthday celebrations to corporate events and special occasions, we focus on every smile, emotion, and unforgettable detail that makes your event truly special.",
            "Our team combines advanced technology, creative vision, and personalized service to create stunning photographs and videos that you can cherish for a lifetime. We believe in turning fleeting moments into everlasting memories with elegance and perfection.",
            "At GK Photos and Video, your happiness is our inspiration, and your memories are our priority."
        ],
        "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776774152/Gokul_-_owner_photographer_nzgzkg.png",
    },
    "team": {
        "heading": "Our Team",
        "subheading": "Awesome team members",
        "members": [
            {
                "name": "Gokul",
                "role": "Owner | Photographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776774152/Gokul_-_owner_photographer_nzgzkg.png",
                "bio": "Visionary founder and lead storyteller behind GK Photos & Video."
            },
            {
                "name": "Likitha",
                "role": "Owner | Creativity Lead",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772825/likitha_Owner_creativity_lead_yaebra.png",
                "bio": "Guiding the creative vision with a passion for soulful storytelling."
            },
            {
                "name": "Divakar",
                "role": "Designer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772830/Divakar_-_designer_vnhvkx.png",
                "bio": "Crafting visual harmony and elegant design experiences."
            },
            {
                "name": "Balu",
                "role": "Drone Pilot",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776871896/Balu_-_drone_pilot.png_nhjlpy.png",
                "bio": "Capturing grand perspectives from the sky with cinematic precision."
            },
            {
                "name": "Hariprasad",
                "role": "Editor",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772822/Hariprasad_-editor_gnrses.png",
                "bio": "Weaving frames into timeless narratives with meticulous detail."
            },
            {
                "name": "Edward",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772821/Edward_-_videographer_zlcxty.png",
                "bio": "Life in motion – capturing the essence of every celebration."
            },
            {
                "name": "Prajwal",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772826/Prajwal_-_videographer_ibg2du.png",
                "bio": "Mastering light and shadow to tell cinematic stories."
            },
            {
                "name": "Iwin",
                "role": "Photographer | Cinematographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772823/Iwin_-_photographer_cinematographer_hia5hl.png",
                "bio": "Blending still and moving imagery into one grand artistic vision."
            },
            {
                "name": "Rohan",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772822/Rohan_-_videographer_sn2pfw.png",
                "bio": "Documenting authentic moments with a fresh cinematic edge."
            },
            {
                "name": "Dharshan",
                "role": "Cinematographer | Editor",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772821/Dharshan_-_cinematographer_editor_lfhqsb.png",
                "bio": "Expertly blending technical skill with creative post-production."
            },
            {
                "name": "Sagar",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772827/Sagar_-_videographer_qiksqa.png",
                "bio": "Behind the lens, finding the magic in every frame."
            },
            {
                "name": "Chandu",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772820/Chandu_-_videographer_m1nj2m.png",
                "bio": "Dedicated to capturing the high-energy vibe of every event."
            },
            {
                "name": "Vinay",
                "role": "Videographer",
                "image": "https://res.cloudinary.com/dxmsz4akw/image/upload/q_auto/f_auto/v1776772824/Vinay_-_videographer_i2znxg.png",
                "bio": "Your memories, transformed through a cinematic lens."
            }
        ]
    },
    "google_reviews": {
        "heading": "Client Stories",
        "subheading": "Verified Google Reviews",
        "average_rating": 5.0,
        "total_count": 134,
        "maps_link": "https://www.google.com/maps/place/Gk+photos+and+video/@13.085801,77.5484059,17z/data=!4m8!3m7!1s0x3bae239aa132b403:0xc0178af12128eea2!8m2!3d13.085801!4d77.5484059!9m1!1b1!16s%2Fg%2F11rv9jgyr0",
        "reviews": [
            {
                "name": "Arjun Sharma",
                "time": "2 days ago",
                "rating": 5,
                "text": "Exceptional work! The team at GK Photos & Video were incredibly professional during our wedding. The cinematic video they delivered was beyond our expectations.",
                "initial": "A",
                "color": "#EA4335"
            },
            {
                "name": "Priya Patel",
                "time": "1 week ago",
                "rating": 5,
                "text": "I highly recommend GK for any event. They have a great eye for candid shots and the quality of the photos is top-notch. Truly the best in Bangalore.",
                "initial": "P",
                "color": "#34A853"
            },
            {
                "name": "Rahul Varma",
                "time": "3 weeks ago",
                "rating": 5,
                "text": "Fantastic experience with the commercial shoot. Very creative and helpful team. Looking forward to working with them again.",
                "initial": "R",
                "color": "#4285F4"
            }
        ]
    },
    "packages": [
        {
            "duration": "1 Day Packages",
            "items": [
                {
                    "name": "Bronze",
                    "price": "₹26,000",
                    "features": [
                        "Traditional Photography",
                        "Traditional Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Silver",
                    "price": "₹28,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Gold",
                    "price": "₹33,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Photography",
                        "Traditional Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Platinum",
                    "price": "₹50,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Photography",
                        "Traditional Videography",
                        "Candid Videography",
                        "Album (15 sheets)",
                    ],
                },
            ],
        },
        {
            "duration": "2 Day Packages",
            "items": [
                {
                    "name": "Bronze",
                    "price": "₹48,000",
                    "features": [
                        "Traditional Photography",
                        "Traditional Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Silver",
                    "price": "₹52,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Gold",
                    "price": "₹62,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Photography",
                        "Traditional Videography",
                        "Album (15 sheets)",
                    ],
                },
                {
                    "name": "Platinum",
                    "price": "₹96,000",
                    "features": [
                        "Traditional Photography",
                        "Candid Photography",
                        "Traditional Videography",
                        "Candid Videography",
                        "Album (15 sheets)",
                    ],
                },
            ],
        },
    ],
    "packages_note": (
        "Album sheets are customizable and priced accordingly. "
        "Drone and LED wall services available."
    ),
    "enquiry": {
        "heading": "Get in Touch",
        "form_heading": "Send a Message",
        "button": "Submit Enquiry",
    },
    "maps": {
        "heading": "Find Us on Google Maps",
        "locations": [
            {
                "name": "Bangalore",
                "id": "bangalore",
                "embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.184852358051!2d77.54493001000001!3d13.087480700000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae239aa132b403%3A0xc0178af12128eea2!2sGk%20photos%20and%20video!5e0!3m2!1sen!2sin!4v1776537623000!5m2!1sen!2sin",
                "maps_url": "https://www.google.com/maps/place/Gk+photos+and+video/@13.0874859,77.54493,17z/data=!4m6!3m5!1s0x3bae239aa132b403:0xc0178af12128eea2!8m2!3d13.0874807!4d77.5475049!16s%2Fg%2F11zj349zzm",
                "address": "Vidyaranyapura, Bangalore"
            },
            {
                "name": "Mangalore",
                "id": "mangalore",
                "embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3889.576020526017!2d74.84298191000001!3d12.8706322!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba35bf6101476f3:0x1fd2deaab8428c1f!2sGk%20photos%20and%20video!5e0!3m2!1sen!2sin!4v1776537713437!5m2!1sen!2sin",
                "maps_url": "https://www.google.com/maps/place/Gk+photos+and+video/@12.8706374,74.8429819,17z/data=!4m6!3m5!1s0x3ba35bf6101476f3:0x1fd2deaab8428c1f!8m2!3d12.8706322!4d74.8455568!16s%2Fg%2F11sgkxnbs8",
                "address": "Balmatta Road, Mangalore"
            }
        ]
    },
    "footer": {
        "tagline": "Let's snap your memories",
        "since": "Since 2020",
        "phones": ["9740689946", "9110689946"],
        "locations": "Bangalore & Mangalore",
        "addresses": [
            {
                "city": "Bangalore",
                "lines": [
                    "Shop No 4, 61/A, Hillside Meadows Layout,",
                    "Sambram College Main Road,",
                    "Vidyaranyapura Post, Bangalore - 560097",
                ],
            },
            {
                "city": "Mangalore",
                "lines": [
                    "Opp Hotel Roopa,",
                    "Balmatta Road, Hampankatta, Mangalore",
                ],
            },
        ],
        "socials": [
            {"name": "Instagram", "abbr": "IG"},
            {"name": "Facebook", "abbr": "FB"},
            {"name": "YouTube", "abbr": "YT"},
        ],
    },
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        page=PAGE_CONTENT,
        current_year=date.today().year,
    )


if __name__ == "__main__":
    app.run(debug=True)
