# Copyright (c) 2019 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountAnalyticGroup(models.Model):
    _inherit = 'account.analytic.group'

    user_id = fields.Many2one('res.users', string='Salesperson')
