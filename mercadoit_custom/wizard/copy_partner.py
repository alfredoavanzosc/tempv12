# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# (c) 2019 Alfredo de la fuente <alfredodelafuente@avanzosc.es> - Avanzosc S.L.

from openerp import models, fields, api


class PartnerDataCopy(models.TransientModel):
    _name = 'partner.data.copy'
    _description = 'Copy Partner to company'

    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', required=True)

    @api.multi
    def copy_partner_data(self):
        partner_obj = self.env['res.partner']
        new_partner_lst = []
        for partner_id in self.env.context['active_ids']:
            contacts = partner_obj.search([('parent_id', '=', partner_id)])
            partner2copy = partner_obj.browse(partner_id)
            default = {'name': partner2copy.name,
                       'company_id': self.company_id.id}
            new_partner = partner2copy.copy(default)
            new_partner_lst.append(new_partner.id)
            for contact in contacts:
                contact_def = {'parent_id': new_partner.id,
                               'company_id': self.company_id.id,
                               'name': contact.name,
                               }
                contact.copy(contact_def)
        wizard = {
            'type': 'ir.actions.act_window',
            'name': 'View new partners',
            'res_model': 'res.partner',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': new_partner.id,
            }
        if len(new_partner_lst) > 1:
            del wizard['res_id']
            wizard.update(
                {'view_type': 'form',
                 'view_mode': 'tree,form',
                 'domain': "[('id','in',{})]".format(new_partner_lst),
                 'view_id': False,
                 'target': 'current'
                 })
        return wizard
