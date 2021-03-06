from odoo import models, fields, api


class CategoryProductStyle(models.Model):
    _name = "category.product.style"
    _description = "Thiết lập style cho danh mục sản phẩm"

    display_styles = fields.Selection([
        ('grid', 'grid'),
        ('list', 'list'),
        ('slide', 'slide'),
    ], default='grid', required=True, string="Dạng hiển thị", help="Dạng hiển thị ở trên website hoặc là ứng dụng")
