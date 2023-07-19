# -*- coding: utf-8 -*-
# from odoo import http


# class Module-bing(http.Controller):
#     @http.route('/module-bing/module-bing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-bing/module-bing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-bing.listing', {
#             'root': '/module-bing/module-bing',
#             'objects': http.request.env['module-bing.module-bing'].search([]),
#         })

#     @http.route('/module-bing/module-bing/objects/<model("module-bing.module-bing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-bing.object', {
#             'object': obj
#         })
