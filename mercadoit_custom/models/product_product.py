# Copyright 2019 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"


    @api.multi
    def name_get(self):
        res = super(ProductProduct, self).name_get()
        res2 = []
        for name_tuple in res:
            product = self.browse(name_tuple[0])
            res2.append((
                name_tuple[0],
                u'{} ({})'.format(name_tuple[1], product.virtual_available)
            ))
        return res2
