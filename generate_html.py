#!/usr/bin/env python3
"""
This script generates HTML files from the config.py file
Run this after editing config.py to update your website
"""

import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.insert(0, str(Path(__file__).parent))
import config

def escape_html(text):
    """Escape HTML special characters"""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;"))

def generate_navigation(current_page=""):
    """Generate navigation HTML"""
    nav_items = [
        ("index.html", "Home"),
        ("video-edit.html", "Video Edit"),
        ("ai-videos.html", "AI Videos"),
        ("motion.html", "Motion"),
        ("vfx.html", "VFX")
    ]
    
    nav_html = '<nav class="navigation">\n'
    nav_html += '  <div class="nav-container">\n'
    nav_html += '    <a href="index.html" class="nav-logo"><span>HM</span></a>\n'
    nav_html += '    <ul class="nav-menu">\n'
    
    for path, label in nav_items:
        active_class = ' class="active"' if (current_page == path or 
                                            (current_page == "" and path == "index.html")) else ""
        nav_html += f'      <li><a href="{path}"{active_class}>{label}</a></li>\n'
    
    nav_html += '    </ul>\n'
    nav_html += '  </div>\n'
    nav_html += '</nav>\n'
    
    return nav_html

def generate_footer():
    """Generate footer HTML"""
    footer_html = '<footer class="footer">\n'
    footer_html += '  <div class="footer-container">\n'
    footer_html += '    <div class="footer-content">\n'
    footer_html += '      <div class="footer-section">\n'
    footer_html += '        <h3>Get In Touch</h3>\n'
    footer_html += f'        <a href="mailto:{config.CONTACT_EMAIL}" class="footer-email">{config.CONTACT_EMAIL}</a>\n'
    footer_html += '      </div>\n'
    footer_html += '      <div class="footer-section">\n'
    footer_html += '        <h3>Follow Me</h3>\n'
    footer_html += '        <div class="social-links">\n'
    
    # Social media icon SVG paths (just the path data, not the full <path> tag)
    social_icons = {
        "instagram": "M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z",
        "youtube": "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z",
        "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
        "twitter": "M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"
    }
    
    for platform, url in config.SOCIAL_MEDIA.items():
        if platform in social_icons:
            footer_html += f'          <a href="{url}" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="{platform.capitalize()}">\n'
            footer_html += f'            <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="{social_icons[platform]}"/></svg>\n'
            footer_html += '          </a>\n'
    
    footer_html += '        </div>\n'
    footer_html += '      </div>\n'
    footer_html += '    </div>\n'
    footer_html += f'    <div class="footer-bottom"><p>&copy; {__import__("datetime").datetime.now().year} {config.NAME}. All rights reserved.</p></div>\n'
    footer_html += '  </div>\n'
    footer_html += '</footer>\n'
    
    return footer_html

def generate_home_page():
    """Generate the home page HTML"""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config.NAME} - {config.PROFESSIONAL_TITLE}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css_js/styles.css">
</head>
<body>
    {generate_navigation("index.html")}
    
    <div class="home-page">
        <section class="hero-section">
            <div class="hero-content">
                <h1 class="hero-name">{escape_html(config.NAME)}</h1>
                <p class="hero-title">{escape_html(config.PROFESSIONAL_TITLE)}</p>
                <p class="hero-intro">{escape_html(config.INTRO_TEXT)}</p>
            </div>
        </section>

        <section class="portfolio-cards-section">
            <div class="cards-container">
                <a href="video-edit.html" class="portfolio-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                    <div class="card-content">
                        <h2 class="card-title">{escape_html(config.SECTIONS["video_edit"]["title"])}</h2>
                        <div class="card-arrow">→</div>
                    </div>
                    <div class="card-overlay"></div>
                </a>
                <a href="ai-videos.html" class="portfolio-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                    <div class="card-content">
                        <h2 class="card-title">{escape_html(config.SECTIONS["ai_videos"]["title"])}</h2>
                        <div class="card-arrow">→</div>
                    </div>
                    <div class="card-overlay"></div>
                </a>
                <a href="motion.html" class="portfolio-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                    <div class="card-content">
                        <h2 class="card-title">{escape_html(config.SECTIONS["motion"]["title"])}</h2>
                        <div class="card-arrow">→</div>
                    </div>
                    <div class="card-overlay"></div>
                </a>
                <a href="vfx.html" class="portfolio-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
                    <div class="card-content">
                        <h2 class="card-title">{escape_html(config.SECTIONS["vfx"]["title"])}</h2>
                        <div class="card-arrow">→</div>
                    </div>
                    <div class="card-overlay"></div>
                </a>
            </div>
        </section>
    </div>

    {generate_footer()}
    <script src="../css_js/script.js"></script>
</body>
</html>'''
    return html

def generate_portfolio_page(section_key):
    """Generate a portfolio page HTML"""
    section = config.SECTIONS[section_key]
    videos = config.VIDEOS[section_key]
    page_name = section_key.replace("_", "-")
    
    videos_html = ""
    for video_url in videos:
        videos_html += f'''                <div class="video-wrapper">
                    <div class="video-container">
                        <iframe
                            src="{video_url}"
                            title="{escape_html(section["title"])} Video"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen
                            class="video-embed"
                        ></iframe>
                    </div>
                </div>
'''
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_html(section["title"])} - {config.NAME}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css_js/styles.css">
</head>
<body>
    {generate_navigation(f"{page_name}.html")}
    
    <div class="portfolio-page">
        <section class="portfolio-header">
            <h1 class="portfolio-title">{escape_html(section["title"])}</h1>
            <p class="portfolio-description">{escape_html(section["description"])}</p>
        </section>

        <section class="portfolio-videos">
            <div class="videos-grid">
{videos_html}
            </div>
        </section>
    </div>

    {generate_footer()}
    <script src="../css_js/script.js"></script>
</body>
</html>'''
    return html

def main():
    """Generate all HTML files"""
    print("Generating HTML files from config.py...")
    
    # Get the project root directory (parent of python folder)
    project_root = Path(__file__).parent.parent
    html_dir = project_root / "html"
    html_dir.mkdir(exist_ok=True)
    
    # Generate home page
    with open(html_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_home_page())
    print("✓ Generated index.html")
    
    # Generate portfolio pages
    pages = {
        "video_edit": "video-edit.html",
        "ai_videos": "ai-videos.html",
        "motion": "motion.html",
        "vfx": "vfx.html"
    }
    
    for section_key, filename in pages.items():
        with open(html_dir / filename, "w", encoding="utf-8") as f:
            f.write(generate_portfolio_page(section_key))
        print(f"✓ Generated {filename}")
    
    print("\n✅ All HTML files generated successfully!")
    print("Run 'python python/server.py' to start your website!")

if __name__ == "__main__":
    main()

