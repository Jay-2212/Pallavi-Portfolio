# Pallavi R. Kamath - Professional Portfolio

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional portfolio website for **Dr. Pallavi R. Kamath**, a healthcare management professional specializing in pre-operational planning, quality excellence, and process improvement.

🌐 **Live Site**: [Add your deployed URL here]

---

## ✨ Features

### Design & UX
- **Responsive Design** - Optimized for desktop, tablet, and mobile devices
- **Modern UI/UX** - Clean, professional design suitable for healthcare industry
- **Smooth Animations** - Scroll-triggered fade-in animations
- **Mobile Navigation** - Hamburger menu with smooth transitions

### Content Sections
- **Hero Section** - Introduction with key statistics (95% efficiency, ₹2.6L savings)
- **About Section** - Three core expertise cards
- **Skills Grid** - Categorized skills display
- **Featured Award** - National QualTech Prize prominently displayed
- **Experience Timeline** - Chronological work history
- **Education Section** - Academic qualifications with thesis highlight
- **Contact Form** - Ready for inquiries

### Technical Features
- **Jinja2 Templating** - Reusable templates with inheritance
- **Centralized Data** - Single source of truth for all content
- **SEO Friendly** - Semantic HTML structure
- **Fast Loading** - Minimal dependencies, optimized assets

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jay-2212/Pallavi-Portfolio.git
   cd Pallavi-Portfolio
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000`

---

## 📁 Project Structure

```
Pallavi-Portfolio/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── README.md                       # This file
├── AGENTS.md                       # Documentation for AI agents
├── .gitignore                      # Git ignore rules
├── .env.example                    # Environment variables template
│
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css              # Main stylesheet (responsive)
│   ├── js/
│   │   └── main.js                # JavaScript functionality
│   ├── images/                    # Add photos here
│   └── Pallavi_R_Kamath_Resume.pdf # Downloadable resume
│
└── templates/                      # Jinja2 HTML templates
    ├── base.html                  # Base layout (nav, footer)
    ├── index.html                 # Homepage
    ├── experience.html            # Experience & awards
    ├── education.html             # Education & certifications
    └── contact.html               # Contact page
```

---

## 🛠️ Customization Guide

### 1. Update Personal Information

Edit `app.py` and modify the `portfolio_data` dictionary:

```python
portfolio_data = {
    "name": "Your Name",
    "email": "your.email@example.com",
    "phone": "+91 XXXXXXXXXX",
    # ... more fields
}
```

**Note**: Changes here automatically update all pages.

### 2. Add Photos

1. Place images in `static/images/`
2. Update `templates/index.html`:

```html
<!-- Replace the placeholder div -->
<div class="profile-image">
    <img src="{{ url_for('static', filename='images/your-photo.jpg') }}" 
         alt="Dr. Pallavi R. Kamath">
</div>
```

### 3. Change Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary: #1e3a5f;      /* Navy blue - main brand */
    --secondary: #0d9488;     /* Teal - accents */
    --accent: #f59e0b;        /* Amber - highlights */
    /* ... see file for all variables */
}
```

### 4. Add New Sections

**To add a new section to homepage**:

1. Add data to `portfolio_data` in `app.py` (if needed)
2. Add HTML to `templates/index.html`:
```html
<section class="new-section">
    <div class="container">
        <!-- Your content -->
    </div>
</section>
```
3. Add styles to `static/css/style.css`

---

## 🎨 Design System

### Colors
| Variable | Value | Usage |
|----------|-------|-------|
| `--primary` | `#1e3a5f` | Headers, buttons, navbar |
| `--secondary` | `#0d9488` | Accents, links, icons |
| `--accent` | `#f59e0b` | Awards, highlights |
| `--text-primary` | `#1f2937` | Body text |
| `--bg-secondary` | `#f8fafc` | Section backgrounds |

### Typography
- **Headings**: Playfair Display (serif)
- **Body**: Inter (sans-serif)
- **Base Size**: 16px

### Breakpoints
- **Desktop**: 1200px+
- **Tablet**: 768px - 1024px
- **Mobile**: < 768px

---

## 🧪 Testing

### Manual Testing Checklist

**Functionality**:
- [ ] All navigation links work
- [ ] Mobile menu opens/closes
- [ ] Contact form validation
- [ ] Resume download works
- [ ] Smooth scroll works

**Responsiveness**:
- [ ] Layout looks good on desktop (1200px+)
- [ ] Layout looks good on tablet (768px - 1024px)
- [ ] Layout looks good on mobile (< 768px)
- [ ] Text is readable at all sizes

**Performance**:
- [ ] Page loads in < 3 seconds
- [ ] No console errors
- [ ] Images optimized

### Running Tests

```bash
# Check Python syntax
python -m py_compile app.py

# Run Flask app and test manually
python app.py
```

---

## 🚀 Deployment

### Deploy to Render (Recommended)

1. Push code to GitHub
2. Create new Web Service on [Render](https://render.com)
3. Connect GitHub repository
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Deploy!

### Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Push to deploy
git push heroku main
```

### Environment Variables

For production deployment, set:

```bash
FLASK_ENV=production
FLASK_DEBUG=0
```

---

## 📞 Contact

**Pallavi R. Kamath**
- 📧 Email: pallavirkamath06@gmail.com
- 💼 LinkedIn: [linkedin.com/in/pallavirkamath](https://www.linkedin.com/in/pallavirkamath)
- 📍 Location: Udupi, India

---

## 🤝 Contributing

This is a personal portfolio. However, if you find bugs or have suggestions:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Fonts: [Google Fonts](https://fonts.google.com) (Inter, Playfair Display)
- Icons: [Font Awesome](https://fontawesome.com)
- Framework: [Flask](https://flask.palletsprojects.com)

---

**Built with ❤️ for showcasing healthcare management expertise.**
