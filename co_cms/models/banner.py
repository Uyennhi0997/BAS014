from odoo import models, fields, api


class Banner(models.Model):
    _name = 'banner.banner'

    name = fields.Char(string="Tên", required=True)
    banner_image = fields.Binary(string="Hình ảnh", attachment=True)
    position = fields.Many2many('website.menus', string='Vị trí hiển thị')
    style = fields.Selection([
        ('banner', 'Banner'),
        ('slide', 'Slide')
    ], default='banner', string='Kiểu')
    img_line = fields.Many2many('img.line', string='Danh sách hình ảnh', copy=True, auto_join=True)
