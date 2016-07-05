{
    'name': "Website Template",

    'summary': """
        none
        """,

    'description': """
        none
    """,

    'author': "Tradeadvance Team",
    'website': "http://trad.com.ua",
    'category': 'ta-addons',
    'version': '0.0.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],
    # always loaded
    'data': [
        'views/templates.xml',
        'views/pages.xml',
    ],
}