/**
 * Pallavi R. Kamath Portfolio - Main JavaScript
 * =============================================
 * 
 * This file handles all interactive functionality for the portfolio website:
 * - Mobile navigation toggle
 * - Smooth scrolling
 * - Scroll-based animations
 * - Form validation
 * - Navbar behavior
 * 
 * @author Pallavi R. Kamath
 * @fileoverview Main JavaScript module for portfolio interactivity
 */

// =============================================================================
// INITIALIZATION
// =============================================================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality when DOM is fully loaded
    initNavigation();
    initNavbarScroll();
    initSmoothScroll();
    initScrollAnimations();
    initFormValidation();
    initActiveNavLink();
});


// =============================================================================
// MODULE: Navigation
// =============================================================================

/**
 * Initialize mobile navigation functionality
 * Handles hamburger menu toggle and click-outside-to-close behavior
 * 
 * @function initNavigation
 */
function initNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Exit if elements don't exist (should not happen in normal operation)
    if (!navToggle || !navMenu) {
        console.warn('Navigation elements not found');
        return;
    }
    
    /**
     * Close mobile menu and reset accessibility state
     */
    function closeMenu() {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
    }

    /**
     * Toggle mobile menu open/closed state
     * Adds/removes 'active' class to both menu and toggle button
     */
    navToggle.addEventListener('click', function() {
        const isOpen = navMenu.classList.toggle('active');
        this.classList.toggle('active', isOpen);
        this.setAttribute('aria-expanded', String(isOpen));
    });
    
    /**
     * Close menu when clicking a navigation link
     * Provides immediate feedback on mobile
     */
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            closeMenu();
        });
    });
    
    /**
     * Close menu when clicking outside the navigation
     * Improves UX by allowing users to dismiss menu easily
     */
    document.addEventListener('click', function(e) {
        if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
            closeMenu();
        }
    });
}


// =============================================================================
// MODULE: Navbar Scroll Effects
// =============================================================================

/**
 * Initialize navbar scroll behavior
 * - Adds shadow on scroll
 * - Hides navbar when scrolling down, shows when scrolling up
 * 
 * @function initNavbarScroll
 */
function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    
    if (!navbar) return;
    
    let lastScroll = 0;
    const scrollThreshold = 50;  // Pixels to scroll before adding shadow
    const hideThreshold = 100;   // Pixels to scroll before hiding navbar
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        // Add/remove shadow based on scroll position
        if (currentScroll > scrollThreshold) {
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }
        
        // Hide/show navbar based on scroll direction
        // Only hide after scrolling past hideThreshold
        if (currentScroll > lastScroll && currentScroll > hideThreshold) {
            // Scrolling down - hide navbar
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up - show navbar
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
}


// =============================================================================
// MODULE: Smooth Scrolling
// =============================================================================

/**
 * Initialize smooth scrolling for anchor links
 * Accounts for fixed navbar height when calculating scroll position
 * 
 * @function initSmoothScroll
 */
function initSmoothScroll() {
    // Select all anchor links that point to IDs
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);
            
            if (target) {
                // Offset for fixed navbar (72px height + some padding)
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}


// =============================================================================
// MODULE: Scroll Animations
// =============================================================================

/**
 * Initialize fade-in animations triggered by scroll
 * Uses Intersection Observer API for performance
 * 
 * @function initScrollAnimations
 */
function initScrollAnimations() {
    // Configuration for Intersection Observer
    const observerOptions = {
        root: null,              // Viewport
        rootMargin: '0px',       // No margin
        threshold: 0.1          // Trigger when 10% visible
    };
    
    /**
     * Intersection Observer callback
     * Adds 'fade-in-visible' class when element enters viewport
     * 
     * @param {IntersectionObserverEntry[]} entries
     * @param {IntersectionObserver} observer
     */
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
                // Stop observing once animation is triggered
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Elements to animate (add your selectors here as needed)
    const animateSelectors = [
        '.about-card',
        '.skill-category',
        '.cert-card',
        '.leadership-card',
        '.timeline-item',
        '.edu-item',
        '.collab-card',
        '.award-detail-card'
    ];
    
    // Add animation class to all matching elements
    const animateElements = document.querySelectorAll(animateSelectors.join(', '));
    
    animateElements.forEach((el, index) => {
        el.classList.add('fade-in');
        // Stagger animations based on element index
        el.style.transitionDelay = `${index * 0.05}s`;
        observer.observe(el);
    });
    
    // Inject CSS for animations
    injectAnimationStyles();
}

/**
 * Inject CSS styles for fade-in animations
 * Creates a <style> element and appends to <head>
 * 
 * @function injectAnimationStyles
 */
function injectAnimationStyles() {
    // Check if styles already exist
    if (document.getElementById('fade-in-styles')) return;
    
    const style = document.createElement('style');
    style.id = 'fade-in-styles';
    style.textContent = `
        .fade-in {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        .fade-in-visible {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);
}


// =============================================================================
// MODULE: Form Validation
// =============================================================================

/**
 * Initialize contact form validation
 * Validates email format before submission
 * 
 * @function initFormValidation
 */
function initFormValidation() {
    const contactForm = document.querySelector('.contact-form');
    
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', function(e) {
        const emailInput = document.getElementById('email');
        
        if (!emailInput) return;
        
        const email = emailInput.value;
        
        // Email validation regex pattern
        // Matches: text@domain.tld
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (!emailPattern.test(email)) {
            e.preventDefault();  // Stop form submission
            
            // Visual error indication
            emailInput.style.borderColor = '#ef4444';
            
            // Show error message
            showFieldError(emailInput, 'Please enter a valid email address');
        } else {
            // Clear any existing errors
            emailInput.style.borderColor = '';
            clearFieldError(emailInput);
        }
    });
}

/**
 * Display error message below a form field
 * 
 * @param {HTMLElement} input - The input element
 * @param {string} message - Error message to display
 */
function showFieldError(input, message) {
    // Check if error already exists
    let errorMsg = input.parentElement.querySelector('.error-message');
    
    if (!errorMsg) {
        errorMsg = document.createElement('span');
        errorMsg.className = 'error-message';
        errorMsg.style.cssText = `
            color: #ef4444;
            font-size: 13px;
            margin-top: 4px;
            display: block;
        `;
        input.parentElement.appendChild(errorMsg);
    }
    
    errorMsg.textContent = message;
}

/**
 * Remove error message from a form field
 * 
 * @param {HTMLElement} input - The input element
 */
function clearFieldError(input) {
    const errorMsg = input.parentElement.querySelector('.error-message');
    if (errorMsg) {
        errorMsg.remove();
    }
}


// =============================================================================
// MODULE: Active Navigation Link
// =============================================================================

/**
 * Update active state of navigation links based on scroll position
 * Highlights the nav link corresponding to the current section
 * 
 * @function initActiveNavLink
 */
function initActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    if (sections.length === 0 || navLinks.length === 0) return;

    // Only run scroll-based highlighting when nav links target on-page sections.
    // Current top-nav links are route URLs, so this avoids removing server-rendered active state.
    const sectionNavLinks = Array.from(navLinks).filter(link => {
        const href = link.getAttribute('href') || '';
        return href.startsWith('#');
    });

    if (sectionNavLinks.length === 0) return;
    
    window.addEventListener('scroll', debounce(function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            
            // Update current when section is in view (with 200px offset)
            if (window.pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        // Update active class on nav links
        sectionNavLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }, 100));  // Debounce for performance
}


// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

/**
 * Debounce function to limit execution rate
 * Useful for scroll/resize event handlers
 * 
 * @param {Function} func - Function to debounce
 * @param {number} wait - Milliseconds to wait
 * @returns {Function} Debounced function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}


// =============================================================================
// LAZY LOADING (Future Enhancement)
// =============================================================================

/**
 * Initialize lazy loading for images
 * Images with 'data-src' attribute will load when entering viewport
 * 
 * Usage: <img data-src="path/to/image.jpg" src="placeholder.jpg">
 * 
 * @function initLazyLoading
 */
function initLazyLoading() {
    // Check if browser supports Intersection Observer
    if (!('IntersectionObserver' in window)) {
        // Fallback: Load all images immediately
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.dataset.src;
        });
        return;
    }
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                
                // Switch from data-src to src
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                }
                
                // Stop observing this image
                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px 0px',  // Start loading 50px before visible
        threshold: 0.01
    });
    
    // Observe all images with data-src
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Initialize lazy loading (uncomment when images are added)
// document.addEventListener('DOMContentLoaded', initLazyLoading);
