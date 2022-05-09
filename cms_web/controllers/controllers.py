# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CmsWeb(http.Controller):
    @http.route('/', auth='public')
    def index(self, **kw):
        Category = http.request.env['product.public.category']
        Cate_style = http.request.env['category.product.style']

        Product_category = http.request.env['product.template']
        Product_style = http.request.env['category.product.display.type']

        print('style = ', Product_style.search([]))

        return http.request.render('cms_web.layout', {
            'category': Category.search([]),
            'cate_style': Cate_style.search([]),
            'product_category': Product_category.search([]),
            'product_style': Product_style.search([]),
        })

    @http.route('/shop', auth='public')
    def Shop(self, **kw):
        # Banner
        Banner = http.request.env['banner.banner']
        position = http.request.env['banner.banner'].sudo().search([('position', '=', '/shop')])
        print('=======================Vi tri:', position)

        # Popups
        Popups = http.request.env['popups.popups']

        if position:
            return http.request.render('cms_web.temp_shop', {
                'banner': Banner.search([('position', '=', '/shop'), ('style', '=', 'banner')]),
                'slide': Banner.search([('position', '=', '/shop'), ('style', '=', 'slide')]),
                'popups': Popups.search([('position', '=', '/shop')])
            })

        else:
            return http.request.render('cms_web.temp_shop')

    @http.route('/about', auth='public')
    def About(self, **kw):
        Banner = http.request.env['banner.banner']
        position = http.request.env['banner.banner'].sudo().search([('position', '=', '/about')])
        print('=======================Vi tri:', position)

        # Popups
        Popups = http.request.env['popups.popups']

        if position:
            return http.request.render('cms_web.temp_about', {
                'banner': Banner.search([('position', '=', '/about')]),
                'popups': Popups.search([('position', '=', '/about')])
            })
        else:
            return http.request.render('cms_web.temp_about')
