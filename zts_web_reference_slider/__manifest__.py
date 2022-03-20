# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Website Reference Slider',
    'version' : '1.1',
    'sequence': 10,
    'description': """SLider""",
    'category': 'Website',
    'website': 'www.zmakan.com',
    'depends' : ['website','base'],
    'data': [
        'views/contact_us_map.xml',
        'views/snippet_reference.xml',
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
