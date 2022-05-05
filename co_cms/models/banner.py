from odoo import models, fields, api


class Banner(models.Model):
	_name = 'banner.banner'
	_description = 'Danh sách thông tin banner'

	name = fields.Char('Tên banner')
	banner_image = fields.Binary(string='Hình ảnh :', attachment=True)
