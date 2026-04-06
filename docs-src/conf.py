project = 'NatureLM-audio'
copyright = '2025, Earth Species Project'
author = 'Earth Species Project'
release = '1.0.0'

extensions = [
    'myst_parser',
    'sphinx_copybutton',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]
myst_heading_anchors = 3
myst_all_links_external = True
myst_links_external_new_tab = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'furo'

html_theme_options = {
    "sidebar_hide_name": True,
    "globaltoc_collapse": False,
    "source_view_link": "https://github.com/earthspecies/NatureLM-audio",
    "light_css_variables": {
        "color-brand-primary": "#129C7B",
        "color-brand-content": "#129C7B",
        "color-brand-visited": "#054C3B",
    },
    "dark_css_variables": {
        "color-brand-primary": "#04D78A",
        "color-brand-content": "#04D78A",
        "color-brand-visited": "#A7ED99",
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#dedede",
        "color-foreground-muted": "#888888",
    },
    "light_logo": "esp-logotype-only-black.png",
    "dark_logo": "esp-logotype-only-white.png",
}

html_extra_path = []

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/home-link.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

html_title = "NatureLM-audio"
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_favicon = "_static/favicon.svg"
