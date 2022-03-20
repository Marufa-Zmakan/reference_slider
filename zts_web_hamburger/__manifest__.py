# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Website Hamburger',
    'version' : '1.1',
    'summary': 'zts_web_hamburger',
    'sequence': 10,
    'description': """zts_web_hamburger""",
    'category': 'Website',
    'website': 'www.zmakan.com',
    'depends' : ['website','base'],
    'data': ['views/hamburger.xml',
             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
