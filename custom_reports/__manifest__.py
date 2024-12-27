# -*- coding: utf-8 -*-
{
    'name': "custom_reports",

    'summary': "Custom reports for Tomidp",

    'description': """
        Slovenian translation and customization of reports for Tomidp
    """,

    'author': "Neo X Kirbiš",
    'website': "neoxk.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        'report/sale_report_inherit.xml' 
    ],
    'installable': True,
    'application': False 

}

