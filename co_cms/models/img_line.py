from odoo import fields, api, models


class ImgLine(models.Model):
    _name = 'img.line'

    name = fields.Char(
        string='Tên hình ảnh',
    )
    # slide_id = fields.Many2one(
    #     'banner.banner',
    #     string='Slide', required=True, ondelete='cascade', index=True, copy=False
    # )

    image = fields.Binary(
        string='Hình ảnh',
        attachment=True,
    )
