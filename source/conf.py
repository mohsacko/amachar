# Path setup
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

def setup(app):
    app.add_css_file("custom.css")
    app.add_css_file("team.css")

project = 'Association des Maliens de Charlotte (AMACHAR)'
author = 'Mohamed Sacko'
release = '1.0'
language = 'fr'
extensions = []
templates_path = ['_templates']
exclude_patterns = []
html_title = "Association des Maliens de Charlotte (AMACHAR)"
html_theme = 'furo'
html_static_path = ['_static']
html_js_files = []
# -- HTML options ------------------------------------------------------------
html_logo = "_static/amachar_logo.png"  # ✅ Your logo path
html_theme_options = {
    "light_logo": "amachar_logo.png",
    "dark_logo": "amachar_logo.png",
    "navigation_with_keys": True,
    "sidebar_hide_name": False,
    "source_repository": "https://github.com/mohsacko/amachar/",
    "source_branch": "main",
    "path_to_docs": "docs",
    "base_url": "https://mohsacko.github.io/amachar/"
}
html_baseurl = "https://mohsacko.github.io/amachar/"
