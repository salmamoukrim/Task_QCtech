# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'QC TECH',
    'version': '1.1',
    'summary': 'QC TECH',
    'sequence': 15,
    'description': """
""",
    'category': '',
    'website': 'https://www.odoo.com/page/billing',
    'images': [''],
    'depends': ['base_setup', 'mail', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/city.xml',
        'views/stock_picking.xml',
        'views/drive.xml',
        'views/ride.xml'
        
        
    ],
    'demo': [
        
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}