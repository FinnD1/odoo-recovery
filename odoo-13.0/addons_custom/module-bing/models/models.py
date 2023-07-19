from odoo import fields, models

class MyModel(models.Model): 
    _name = 'my.model'
    name = fields.Char(string='Name') 
    age = fields.Integer(string='Age')