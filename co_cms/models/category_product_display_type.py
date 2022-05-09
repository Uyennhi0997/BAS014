from odoo import models, fields, api


class CategoryProductDisplayType(models.Model):
    _name = "category.product.display.type"
    _description = "Cấu hình dạng hiển thị category và product"

    display_type = fields.Selection([
        ('grid', 'Grid'),
        ('List', 'List'),
        ('Slide', 'Slide'),
    ], default="grid", required=True, string="Dạng hiển thị")
