from odoo import models, fields, api


class Banner(models.Model):
    _name = 'banner.banner'
    _description = 'Danh sách thông tin banner'

    name = fields.Char(string="Tên banner")
    banner_image = fields.Binary(string="Hình ảnh", attachment=True)
    style = fields.Selection([
        ('banner', 'Banner'),
        ('slide', 'Slide')
    ], default='banner', string='Kiểu')
    img_line = fields.One2many(
        'img.line',
        'slide_id',
        string='Danh sách hình ảnh',
        copy=True,
        auto_join=True
    )
