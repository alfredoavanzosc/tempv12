# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Copyright (c) 2019 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        if self.analytic_account_id and not self.analytic_account_id.group_id:
            aagroup_obj = self.env['account.analytic.group']
            group = aagroup_obj.search([('user_id', '=', self.user_id.id)],
                                       limit=1)
            if group:
                self.analytic_account_id.group_id = group.id
        return res
