"""
Pallavi R. Kamath - Professional Portfolio Website
===================================================

A personal portfolio showcasing Pallavi's journey from hands-on volunteering 
to healthcare leadership - highlighting her empathy, initiative, and natural 
leadership that drives her to deliver care at scale.

Pallavi's Journey:
- VSO (2019-2023): Discovered her calling through 300+ hours of service
- MHA (2024-2026): Learning to deliver care at scale through operations
- Hospice (2025-Present): Finding purpose in end-of-life dignity

Core Identity:
- Empathetic caregiver who connects deeply with people
- Natural leader who grew from volunteer to campus leader
- Initiative-taker who launches projects and builds systems
- Mission-driven professional seeking to reduce suffering through healthcare

QUICK START:
    1. Create virtual environment: python3 -m venv venv
    2. Activate: source venv/bin/activate
    3. Install dependencies: pip install -r requirements.txt
    4. Run: python app.py
    5. Open: http://localhost:5000
"""

import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# =============================================================================
# PORTFOLIO DATA - PALLAVI'S STORY
# =============================================================================

portfolio_data = {
    # Personal Information
    "name": "Dr. Pallavi R. Kamath",
    "title": "Healthcare Operations | Palliative Care Advocate | People-First Leader",
    "location": "Udupi, India",
    "email": "pallavirkamath06@gmail.com",
    "phone": "+91 8277113400",
    "linkedin": "https://www.linkedin.com/in/pallavirkamath",
    
    # HERO SECTION - Who Pallavi Is
    "hero": {
        "greeting": "Hello, I'm Pallavi",
        "tagline": "I believe healthcare is about human connection",
        "story": """An occupational therapist at heart, I discovered my purpose through 300+ hours of volunteering 
        with children and communities in need. From teaching in village schools to organizing national volunteer 
        movements, I learned that true care lives in empathy, not just protocols. This journey led me to 
        healthcare operations - because I believe the best way to help more people is to build systems that 
        deliver care with dignity, compassion, and excellence. Whether it's a child's first step in therapy, 
        a volunteer discovering their potential, or an elderly patient finding comfort in their final days - 
        every person deserves to be seen, heard, and cared for.""",
        "main_image": "images/pallavi-main.jpg",
        "stats": [
            {"value": "300+", "label": "Volunteering Hours"},
            {"value": "700+", "label": "Volunteers Led"},
            {"value": "6", "label": "Years of Service"}
        ]
    },
    
    # MY JOURNEY - The Story Arc
    "my_journey": {
        "title": "My Journey of Purpose",
        "subtitle": "From hands-on care to systems that scale",
        "sections": [
            {
                "id": "vso",
                "phase": "Discovery",
                "years": "2019 - 2023",
                "title": "Finding Myself Through Service",
                "organization": "Volunteer Service Organization (VSO)",
                "story": """I joined VSO as a volunteer in 2019, not knowing it would transform my life. Starting with 
                community outreach and educational programs, I discovered my love for helping others. Over 300 hours 
                of service taught me that leadership isn't about titles - it's about showing up, caring deeply, and 
                inspiring others to do the same. From teaching children in village schools to coordinating logistics 
                for 15+ projects, I grew from volunteer to Student Ambassador - leading India's largest student-run 
                volunteer organization and mobilizing 700+ volunteers nationally.""",
                "key_moments": [
                    "Started as volunteer, accumulated 300+ service hours",
                    "Coordinated logistics for 15-20 community projects",
                    "Led operations for campus-level initiatives",
                    "Student Ambassador - principal representative for 700+ volunteers",
                    "Organized national conferences with 700+ participants"
                ],
                "images": [
                    "images/vso/AISelect_20260205_224449_Instagram.jpg",  # With children - warmth
                    "images/vso/AISelect_20260205_225531_Instagram.jpg",  # Team leadership
                    "images/vso/AISelect_20260205_224315_Instagram.jpg",  # Village school
                    "images/vso/AISelect_20260205_224510_Instagram.jpg",  # Playing with kids
                    "images/vso/AISelect_20260205_224202_Instagram.jpg",  # Recognition
                    "images/vso/AISelect_20260205_225600_Instagram.jpg",  # Old age home
                ]
            },
            {
                "id": "mha",
                "phase": "Growth",
                "years": "2024 - 2026",
                "title": "Learning to Deliver Care at Scale",
                "organization": "Master of Hospital Administration, MAHE Manipal",
                "story": """My experiences in VSO showed me the gap between good intentions and systematic impact. 
                I realized that to help more people, I needed to understand healthcare operations - how to build 
                systems, manage resources, and create sustainable frameworks for care delivery. Pursuing my MHA 
                was about amplifying my ability to serve. It's where I learned that operational excellence and 
                human compassion aren't opposing forces - they work together to create dignified, accessible care.""",
                "key_moments": [
                    "8.03 CGPA - Academic excellence in healthcare management",
                    "Thesis on Organizational Health Literacy in Hospitals",
                    "Coursework: Quality Management, Healthcare Finance, HRM",
                    "Student Secretary for SVASTH 2025 national conference (250+ participants)",
                    "Coordinator for Manipal Health Literacy Unit"
                ],
                "aerial_image": "images/hospice-aerial.jpg",
                "impact": "Part of the team that brought a 100-bed palliative care vision to operational reality",
                "achievements": [
                    {
                        "title": "National Winner - QualTech Prize",
                        "org": "Qimpro Foundation",
                        "desc": "First place among 200+ submissions. Reduced plasma bag breakage by 95%, saving ₹2.6L annually through DMAIC methodology.",
                        "image": "images/Qimpro.jpg"
                    }
                ]
            },
            {
                "id": "hospice",
                "phase": "Purpose",
                "years": "June 2024 - Present",
                "title": "Building End-of-Life Care from the Ground Up",
                "organization": "Manipal Hospice and Respite Centre",
                "story": """I joined the Hospice at its very inception - before the first patient arrived, before the systems were 
                in place, when it was just a vision of dignified end-of-life care. Being there from day one has been 
                the most profound experience of my career. I've had the privilege of literally building the operational 
                foundation of a place that will provide comfort to countless families. From conducting mock drills to 
                ensure patient safety, to designing workflows that honor both medical necessity and human dignity, 
                to navigating government liaisons for death certificates - every task has taught me that operational 
                excellence in healthcare is an act of love. This is where I learned that the best way to serve is to 
                build systems that allow compassion to flow seamlessly.""",
                "key_moments": [
                    "Joined at inception - part of the founding operational team",
                    "Conducted pre-operational mock drills to ensure patient safety readiness",
                    "Designed comprehensive SOPs for patient admission pathways from 2,000-bed tertiary hospital",
                    "Created workflows and operational frameworks for 35-bed clinical block",
                    "Liaised with government authorities to establish death certificate approval processes",
                    "Built supply chain systems ensuring consistent availability of clinical materials",
                    "Coordinated cross-functional teams across clinical and non-clinical departments",
                    "Established multi-stakeholder documentation frameworks ensuring regulatory compliance"
                ],
                "team_image": "images/hospice-team.jpg"
            }
        ]
    },
    
    # WHO I AM - Core Values
    "who_i_am": {
        "title": "Who I Am",
        "subtitle": "The qualities that define my approach",
        "qualities": [
            {
                "title": "Empathetic",
                "icon": "fa-heart",
                "description": "I don't just understand people's needs - I feel them. From children with disabilities to elderly patients, I connect on a human level."
            },
            {
                "title": "Initiative-Taker",
                "icon": "fa-rocket",
                "description": "I see gaps and fill them. Launched 8-10 new projects at VSO, built operational frameworks from scratch, always asking 'how can we do better?'"
            },
            {
                "title": "Natural Leader",
                "icon": "fa-users",
                "description": "Leadership found me through service. Grew from volunteer to leading 700+ people - not because I sought titles, but because I cared about impact."
            },
            {
                "title": "Systems Thinker",
                "icon": "fa-project-diagram",
                "description": "I see the big picture. From volunteer coordination to hospital operations, I build frameworks that amplify human effort."
            }
        ]
    },
    
    # PROFESSIONAL EXPERTISE
    "skills": {
        "Healthcare Operations": [
            "Facility Planning & Pre-Operational Strategy",
            "Process Improvement & Quality Assurance",
            "Supply Chain Optimization",
            "Standard Operating Procedures"
        ],
        "Leadership & Management": [
            "Cross-Functional Team Leadership",
            "Stakeholder Coordination",
            "Event Management (700+ participants)",
            "Volunteer Management & Engagement"
        ],
        "Healthcare Focus Areas": [
            "Palliative & End-of-Life Care",
            "Patient-Centered Care Design",
            "Organizational Health Literacy",
            "Community Health Programs"
        ]
    },
    
    # EDUCATION
    "education": [
        {
            "degree": "Master of Hospital Administration (MHA)",
            "institution": "Prasanna School of Public Health, MAHE, Manipal",
            "period": "2024 - 2026 (Expected)",
            "score": "8.03 CGPA",
            "details": [
                "Thesis: Organizational Health Literacy Among Administrative Stakeholders in Hospitals",
                "Coursework: Quality Management, Healthcare Finance, Biostatistics, HRM"
            ]
        },
        {
            "degree": "Bachelor of Occupational Therapy (BOT)",
            "institution": "Manipal College of Health Professions",
            "period": "2019 - 2024",
            "score": "7.80 CGPA",
            "details": [
                "Clinical foundation in patient rehabilitation",
                "Experience with pediatric and disability care"
            ]
        }
    ],
    
    # CERTIFICATIONS
    "certifications": [
        {"name": "Lean Six Sigma - Yellow Belt", "issuer": "Anexas Group", "date": "2025"},
        {"name": "Supply Chain and Logistics", "issuer": "Coursera", "date": "2025"},
        {"name": "Systematic Review Workshop", "issuer": "MAHE - DHR TRC", "date": "2025"}
    ],
    
    # CONTACT CTA
    "contact_cta": {
        "title": "Let's Connect",
        "message": "I'm always open to conversations about healthcare, operations, volunteering, or how we can work together to make care more human-centered.",
        "button_text": "Get in Touch"
    }
}


# =============================================================================
# ROUTE DEFINITIONS
# =============================================================================

@app.route('/')
def index():
    """Homepage - Pallavi's story and journey"""
    return render_template('index.html', data=portfolio_data)


@app.route('/experience')
def experience():
    """Experience page - detailed professional journey"""
    return render_template('experience.html', data=portfolio_data)


@app.route('/education')
def education():
    """Education and credentials"""
    return render_template('education.html', data=portfolio_data)


@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html', data=portfolio_data)


# =============================================================================
# STATIC FILES & FAVICON
# =============================================================================

@app.route('/favicon.ico')
def favicon():
    """Serve favicon.ico"""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.svg',
        mimetype='image/svg+xml'
    )


@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    """Serve apple-touch-icon.png"""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.svg',
        mimetype='image/svg+xml'
    )


# =============================================================================
# ERROR HANDLERS
# =============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 Not Found errors."""
    return render_template('404.html', data=portfolio_data), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 Internal Server errors."""
    return render_template('500.html', data=portfolio_data), 500


# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
