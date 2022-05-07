from odoo import fields, api, models


class ImgLine(models.Model):
    _name = 'img.line'

    name = fields.Char(string='Tên hình ảnh')
    image = fields.Binary(string='Hình ảnh', attachment=True)
