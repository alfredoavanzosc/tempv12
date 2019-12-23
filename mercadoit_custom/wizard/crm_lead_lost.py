# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# (c) 2019 Alfredo de la fuente <alfredodelafuente@avanzosc.es> - Avanzosc S.L.
from odoo import models, api


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    @api.multi
    def action_lost_reason_apply(self):
        result = super(CrmLeadLost, self).action_lost_reason_apply()
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        for lead in leads:
            cond = [('opportunity_id', '=', lead.id)]
            sales = self.env['sale.order'].search(cond)
            sales.action_cancel()
        return result
