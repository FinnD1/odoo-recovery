import xlrd

from odoo import models, api, fields
import base64
from odoo.modules.module import get_resource_path
from xlrd import open_workbook
from openerp.addons.data_im import FakeModel


class DataImport(models.TransientModel):
    _name = 'import.wizard'

    file = fields.Binary(string='Excel File')
    file_name = fields.Char()

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
            row = worksheet.row(row_no)

            if row[0].value:
                vals['name'] = row[0].value

            # Tạo record mới trong Odoo
            self.env['model_name'].create({
                'field_1': value_1,
                'field_2': value_2
            })
