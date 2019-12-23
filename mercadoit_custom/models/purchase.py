# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# (c) 2019 Alfredo de la fuente <alfredodelafuente@avanzosc.es> - Avanzosc S.L.
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def _compute_print_taxes(self):
        for purchase in self:
            partner = purchase.partner_id
            if (not partner.property_account_position_id or
                    'Extra' in partner.property_account_position_id.name):
                purchase.print_taxes = False
            else:
                purchase.print_taxes = True

    print_taxes = fields.Boolean(
        string='Print taxes', compute='_compute_print_taxes')
    purchase_shipping_method = fields.Many2one(
        string='Shipping method', comodel_name='purchase.shipping.method')


class PurchaseShippingMethod(models.Model):
    _name = 'purchase.shipping.method'
    _description='Purchase shiping method'

    name = fields.Char(string='Description', required=True)
