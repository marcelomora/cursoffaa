# -*- coding: utf-8 -*-
from odoo import http

# class Workout(http.Controller):
#     @http.route('/workout/workout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workout/workout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('workout.listing', {
#             'root': '/workout/workout',
#             'objects': http.request.env['workout.workout'].search([]),
#         })

#     @http.route('/workout/workout/objects/<model("workout.workout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workout.object', {
#             'object': obj
#         })