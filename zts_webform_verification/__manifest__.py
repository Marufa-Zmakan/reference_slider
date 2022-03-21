# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Get webform details for verification',
    'version' : '1.1',
    'sequence': 10,
    'description': """Get webform details for verification""",
    'category': 'Website',
    'website': 'www.zmakan.com',
    'depends' : ['website','base','website_profile'],
    'data': [
        'views/portal_user_form.xml',
        'data/mail_template.xml'
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
