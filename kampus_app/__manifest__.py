# -*- coding: utf-8 -*-
{
    'name' : 'Kampus',
    'description':'aplikasi sederhana',
    'version' : '1.0',
    'sequence':-100,
    'description': """mecoba memahami odoo 14""",
    'summary' : 'dibuat dengan menggunakan odoo14',
    'website' :'https://univodoo.com',
    'locense' :'LGPL-3',
    'category': 'Productivity',
    'depends' : [],
    'data': [
        'views/mahasiswa.xml',
        'security/ir.model.access.csv'

    ],
    'qweb' :[],
    'installable': True,
    'application': True,
    'auto_install': False,
}
