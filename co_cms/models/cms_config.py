from odoo import models, fields, api


# =============Cấu hình banner==============
class BannerConfig(models.Model):
    _name = "banner"
    _description = "Cấu hình banner"

    image = fields.Text(string="Hình ảnh")

    unit = fields.Selection([
        ('px', 'px'),
        ('%', '%'),
        ('cm', 'cm'),
        ('mm', 'mm'),
        ('in', 'in'),
        ('pt', 'pt'),
        ('pc', 'pc'),
        ('em', 'em'),
        ('ex', 'ex'),
        ('ch', 'ch'),
        ('rem', 'rem'),
        ('vw', 'vw'),
        ('vh', 'vh'),
        ('vmin', 'vmin'),
        ('vmax', 'vmax')
    ], default="px", string="Đơn vị")

    width = fields.Float(string="Thiết lập chiều dài banner")
    height = fields.Float(string="Thiết lập chiều cao banner")

    border_height = fields.Float(string="Thiết lập độ dày cho đường viền",
                                 help="Ví dụ: 1.0")
    border_style = fields.Selection([
        ('dotted', 'Dotted'),
        ('dashed', 'Dashed'),
        ('solid', 'Solid'),
        ('double', 'Double'),
        ('groove', 'Groove'),
        ('ridge', 'Ridge'),
        ('inset', 'Inset'),
        ('outset', 'Outset'),
        ('none', 'None'),
        ('hidden', 'Hidden')
    ], default="none", string="Chọn kiểu đường viền")
    border_color = fields.Chart(string="Thiết lập màu cho đường viền",
                                help="Ví dụ: green; Hoặc dùng mã: #00ff00")

    border_radius = fields.Float(string="Thiết lập bo tròn cho đường viền",
                                 help="Ví dụ: 15.0")


# =============Cấu hình dạng hiển thị category và product==============
class CategoryProductDisplayType(models.Model):
    _name = "category.product.display_type"
    _description = "Cấu hình dạng hiển thị category và product"

    display_type = fields.Selection([
        ('grid', 'Grid'),
        ('List', 'List'),
        ('Slide', 'Slide'),
    ], default="Grid", string="Dạng hiển thị")


# =============Cấu hình vị trí hiển thị popups quảng cáo==============
class AdvertisingPopups(models.Model):
    _name = "advertising.popups"
    _description = "Cấu hình vị trí hiển thị popups quảng cáo"

    display_position = fields.Selection([
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('left', 'Left'),
        ('right', 'Right'),
    ], string="Vị trí hiển thị popups quảng cáo")