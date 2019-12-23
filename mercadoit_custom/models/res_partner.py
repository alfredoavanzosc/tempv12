# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Copyright (c) 2019 Alfredo de la Fuente - Avanzosc S.L.
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cards = fields.Binary(string="Image", attachment=True)
    business = fields.Text(string='Businnes', translate=True)
    take_outs_ids = fields.Many2many(
        string='Take outs', comodel_name='res.partner.take.outs',
        relation='rel_partner_take_out', column1='partner_id',
        column2='take_outs_id')


class ResPartnerTakeOus(models.Model):
    _name = 'res.partner.take.outs'
    _description = 'Supplier take outs'

    name = fields.Char(string='Description', required=True)
