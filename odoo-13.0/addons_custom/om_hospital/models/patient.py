from odoo import fields,models


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Hospital Patient"
    
    name=fields.Char(string='name' ,required=True)
    age=fields.Char(string='Age')
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ],required=True ,default='male')
    note=fields.Text
    
    