# -*- coding: utf-8 -*-
{
    'name': "My Library",
    'summary': """Manage books easily""",
    'description': """Manage Library""",
    'author': "Nor-Mand",
    'website': "http://www.normandweb.com",
    'category': "Uncategorized",
    'version': '13.0.1',
    'depends': ['base','mail','hexacorp_garantias'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_category.xml',
        'views/fields_models_view.xml',
    ],
    'application': True,
}