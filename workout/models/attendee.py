# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class WorkoutAttendee(models.Model):
    _inherit = 'res.partner'

    is_attendee = fields.Boolean(string="Attendee", )
    is_coach = fields.Boolean(string="Coach", )
