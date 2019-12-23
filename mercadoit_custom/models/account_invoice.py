# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# (c) 2019 Alfredo de la fuente <alfredodelafuente@avanzosc.es> - Avanzosc S.L.
from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    mandate_bank_id = fields.Many2one(
        comodel_name='res.partner.bank', string='Mandate Bank',
        related='mandate_id.partner_bank_id')
