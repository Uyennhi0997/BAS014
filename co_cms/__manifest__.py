# -*- coding: utf-8 -*-
{
    'name': "CMS",

    'summary': """
        + Thiết lập danh sách banner (hình ảnh) hiển thị,\n
        + Thiết lập style của banner ( vd: bo tròng, hiển thị full, hiển thị 90%, viềng vuông, ...)\n
        + Thiết lập style hiển thị cho cụm category ( cụm danh mục sản phẩm)\n
        + Thiết lập style hiển thị cho cụm sản phẩm ( vd: grid, slide, list, ...)\n
        + Thiết lập popup quảng cáo, vị trí hiện, ...\n
        + ...""",

    'description': """
        + Thiết lập danh sách banner (hình ảnh) hiển thị,\n
        + Thiết lập style của banner ( vd: bo tròng, hiển thị full, hiển thị 90%, viềng vuông, ...)\n
        + Thiết lập style hiển thị cho cụm category ( cụm danh mục sản phẩm)\n
        + Thiết lập style hiển thị cho cụm sản phẩm ( vd: grid, slide, list, ...)\n
        + Thiết lập popup quảng cáo, vị trí hiện, ...\n
        + ...
    """,

    'author': "CLOUDMEDIA CO.,LTD",
    'website': "https://cloudmedia.vn/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/banner_view.xml',
        'views/category_product_style_view.xml',
        'views/product_public_category_view.xml',
        'views/img_line_views.xml',
        'views/website_menus_view.xml',
        'views/product_template_view.xml',
        'views/menus.xml',
        'views/popups_view.xml'
    ],
    'application': True
}
