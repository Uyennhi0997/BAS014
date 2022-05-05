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
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True
}
