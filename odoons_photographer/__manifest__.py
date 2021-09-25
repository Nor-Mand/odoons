# -*- coding: utf-8 -*-
{
    'name': "Photographer",
    'summary': """This modulo is to take control about sesions of clients, products, retouch, shooting""",
    'depends':['base'],
    'application': True
    'data': [
        'views/photographer_view.xml'
        'secutiry/photographer_security.xml',
        'secutiry/ir.model.access.csv'
    ]
}