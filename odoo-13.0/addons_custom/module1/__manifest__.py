# -*- coding: utf-8 -*-
{
    'name': "module1",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "FinnD",
    'website': "https://fb.com",
    'license':'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'data':[
            "views/player.xml",
        ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'installable': True,
    'application': False,
    'auto_install': False,
    

}
