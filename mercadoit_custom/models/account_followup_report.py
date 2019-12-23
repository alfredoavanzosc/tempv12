# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# (c) 2019 Alfredo de la fuente <alfredodelafuente@avanzosc.es> - Avanzosc S.L.
from odoo import models, _


class AccountFollowupReport(models.AbstractModel):
    _inherit = 'account.followup.report'

    def _get_columns_name(self, options):
        result = super(AccountFollowupReport, self)._get_columns_name(options)
        result.insert(1, {'name': _('Invoice'),
                          'style': 'text-align:center; white-space:nowrap;'})
        return result

    def _get_lines(self, options, line_id=None):
        res = super(AccountFollowupReport, self)._get_lines(options,
                                                            line_id=line_id)
        for lin in res:
            if lin.get('invoice_id', False):
                inv = self.env['account.invoice'].browse(lin.get('invoice_id'))
                lin['columns'].insert(0, {'name': inv.number})
        return res
