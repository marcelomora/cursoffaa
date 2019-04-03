# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class WorkoutAttendee(models.Model):
    _inherit = 'res.partner'

    is_attendee = fields.Boolean(string="Attendee", default=lambda r: r.env.context.get('is_attendee', False) )
    is_coach = fields.Boolean(string="Coach", )
