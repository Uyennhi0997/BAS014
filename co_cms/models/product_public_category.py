from odoo import fields, models, api


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'
    _description = 'Thiết lập style hiển thị cho cụm danh mục'