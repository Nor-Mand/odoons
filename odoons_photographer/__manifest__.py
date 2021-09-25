# -*- coding: utf-8 -*-
{
    'name': "Photographer",
    'summary': """This modulo is to take control about sesions of clients, products, retouch, shooting""",
    'depends':['base'],
    'application': True,
    'data': [
        'views/photographer_view.xml',
        'security/photographer_security.xml',
        'security/ir.model.access.csv',
    ]
}