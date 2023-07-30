from odoo import http
import json
from odoo.http import request


class CRM_Lead(http.Controller):

    @http.route(route='/crm/lead', auth='public', methods=['POST'], type='json', website='True')
    def create_lead(self):
        data = json.load(request.httprequest.data)
        self.env['crm.lead'].create({
            
        })
        return "Create Lead Successful"
