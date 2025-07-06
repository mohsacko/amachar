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
# -- HTML options ------------------------------------------------------------
html_logo = "_static/amachar_logo.png"  # ✅ Your logo path
html_theme_options = {
    "logo_only": False,  # True = logo only, False = logo + title
    "display_version": False,
}