# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class module1(models.Model):
#     _name = 'module1.module1'
#     _description = 'module1.module1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import fields, models

class PLayer (models.Model):
    _name='player'
    _description='Player'
    
    name= fields.Char(string='Name',required=True)
    image=fields.Binary(string='Image',attachment=True)
    country=fields.Char(string='Country')
    gender=fields.Selection(([('male','Male'),('female','Female')]),string="gender",default='male')
    day_of_birth=fields.Datetime(string='Day of birth')
    position =fields.Char('Position')
    height=fields.Float(string='Height')
    Weight=fields.Float(string='Weight')
    