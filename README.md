# 🎨 Portfolio Website - HTML/CSS/Python Version

A vibrant, modern portfolio website built with **pure HTML, CSS, and JavaScript**, served with Python!

## 📁 Project Structure

The project is organized into 3 folders by language:

```
.
├── python/              # 🐍 Python files
│   ├── config.py       # ⭐ EDIT THIS - All your content
│   ├── generate_html.py # Generates HTML from config
│   └── server.py        # Web server
├── html/                # 📄 HTML files (generated)
│   ├── index.html
│   ├── video-edit.html
│   ├── ai-videos.html
│   ├── motion.html
│   └── vfx.html
└── css_js/              # 🎨 CSS & JavaScript
    ├── styles.css       # All styling
    └── script.js        # Animations
```

## 🚀 Quick Start

### 1. Edit Your Content
Open `python/config.py` and edit your information:
- Your name, title, and intro text
- Contact information and social media links
- Portfolio section titles and descriptions
- Your video links

### 2. Generate HTML Files
After editing `python/config.py`, run:
```bash
python3 python/generate_html.py
```

This creates all the HTML files in the `html/` folder.

### 3. Start the Server
```bash
python3 python/server.py
```

Your website will be available at: **http://localhost:8000**

---

## 📝 How to Edit

### **Everything is in `python/config.py`!**

Just open `python/config.py` and follow the comments. They tell you exactly what to change:

```python
NAME = "Hamdy Magdy"  # ← Change this to your name
PROFESSIONAL_TITLE = "Video Editor & Creative Professional"  # ← Change this
```

### After Editing:

1. **Save `python/config.py`**
2. **Run `python3 python/generate_html.py`** to update HTML files
3. **Refresh your browser** (or restart the server)

---

## 🎬 Adding Videos

### YouTube:
1. Go to your video → Click "Share" → Click "Embed"
2. Copy: `https://www.youtube.com/embed/VIDEO_ID`
3. Paste in `python/config.py` in the `VIDEOS` section

### Vimeo:
1. Go to your video → Click "Share" → Click "Embed"
2. Copy: `https://player.vimeo.com/video/VIDEO_ID`
3. Paste in `python/config.py` in the `VIDEOS` section

---

## ✨ Features

- ✅ **5 Pages**: Home + 4 portfolio sections
- ✅ **Vibrant Design**: Bold gradients and modern styling
- ✅ **Smooth Animations**: Scroll-triggered fade-ins
- ✅ **Responsive**: Works on all devices
- ✅ **Easy to Edit**: Just edit `python/config.py`!
- ✅ **Organized**: Files separated by language type

---

## 🛠️ Workflow

1. **Edit** `python/config.py` with your content
2. **Generate** HTML: `python3 python/generate_html.py`
3. **Serve** website: `python3 python/server.py`
4. **View** at http://localhost:8000

---

## 💡 Tips

- **Read the comments** in `python/config.py` - they explain everything!
- **Keep quotes** around text: `"Your Text"`
- **Save and regenerate** after editing config
- **No need to edit HTML** - it's all generated!

---

## 🆘 Troubleshooting

**Problem:** Changes don't show up
- **Solution:** Run `python3 python/generate_html.py` after editing `python/config.py`

**Problem:** Server won't start
- **Solution:** Make sure port 8000 is available, or edit `PORT = 8000` in `python/server.py`

**Problem:** Videos don't show
- **Solution:** Make sure video URLs start with `https://www.youtube.com/embed/` or `https://player.vimeo.com/video/`

**Problem:** CSS/JS not loading
- **Solution:** Make sure you're running the server from the project root, not from inside a folder

---

## 🎉 You're Ready!

Just edit `python/config.py`, generate HTML, and serve! It's that simple! 🚀
