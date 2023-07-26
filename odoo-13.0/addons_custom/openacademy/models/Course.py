from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy'

    title = fields.Char(required=True)
    description = fields.Text()

    # sql constrain(rang buoc sql)
    _sql_constraints = [
        ('title_description_check',
         'CHECK(title != description)',
         "The title of the course should not be the description"),

        ('title_unique',
         'UNIQUE(title)',
         "The course must be UNIQUE")
    ]

    # Người chịu trahc nhiem
    responsible_id = fields.Many2one('res.users', string='Responsible', required=True)
    session_id = fields.One2many(comodel_name='openacademy.session', inverse_name='course_id', string='Session')

    # @api.onchange('description')
    # def action_url(self):
    #     return{
    #         'type':'ir.actions.act_url',
    #         'target':'new',
    #         'url':'https://www.facebook.com/',
    #     }
    def action(self):
        # odoo search method
        for rec in self:
            course1 = self.env['openacademy.course'].search([])
            print('course:.....', course1)
            # course_responsible = self.env['openacademy.course'].search(['title', '=', 'Flutter'])
            # print('responsible_willis:....', course_responsible)
            # famale=self.env['hospital.patient'].seacrh(['|',('gender','=','female'),('patient_age','>=',30)])

            # odoo search count
            course1 = self.env['openacademy.course'].search_count([])
            print('course:.....', course1)

            # odoo brower
            brower_course = self.env['openacademy.course'].browse(4)
            print('brower_course:.....', brower_course)
            if brower_course.exists():
                print('co r nha')
            else:
                print('cook')

    def create1(self):
        for rec in self:
            create_record = self.env['openacademy.course'].create({'title': 'course test create 1'})
            print('tao moi thanh cong nha :D.....', create_record)

    def write1(self):
        record_update = self.env['openacademy.course'].browse(8)
        if record_update.exists():
            record_update.write({'description': 'course test  bla bla'})
# //tai sao khi minh cham cac truong den many2one thi minh dc
# thu nhat la tai saomany2one lai luu o daatabase la interger
# tai sao one2many lai co inverse name
