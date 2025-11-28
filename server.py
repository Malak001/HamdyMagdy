#!/usr/bin/env python3
"""
Simple Python HTTP Server for the Portfolio Website
Run this file to start your website: python server.py
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Port to run the server on
PORT = 8000

# Get the project root directory (parent of python folder)
BASE_DIR = Path(__file__).parent.parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow loading resources
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Parse the path
        path = self.path.split('?')[0]  # Remove query parameters
        
        # Route to appropriate folders
        if path == '/' or path == '':
            # Serve index.html
            self.path = '/html/index.html'
        elif path.endswith('.html'):
            # Serve HTML files from html folder
            if not path.startswith('/html/'):
                self.path = '/html' + path
        elif path.endswith('.css'):
            # Serve CSS files from css_js folder
            if '/css_js/' not in path:
                filename = path.split('/')[-1]
                self.path = f'/css_js/{filename}'
        elif path.endswith('.js'):
            # Serve JS files from css_js folder
            if '/css_js/' not in path:
                filename = path.split('/')[-1]
                self.path = f'/css_js/{filename}'
        
        # Call parent method to serve the file
        return super().do_GET()

    def log_message(self, format, *args):
        # Custom log format
        sys.stderr.write("%s - - [%s] %s\n" %
                        (self.address_string(),
                         self.log_date_time_string(),
                         format%args))

def main():
    # Change to the project root directory
    os.chdir(BASE_DIR)
    
    # Create server
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print(f"🚀 Portfolio Website Server Running!")
        print(f"📂 Serving from: {BASE_DIR}")
        print(f"🌐 Open your browser at: http://localhost:{PORT}")
        print("=" * 60)
        print("Press Ctrl+C to stop the server")
        print("=" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()

