from odoo import models
from odoo.tools import slugify as slug

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _get_website_url(self):
        """Genera una URL de producto sin ID numérico y con /catalogo en lugar de /shop"""
        self.ensure_one()
        return "/catalogo/%s" % (slug(self))

class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    def _get_website_url(self):
        """Genera una URL de categoría sin ID numérico y con /catalogo/categoria en lugar de /shop/category"""
        self.ensure_one()
        return "/catalogo/categoria/%s" % (slug(self))
