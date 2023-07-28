import base64

import xlrd

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many(comodel_name='crm.customer.request', inverse_name='opportunity_id', string='Request')
    sale = fields.Float(string='Sale', compute='total_sale')
    expected_revenue = fields.Char(string='Revenue', compute='compute_revenue')

    # customer_needs=fields.Char()
    import_request = fields.Binary()

    @api.depends('request_ids.qty')
    def total_sale(self):
        for rec in self:
            total_qty = 0
            for record in rec.request_ids:
                total_qty += record.qty
            rec.sale = total_qty

    @api.depends('request_ids.product_id')
    def compute_revenue(self):
        for rec in self:
            total_revenue = 0
            for record in rec.request_ids:
                total_revenue += record.qty * record.product_id.list_price
            rec.expected_revenue = total_revenue

    def import_file(self):
        # Decode file
        file_data = base64.b64decode(self.file)

        # Parse Excel file
        workbook = xlrd.open_workbook(file_contents=file_data)
        worksheet = workbook.sheet_by_index(0)

        # Lặp qua các dòng dữ liệu
        for row_num in range(worksheet.nrows):
            # Lấy dữ liệu từng cột theo row
            vals = {}
            row = worksheet.row()

            if row[0].value:
                vals['product_id'] = row[0].value
                vals['opportunity_id'] = row[1].value
                vals['date'] = row[2].value
                vals['description'] = row[3].value
                vals['qty'] = row[4].value

            # Tạo record mới trong Odoo
            self.env['crm.customer.request'].create({
                'product_id': vals['product_id'],
                'opportunity_id': vals['opportunity_id'],
                'date': vals['date'],
                'description': vals['description'],
                'qty': vals['qty'],

            })
