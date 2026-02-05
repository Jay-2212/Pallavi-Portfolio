"""
Pallavi R. Kamath - Professional Portfolio Website
===================================================

A Flask-based professional portfolio website showcasing healthcare management
expertise, pre-operational planning, and quality excellence.

Author: Pallavi R. Kamath
Contact: pallavirkamath06@gmail.com

QUICK START:
    1. Create virtual environment: python3 -m venv venv
    2. Activate: source venv/bin/activate
    3. Install dependencies: pip install -r requirements.txt
    4. Run: python app.py
    5. Open: http://localhost:5000

PROJECT STRUCTURE:
    - app.py          : Main Flask application (this file)
    - static/         : CSS, JS, images, and downloadable files
    - templates/      : HTML templates using Jinja2

MODIFYING CONTENT:
    All portfolio data is centralized in the `portfolio_data` dictionary below.
    Update that dictionary to change content across all pages.

DEPLOYMENT:
    The Procfile is configured for Heroku/Render deployment using gunicorn.
    Set FLASK_ENV=production for production deployments.
"""

import os
from flask import Flask, render_template, request, send_from_directory

# =============================================================================
# FLASK APPLICATION INITIALIZATION
# =============================================================================

# Create Flask application instance
# template_folder: Location of HTML templates (default: 'templates')
# static_folder: Location of static assets (default: 'static')
app = Flask(__name__)


# =============================================================================
# PORTFOLIO DATA CONFIGURATION
# =============================================================================
# 
# This dictionary contains all content displayed on the website.
# Modify values here to update content across all pages automatically.
#
# Structure:
#   - name, title, location    : Basic personal information
#   - contact details          : Email, phone, LinkedIn
#   - summary                  : Professional summary (used in Hero section)
#   - experience               : List of work experiences
#   - education                : Academic qualifications
#   - skills                   : Categorized skills dictionary
#   - certifications           : Professional certifications
#   - awards                   : Awards and recognitions
#   - leadership               : Leadership roles and initiatives
#   - languages                : Language proficiencies

portfolio_data = {
    # -------------------------------------------------------------------------
    # PERSONAL INFORMATION
    # -------------------------------------------------------------------------
    "name": "Dr. Pallavi R. Kamath",
    "title": "Healthcare Management | Pre-Operational Planning & Quality Excellence",
    "location": "Udupi, India",
    
    # -------------------------------------------------------------------------
    # CONTACT INFORMATION
    # -------------------------------------------------------------------------
    "email": "pallavirkamath06@gmail.com",
    "phone": "+91 8277113400",
    "linkedin": "https://www.linkedin.com/in/pallavirkamath",
    
    # -------------------------------------------------------------------------
    # HERO SECTION - EMPATHETIC NARRATIVE
    # This speaks to the HEART of who Pallavi is - for Praan Health
    # -------------------------------------------------------------------------
    "hero": {
        "greeting": "Hello, I'm Pallavi",
        "tagline": "I believe healthcare is about human connection",
        "story": """An occupational therapist at heart, I discovered my calling through 300+ hours of volunteering 
        with children and people with disabilities. From those moments of genuine connection—helping a child 
        take their first independent step, sitting with families through their hardest days—I learned that 
        true care lives in empathy, not just protocols. Today, I bring this human-centered approach to 
        healthcare operations, because our parents deserve care that honors their dignity, their stories, 
        and their hope for healthier years ahead.""",
        "main_image": "images/pallavi-main.jpg"
    },
    
    # -------------------------------------------------------------------------
    # WHY PRAAN - VALUES ALIGNMENT
    # Explicitly connecting Pallavi's journey to Praan Health's mission
    # -------------------------------------------------------------------------
    "why_praan": {
        "headline": "Why I'm Drawn to Praan Health",
        "quote": """"To give every parent in India a second chance at health." This mission speaks to everything 
        I believe about healthcare.""",
        "connections": [
            {
                "praan_value": "Empathy & Emotional Intelligence",
                "pallavi_story": "Working with children with disabilities taught me that care lives in emotions—fear, hope, dignity. I've sat with families during their most vulnerable moments."
            },
            {
                "praan_value": "Extreme Ownership",
                "pallavi_story": "As Student Ambassador of India's largest student volunteer organization, I led 700+ volunteers and launched 8-10 new projects from scratch."
            },
            {
                "praan_value": "Mission-First, Ego-Light",
                "pallavi_story": "I started as a volunteer and grew through service. From day-one volunteer to campus leader—it's never been about titles, but about impact."
            },
            {
                "praan_value": "Builder Mentality",
                "pallavi_story": "Designed operational frameworks for a 35-bed palliative care facility and a national conference with 700+ volunteers—built from 0→1."
            }
        ]
    },
    
    # -------------------------------------------------------------------------
    # VSO JOURNEY - VISUAL STORYTELLING
    # The transformative journey that shaped Pallavi
    # -------------------------------------------------------------------------
    "vso_journey": {
        "title": "My Journey of Discovery",
        "subtitle": "Through volunteering, I found my purpose",
        "story": """Volunteer Service Organization (VSO) wasn't just an organization I joined—it was where I discovered 
        who I am. Starting as a volunteer in 2019, I accumulated 300+ hours working with communities, children, 
        and people with disabilities. Each interaction taught me empathy, resilience, and the profound impact of 
        simply showing up with care.""",
        "stages": [
            {
                "year": "2019",
                "role": "Volunteer",
                "description": "Started with 300+ hours of service, community development, and educational outreach",
                "image": "images/vso/AISelect_20260205_224049_Instagram.png"
            },
            {
                "year": "2020-2021",
                "role": "Logistics Coordinator",
                "description": "Coordinated logistics for 15-20 volunteer projects, building systematic planning capabilities",
                "image": "images/vso/AISelect_20260205_224141_Instagram.png"
            },
            {
                "year": "2020-2022",
                "role": "Operations Coordinator",
                "description": "Managed day-to-day operations and established frameworks for organizational efficiency",
                "image": "images/vso/AISelect_20260205_224202_Instagram.png"
            },
            {
                "year": "2022-2023",
                "role": "Student Ambassador",
                "description": "Led India's largest student volunteer organization, mobilizing 700+ volunteers nationally",
                "image": "images/vso/AISelect_20260205_224315_Instagram.png"
            }
        ],
        "gallery": [
            "images/vso/AISelect_20260205_224049_Instagram.png",
            "images/vso/AISelect_20260205_224141_Instagram.png",
            "images/vso/AISelect_20260205_224202_Instagram.png",
            "images/vso/AISelect_20260205_224232_Instagram.png",
            "images/vso/AISelect_20260205_224315_Instagram.png",
            "images/vso/AISelect_20260205_224401_Instagram.png",
            "images/vso/AISelect_20260205_224412_Instagram.png",
            "images/vso/AISelect_20260205_224449_Instagram.png"
        ]
    },
    
    # -------------------------------------------------------------------------
    # PROFESSIONAL SUMMARY (Legacy - for Experience page)
    # -------------------------------------------------------------------------
    "summary": """Master of Hospital Administration candidate with clinical foundation and proven track record 
    in healthcare facility planning and operational excellence. Designed end-to-end operational framework 
    for 35-bed clinical block within 100-bed palliative care center. National award winner (Qimpro QualTech Prize) 
    for process improvement initiative that reduced operational inefficiencies by 95% and delivered ₹2.6L 
    annual cost savings. Six years of leadership experience coordinating multi-stakeholder initiatives 
    and managing cross-functional teams.""",
    
    # -------------------------------------------------------------------------
    # WORK EXPERIENCE
    # Each experience item requires:
    #   - role          : Job title
    #   - organization  : Company/Institution name
    #   - location      : Work location
    #   - period        : Time period (e.g., "June 2025 - Present")
    #   - highlights    : List of achievements/responsibilities
    # -------------------------------------------------------------------------
    "experience": [
        {
            "role": "Management Trainee",
            "organization": "Manipal Hospice and Respite Centre",
            "location": "Manipal",
            "period": "June 2025 - Present",
            "highlights": [
                "Led pre-operational planning for 35-bed clinical block within 100-bed specialized palliative care facility",
                "Designed SOPs for patient admission pathways from 2,000-bed tertiary care hospital",
                "Established multi-stakeholder death documentation framework ensuring regulatory compliance",
                "Streamlined supply chain processes, eliminating operational bottlenecks",
                "Ensured operational readiness through comprehensive logistics planning"
            ]
        },
        {
            "role": "Pediatric Occupational Therapist",
            "organization": "Anir vedha",
            "location": "Mangalore",
            "period": "February 2024 - June 2024",
            "highlights": [
                "Managed caseload of 8-10 pediatric clients with individualized care plans",
                "Coordinated weekly stakeholder communications, improving treatment adherence",
                "Designed and executed weekly group therapy programs with budget allocation",
                "Developed expertise in patient-centered care and clinical operations planning"
            ]
        }
    ],
    
    # -------------------------------------------------------------------------
    # EDUCATION
    # Each education item requires:
    #   - degree        : Degree/certification name
    #   - institution   : School/University name
    #   - period        : Duration of study
    #   - score         : GPA/Percentage (optional but recommended)
    #   - details       : List of additional details (thesis, coursework, etc.)
    # -------------------------------------------------------------------------
    "education": [
        {
            "degree": "Master of Hospital Administration (MHA)",
            "institution": "Prasanna School of Public Health, MAHE, Manipal",
            "period": "August 2024 - May 2026 (Expected)",
            "score": "8.03 CGPA",
            "details": [
                "Thesis: Exploring Organizational Health Literacy Among Administrative Stakeholders in Hospitals",
                "Coursework: Quality Management, Organizational Behaviour, Healthcare Finance, Biostatistics, HRM"
            ]
        },
        {
            "degree": "Bachelor of Occupational Therapy (BOT)",
            "institution": "Manipal College of Health Professions",
            "period": "2019 - 2024",
            "score": "7.80 CGPA",
            "details": [
                "Clinical foundation in patient care and rehabilitation",
                "Healthcare operations and patient management expertise"
            ]
        }
    ],
    
    # -------------------------------------------------------------------------
    # SKILLS
    # Organized by categories. Keys are category names, values are lists of skills.
    # Displayed on homepage in a 3-column grid layout.
    # -------------------------------------------------------------------------
    "skills": {
        "Strategic Operations Management": [
            "Healthcare Facility Planning",
            "Pre-Operational Strategy", 
            "Cross-Functional Team Leadership",
            "Stakeholder Coordination"
        ],
        "Process Excellence & Compliance": [
            "Quality Assurance Systems",
            "Standard Operating Procedures",
            "Regulatory Compliance",
            "Supply Chain Optimization",
            "DMAIC Methodology"
        ],
        "Project & Financial Management": [
            "Budget Management",
            "Resource Allocation",
            "Data-Driven Decision Making",
            "Process Implementation"
        ]
    },
    
    # -------------------------------------------------------------------------
    # CERTIFICATIONS
    # Displayed on both homepage and education page
    # -------------------------------------------------------------------------
    "certifications": [
        {
            "name": "Lean Six Sigma - Yellow Belt",
            "issuer": "Anexas Group",
            "date": "August 2025"
        },
        {
            "name": "Supply Chain and Logistics Specialization",
            "issuer": "Coursera",
            "date": "October 2025"
        },
        {
            "name": "Systematic Review and Meta-Analysis Workshop",
            "issuer": "MAHE - DHR TRC",
            "date": "December 2025"
        }
    ],
    
    # -------------------------------------------------------------------------
    # AWARDS
    # First award (index 0) is featured prominently on homepage
    # All awards displayed on experience page
    # -------------------------------------------------------------------------
    "awards": [
        {
            "title": "National Winner - QualTech® Prize",
            "organization": "Qimpro Foundation",
            "date": "September 2025",
            "description": "First place among 200+ national submissions for process improvement solution achieving 95% reduction in plasma bag breakage and ₹2.6L annual cost savings through DMAIC methodology."
        },
        {
            "title": "Overall Cultural Programme Champions",
            "organization": "OTCON - All India Occupational Therapy Association",
            "date": "February 2023",
            "description": "Led Team Manipal as event coordinator, managing logistics and team coordination to secure overall championship."
        }
    ],
    
    # -------------------------------------------------------------------------
    # LEADERSHIP ROLES
    # Displayed on experience page in a grid layout
    # -------------------------------------------------------------------------
    "leadership": [
        {
            "role": "Student Secretary",
            "organization": "SVASTH 2025 - National Conference",
            "period": "June - September 2025",
            "description": "Led 15-member team managing ₹1.8L budget for 250+ participant national conference"
        },
        {
            "role": "Coordinator",
            "organization": "Manipal Health Literacy Unit",
            "period": "November 2024 - Present",
            "description": "Organizing 7-8 national/international webinars for diverse healthcare stakeholders"
        },
        {
            "role": "Campus Ambassador",
            "organization": "Office of International Affairs, MAHE",
            "period": "July 2025 - Present",
            "description": "Managing international student programs and cross-cultural initiatives"
        },
        {
            "role": "Student Ambassador",
            "organization": "Volunteer Service Organization",
            "period": "2019 - Present",
            "description": "Progressed from volunteer to campus-level principal representative; 300+ active volunteering hours"
        }
    ],
    
    # -------------------------------------------------------------------------
    # LANGUAGES
    # Displayed on experience page
    # -------------------------------------------------------------------------
    "languages": ["English", "Hindi", "Kannada", "Konkani"]
}


# =============================================================================
# ROUTE DEFINITIONS
# =============================================================================
# 
# Each route corresponds to a page on the website.
# All routes pass the portfolio_data dictionary to templates.

@app.route('/')
def index():
    """
    Homepage Route
    --------------
    URL: /
    Template: templates/index.html
    
    Displays:
        - Hero section with intro, stats, and photo placeholder
        - About section with 3 key expertise cards
        - Skills grid
        - Featured national award
        - Certifications
        - Quick contact CTA
    """
    return render_template('index.html', data=portfolio_data)


@app.route('/experience')
def experience():
    """
    Experience Page Route
    ---------------------
    URL: /experience
    Template: templates/experience.html
    
    Displays:
        - Work experience timeline
        - Leadership roles grid
        - Awards and recognitions
        - Languages
    """
    return render_template('experience.html', data=portfolio_data)


@app.route('/education')
def education():
    """
    Education Page Route
    --------------------
    URL: /education
    Template: templates/education.html
    
    Displays:
        - Education timeline with degrees
        - Master's thesis highlight
        - Certifications
        - Key coursework
    """
    return render_template('education.html', data=portfolio_data)


@app.route('/contact')
def contact():
    """
    Contact Page Route
    ------------------
    URL: /contact
    Template: templates/contact.html
    
    Displays:
        - Contact information (email, phone, location, LinkedIn)
        - Contact form (mailto: action)
        - Areas of collaboration
        - Resume download CTA
    """
    return render_template('contact.html', data=portfolio_data)


# =============================================================================
# STATIC FILES & FAVICON
# =============================================================================

@app.route('/favicon.ico')
def favicon():
    """
    Serve favicon.ico
    Browsers automatically request this for bookmarks/tabs.
    """
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.svg',
        mimetype='image/svg+xml'
    )


@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    """
    Serve apple-touch-icon.png
    iOS devices request this when users add site to home screen.
    Falls back to favicon.svg if PNG not available.
    """
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
# 
# When running directly (not imported as module), start the development server.
# 
# WARNING: Do NOT use debug=True in production!
# For production, use a WSGI server like gunicorn (see Procfile)

if __name__ == '__main__':
    # Development server configuration
    # host='0.0.0.0' - Accessible from any network interface
    # port=5000      - Standard Flask development port
    # debug=True     - Auto-reload on code changes, detailed error pages
    app.run(debug=True, host='0.0.0.0', port=5000)
