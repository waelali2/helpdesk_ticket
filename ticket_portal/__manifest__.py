{
    "name": "Portal tickets",
    "summary": """
        attendances
    """,
    "author": "wael",
    "category": "Human Resources",
    "version": "15.0.0.0.0",
    "license": "AGPL-3",
    'depends': ['website', 'hr_attendance', 'portal','helpdesk'],
    "installable": True,
    "application": False,
    "auto_install": False,

    'data': [
        'views/views.xml'
    ],
}
