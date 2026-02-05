# Agent Documentation - Pallavi Portfolio

**Purpose**: This file provides essential context for AI agents and developers working on this codebase.

---

## 🎯 Project Overview

**Project Type**: Professional Portfolio Website  
**Framework**: Flask (Python) + HTML/CSS/JS  
**Target Audience**: Healthcare industry professionals, recruiters, potential clients  
**Website Goal**: Showcase Pallavi's expertise in healthcare management, process improvement, and operational excellence

**Key Value Propositions**:
- National award winner (Qimpro QualTech Prize)
- 95% operational efficiency improvement achieved
- Pre-operational planning for 35-bed clinical facility
- Lean Six Sigma Yellow Belt certified

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Flask App                           │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │    Routes    │  │   Template   │  │  Static Assets  │   │
│  │   (app.py)   │──│   Rendering  │──│   (CSS/JS/Img)  │   │
│  └──────────────┘  └──────────────┘  └─────────────────┘   │
│         │                                                      │
│         ▼                                                      │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              portfolio_data Dictionary                   │  │
│  │  (Centralized content - modify this to update site)      │  │
│  └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Common Tasks for Agents

### 1. Update Content

**Location**: `app.py` → `portfolio_data` dictionary

**What to modify**:
```python
portfolio_data = {
    "name": "Dr. Pallavi R. Kamath",  # Change name
    "email": "newemail@example.com",   # Update email
    "phone": "+91 9876543210",          # Update phone
    # ... etc
}
```

**Impact**: Changes automatically reflect across all pages that use that data.

### 2. Add/Remove Pages

**Steps**:
1. Create route in `app.py`:
```python
@app.route('/newpage')
def newpage():
    return render_template('newpage.html', data=portfolio_data)
```

2. Create template `templates/newpage.html`:
```html
{% extends "base.html" %}
{% block content %}
    <!-- Your content here -->
{% endblock %}
```

3. Add link to navigation in `templates/base.html`:
```html
<li><a href="{{ url_for('newpage') }}" class="nav-link">New Page</a></li>
```

### 3. Add Photos

**Location**: `static/images/`

**Current placeholder**: In `templates/index.html`, replace:
```html
<!-- REPLACE THIS -->
<div class="profile-image-placeholder">
    <i class="fas fa-user"></i>
    <span>Photo Coming Soon</span>
</div>

<!-- WITH THIS -->
<div class="profile-image">
    <img src="{{ url_for('static', filename='images/photo.jpg') }}" 
         alt="Dr. Pallavi R. Kamath">
</div>
```

**Image optimization tips**:
- Use WebP format when possible
- Recommended size: 600x800px for profile
- Compress images before adding

### 4. Change Colors/Theme

**Location**: `static/css/style.css` → `:root` selector

**Key variables**:
```css
:root {
    --primary: #1e3a5f;      /* Main brand color */
    --secondary: #0d9488;     /* Accent color */
    --accent: #f59e0b;        /* Highlight/award color */
    /* ... more variables */
}
```

**Design constraints**:
- Keep it professional (healthcare industry)
- Maintain good contrast ratios (accessibility)
- Test on mobile devices

### 5. Add New Sections

**Pattern to follow**:
1. Add data to `portfolio_data` in `app.py` if needed
2. Add HTML structure to appropriate template
3. Add CSS styles to `static/css/style.css` (search for similar sections)
4. Add any JS interactions to `static/js/main.js`

---

## 🔧 Technical Reference

### Jinja2 Template Syntax

This project uses Jinja2 templating. Common patterns:

```html
<!-- Variable interpolation -->
<h1>{{ data.name }}</h1>

<!-- Conditionals -->
{% if data.awards %}
    <div class="awards">...</div>
{% endif %}

<!-- Loops -->
{% for job in data.experience %}
    <h3>{{ job.role }}</h3>
{% endfor %}

<!-- Template inheritance -->
{% extends "base.html" %}
{% block content %}
    <!-- Page-specific content -->
{% endblock %}
```

### CSS Architecture

**BEM-like naming** (not strict BEM):
- `.section-name` - Section container
- `.section-name-card` - Card components
- `.section-name-grid` - Grid layouts
- Modifiers: `.btn-primary`, `.btn-outline`

**Responsive breakpoints**:
- Desktop: default styles
- Tablet: `@media (max-width: 1024px)`
- Mobile: `@media (max-width: 768px)`
- Small mobile: `@media (max-width: 480px)`

### JavaScript Patterns

**Module structure**: Each feature is in its own init function
```javascript
function initFeature() {
    // Feature code here
}
```

**Adding new JS**:
1. Add init function at the bottom of the file
2. Call it in `DOMContentLoaded` event listener
3. Follow existing JSDoc commenting style

---

## ⚠️ Important Notes

### DON'Ts

1. **Don't hardcode content in templates** - Always use `portfolio_data` from `app.py`
2. **Don't modify CSS without checking responsive** - Test at 1024px, 768px, 480px
3. **Don't add heavy JS libraries** - Keep it lightweight
4. **Don't break the Flask route structure** - Maintain `data=portfolio_data` in all routes

### DOs

1. **DO add comments** for complex logic
2. **DO test on mobile** after any CSS changes
3. **DO validate HTML** if making template changes
4. **DO check accessibility** (contrast, alt text, semantic HTML)

### File Naming Conventions

- Templates: `lowercase.html` (e.g., `index.html`)
- CSS: `kebab-case.css` (e.g., `style.css`)
- JS: `kebab-case.js` (e.g., `main.js`)
- Images: `descriptive-name.ext` (e.g., `profile-photo.jpg`)

---

## 🧪 Testing Checklist

When making changes, verify:

- [ ] Site loads without errors (check browser console)
- [ ] Navigation works on all pages
- [ ] Mobile menu opens/closes correctly
- [ ] All links are functional
- [ ] Contact form validation works
- [ ] Resume download works
- [ ] Page looks good at all breakpoints:
  - [ ] Desktop (1200px+)
  - [ ] Tablet (768px - 1024px)
  - [ ] Mobile (< 768px)

---

## 📦 Dependencies

Listed in `requirements.txt`:
- Flask 3.1.2 - Web framework
- gunicorn 23.0.0 - WSGI server (production)
- python-dotenv 1.0.1 - Environment variables

**External CDNs used in templates**:
- Google Fonts (Inter, Playfair Display)
- Font Awesome 6.4.0 (icons)

---

## 🚀 Deployment

**Platforms tested**: Render, Heroku, PythonAnywhere

**Environment variables**:
```bash
FLASK_ENV=production      # Required
FLASK_DEBUG=0            # Recommended for production
```

**Procfile**: `web: gunicorn app:app`

---

## 📞 Questions?

If something is unclear:
1. Check existing code patterns - follow what's already there
2. Read `README.md` for user-facing documentation
3. Look at similar sections for implementation examples
4. When in doubt, prioritize simplicity and maintainability

---

**Last Updated**: 2026-02-05  
**Maintainer**: Pallavi R. Kamath
