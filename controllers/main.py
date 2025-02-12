from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class CustomWebsiteSale(WebsiteSale):

    @http.route(['/catalogo', '/catalogo/page/<int:page>'], type='http', auth='public', website=True, sitemap=True)
    def shop(self, page=0, category=None, search='', **post):
        """Sobreescribe la tienda para que use /catalogo en lugar de /shop"""
        return super(CustomWebsiteSale, self).shop(page=page, category=category, search=search, **post)

    @http.route(['/catalogo/categoria/<model("product.public.category"):category>'], type='http', auth='public', website=True, sitemap=True)
    def product_category(self, category, search='', **kwargs):
        """Sobreescribe las categorías para que usen /catalogo/categoria/ en lugar de /shop/category/"""
        return super(CustomWebsiteSale, self).product_category(category, search=search, **kwargs)