from odoo import fields,models

class Wizards(models.Model):
    _name='openacademy.wizards'
    _description=' Wizards !!!'
    
    session_id=fields.Many2one('openacademy.session','Session',requied=True)
    partner_id=fields.Many2many('res.partner',string='Attendees')