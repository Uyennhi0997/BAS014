# -*- coding: utf-8 -*-
{
    'name': "cms_web",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'co_cms'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/frontend/assets.xml',
        'views/frontend/layout.xml',
        'views/frontend/header.xml',
        'views/frontend/shop.xml',
        'views/frontend/about.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
