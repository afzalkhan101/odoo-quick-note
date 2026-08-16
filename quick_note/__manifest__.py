{
    "name": "Quick Note",
    "version": "18.0.1.0.0",
    "summary": "Create and manage quick notes from anywhere in Odoo",
    "description": """
Quick Note
==========

A simple and powerful note-taking module for Odoo.

Features:
- Create quick notes from anywhere in Odoo.
- Global quick note access from the backend.
- Organize notes using categories.
- Easy note management.
- Clean and user-friendly interface.
- Compatible with Odoo 18 Community and Enterprise.

License:
OPL-1
""",
    "category": "Productivity",
    "author": "Your Company Name",
    "website": "https://yourwebsite.com",
    "license": "OPL-1",

    "depends": [
        "base",
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/quick_note_views.xml",
        "views/quick_note_category.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "quick_note/static/src/js/global_quick_note.js",
            "quick_note/static/src/xml/global_quick_note.xml",
            "quick_note/static/src/css/global_quick_note.css",
        ],
    },

    "images": [
        "static/description/banner.png",
        "static/description/icon.png",
    ],

    # Odoo Apps Store pricing
    "price": 39.00,
    "currency": "USD",

    "installable": True,
    "application": True,
    "auto_install": False,
}