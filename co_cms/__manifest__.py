# -*- coding: utf-8 -*-
{
    'name': "CMS",

    'summary': """
        + Thiết lập danh sách banner (hình ảnh) hiển thị,
        + Thiết lập style của banner ( vd: bo tròng, hiển thị full, hiển thị 90%, viềng vuông, ...)
        + Thiết lập style hiển thị cho cụm category ( cụm danh mục sản phẩm)
        + Thiết lập style hiển thị cho cụm sản phẩm ( vd: grid, slide, list, ...)
        + Thiết lập popup quảng cáo, vị trí hiện, ...
        + ...""",

    'description': """
        + Thiết lập danh sách banner (hình ảnh) hiển thị,
        + Thiết lập style của banner ( vd: bo tròng, hiển thị full, hiển thị 90%, viềng vuông, ...)
        + Thiết lập style hiển thị cho cụm category ( cụm danh mục sản phẩm)
        + Thiết lập style hiển thị cho cụm sản phẩm ( vd: grid, slide, list, ...)
        + Thiết lập popup quảng cáo, vị trí hiện, ...
        + ...
    """,

    'author': "CLOUDMEDIA CO.,LTD",
    'website': "https://cloudmedia.vn/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/banner_view.xml',
        'views/category_product_style_view.xml',
        'views/menus.xml',
        'views/product_public_category_view.xml',
        'views/img_line_views.xml',
        'views/category_product_display_type_view.xml',
        'views/product_template_view.xml',
        'views/popups_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True
}
