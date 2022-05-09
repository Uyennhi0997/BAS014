from odoo import fields, models, api, _


class WebsiteMenus(models.Model):
    _name = 'website.menus'
    _parent_store = True
    _order = "sequence, name, id"
    # _description = 'Description'

    def _default_sequence(self):
        cat = self.search([], limit=1, order="sequence DESC")
        if cat:
            return cat.sequence + 5
        return 10000

    name = fields.Char(string='Tên', required=True, translate=True)
    parent_id = fields.Many2one('website.menus', string='Menu cha', index=True, ondelete="cascade")
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('website.menus', 'parent_id', string='Menu con')
    parents_and_self = fields.Many2many('website.menus', compute='_compute_parents_and_self')
    sequence = fields.Integer(help="Cung cấp thứ tự trình tự khi hiển thị danh sách các menu trong website", index=True, default=_default_sequence)
    # website_description = fields.Html('Category Description', sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    # product_tmpl_ids = fields.Many2many('product.template', relation='product_public_category_product_template_rel')

    @api.constrains('parent_id')
    def check_parent_id(self):
        if not self._check_recursion():
            raise ValueError(_('Error ! You cannot create recursive menu.'))

    def name_get(self):
        res = []
        for category in self:
            res.append((category.id, " / ".join(category.parents_and_self.mapped('name'))))
        return res

    def _compute_parents_and_self(self):
        for category in self:
            if category.parent_path:
                category.parents_and_self = self.env['website.menus'].browse([int(p) for p in category.parent_path.split('/')[:-1]])
            else:
                category.parents_and_self = category

