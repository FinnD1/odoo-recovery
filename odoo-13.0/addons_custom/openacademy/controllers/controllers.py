from odoo import http
import json
from odoo.http import request

class OpenAcademy(http.Controller):
    @http.route("/my_course" ,auth="public",website=True)
    def my_template(self,**kw):
        courses= request.env['openacademy.course'].sudo().search([])
        return http.request.render("openacademy.mytemplate",{'courses': courses})
    
    @http.route("/my_course/1",auth='public')
    def my_template_json(self):
        records=request.env['openacademy.course'].sudo().search([])
        data={
            'records':[{
                'title':record.title,
                'description':record.description,
            }for record in records]
        }
        return http.request.make_response(
            json.dumps(data)
        )