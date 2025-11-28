// ============================================
// PORTFOLIO WEBSITE JAVASCRIPT
// Smooth scroll animations and interactive effects
// ============================================

// Wait for page to load
document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // Smooth Scroll Animations
    // ============================================
    
    // Function to check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Function to check if element is partially visible
    function isPartiallyVisible(element) {
        const rect = element.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        return (
            rect.top < windowHeight &&
            rect.bottom > 0
        );
    }
    
    // Animate portfolio cards on home page
    function animatePortfolioCards() {
        const cards = document.querySelectorAll('.portfolio-card');
        cards.forEach((card, index) => {
            if (isPartiallyVisible(card)) {
                setTimeout(() => {
                    card.classList.add('fade-in');
                }, index * 100); // Stagger animation
            }
        });
    }
    
    // Animate video wrappers on portfolio pages
    function animateVideoWrappers() {
        const videos = document.querySelectorAll('.video-wrapper');
        videos.forEach((video, index) => {
            if (isPartiallyVisible(video)) {
                setTimeout(() => {
                    video.classList.add('fade-in');
                }, index * 100); // Stagger animation
            }
        });
    }
    
    // Run animations on scroll
    function handleScroll() {
        animatePortfolioCards();
        animateVideoWrappers();
    }
    
    // Initial check
    handleScroll();
    
    // Check on scroll (with throttling for performance)
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    });
    
    // ============================================
    // Navigation Hover Effects
    // ============================================
    
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.15)';
        });
        link.addEventListener('mouseleave', function() {
            if (!this.classList.contains('active')) {
                this.style.transform = 'scale(1)';
            }
        });
    });
    
    // ============================================
    // Portfolio Card Hover Effects
    // ============================================
    
    const portfolioCards = document.querySelectorAll('.portfolio-card');
    portfolioCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // Additional hover effects can be added here
        });
    });
    
    // ============================================
    // Smooth Page Transitions
    // ============================================
    
    // Add fade-in effect to body on page load
    document.body.style.opacity = '0';
    window.addEventListener('load', function() {
        document.body.style.transition = 'opacity 0.3s ease';
        document.body.style.opacity = '1';
    });
    
    // ============================================
    // Navigation Active State
    // ============================================
    
    // Highlight current page in navigation
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (linkPath === currentPath || 
            (currentPath === '/' && linkPath === '/index.html') ||
            (currentPath === '' && linkPath === '/')) {
            link.classList.add('active');
        }
    });
    
    // ============================================
    // Intersection Observer for Better Performance
    // ============================================
    
    // Use Intersection Observer for more efficient scroll animations
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };
        
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        // Observe portfolio cards
        document.querySelectorAll('.portfolio-card').forEach(card => {
            observer.observe(card);
        });
        
        // Observe video wrappers
        document.querySelectorAll('.video-wrapper').forEach(video => {
            observer.observe(video);
        });
    }
    
    // ============================================
    // Console Welcome Message
    // ============================================
    
    console.log('%c🎨 Portfolio Website Loaded!', 'color: #667eea; font-size: 20px; font-weight: bold;');
    console.log('%cEdit config.py to customize your content!', 'color: #764ba2; font-size: 14px;');
    
});

