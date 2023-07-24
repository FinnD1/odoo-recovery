from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError
from datetime import timedelta


class openacademy_session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session Academy'

    name = fields.Char(string='Session Name', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    duration = fields.Float(string='Duration(days)', help='Duration in days')
    number_of_seats = fields.Integer(String='Number of Seats')

    # Nguoi huong dan
    # instructor_id=fields.Many2one('res.partner',string='Instructor',required=True,domain=[('|','instructor','=',True),('category_id.name','ilike','Teacher')])
    instructor_id = fields.Many2one('res.partner', string='Instructor', required=True)
    course_id = fields.Many2one('openacademy.course', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    active = fields.Boolean(default=True)

    # compute fields(là hàm tính toán đc khai báo = depend)
    taken_seats = fields.Float(string='Taken Seats', compute='_taken_seats')

    # Tính % giữa số ghế và số người tham dự
    @api.depends('number_of_seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.number_of_seats:
                r.taken_seats = 0
            else:
                r.taken_seats = 100 * len(r.attendee_ids) / r.number_of_seats

    # kiểm tra số ghế và số người tham dự(nếu số ghế <0 thì báo lỗi && số ghế < số người tham dự thì báo lỗi)
    @api.onchange('number_of_seats', 'attendee_ids')
    def check_seats(self):
        if (self.number_of_seats < 0):
            return {
                'warning': {
                    'title': 'Incorrect "seats" values',
                    'message': 'The number of seats may not be negative'
                },
            }
        if (self.number_of_seats < len(self.attendee_ids)):
            return {
                'warning': {
                    'title': 'Too many attendee_ids',
                    'message': 'Increase seats or remove excess attendees'
                },
            }

    # kiểm tra người hướng dẫn không được có tên trong danh sách người tham dự
    @api.constrains('instructor_id')
    def _check_instructor_ids(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")

