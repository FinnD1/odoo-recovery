from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many(comodel_name='crm.customer.request', inverse_name='opportunity_id', string='Request')
    sale = fields.Float(string='Sale', compute='total_sale')
    expected_revenue = fields.Char(string='Revenue', compute='compute_revenue')

    # customer_needs=fields.Char()
    # import_request=fields.Binary()
    # @api.model
    # def

    # @api.model_create_multi
    # def import_requests(self):

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
