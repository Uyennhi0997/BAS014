from odoo import models, fields, api


class Popups(models.Model):
    _name = "popups.popups"

    name = fields.Char(string="Tiêu đề", required=True)
    content = fields.Html(string="Nội dung")
    image = fields.Binary(string="Hình ảnh")
