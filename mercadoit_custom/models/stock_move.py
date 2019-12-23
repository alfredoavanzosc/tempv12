# Copyright 2019 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _


class StockPicking(models.Model):
    _inherit = "stock.move.line"

    imei = fields.Char(string="IMEI", related="lot_id.imei")

