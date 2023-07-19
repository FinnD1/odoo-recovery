# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class module-bing(models.Model):
#     _name = 'module-bing.module-bing'
#     _description = 'module-bing.module-bing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
