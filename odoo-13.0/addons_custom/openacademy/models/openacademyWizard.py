from odoo import models, fields, api


class openWizard(models.TransientModel):
    _name = 'openacademy.wizard'

    session_ids = fields.Many2many('openacademy.session')
    # , default="self._context.get('session_ids')"
    # chưa làm được wizard
    attendee_ids = fields.Many2many('res.partner', string='Attendee')

    @api.model_create_multi
    def open_wizard(self):
        return {
            'name': 'Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'openacademy.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'session_id': self.id}
        }
