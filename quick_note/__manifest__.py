{
    "name": "quick_note",
    "version": "18.0.1.0.0",
    "summary": "",
    "description": "",
    "category": "",
    "author": "",
    "website": "",
    "license": "OPL-1",

    "depends": [
        "base",
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/quick_note_views.xml",
        "views/quick_note_category.xml"
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

    "installable": True,
    "application": True,
    "auto_install": False,
}