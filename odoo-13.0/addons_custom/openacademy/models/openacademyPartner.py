from odoo import models, fields


class partner_inherit(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor', default=False)
    session_ids = fields.Many2many('openacademy.session', string='Session ID')
