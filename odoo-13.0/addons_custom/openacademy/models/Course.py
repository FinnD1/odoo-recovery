from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy'

    title = fields.Char(required=True)
    description = fields.Text()
    
    #sql constrain(rang buoc sql)
    _sql_constraints=[
        ('title_description_check',
         'CHECK(title != description)',
         "The title of the course should not be the description"),
        
        ('title_unique',
         'UNIQUE(title)',
         "The course must be UNIQUE")
    ]
    
    # Người chịu trahc nhiem
    responsible_id=fields.Many2one('res.users',string='Responsible',required=True)
    session_id=fields.One2many('openacademy.session','course_id',string='Session')
    
    # @api.onchange('description')
    # def action_url(self):
    #     return{
    #         'type':'ir.actions.act_url',
    #         'target':'new',
    #         'url':'https://www.facebook.com/',
    #     }