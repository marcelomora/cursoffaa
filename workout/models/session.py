# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class WorkoutSession(models.Model):
    _name = 'workout.session'
    _description = 'Session schedule for workout classes'

    name = fields.Char("Name")
    coach_id = fields.Many2one(
        string="Coach",
        comodel_name="res.partner",
        domain="[('is_coach', '=', True)]",
        ondelete="restrict",
        help="Select coach.",
    )

    attendee_ids = fields.Many2many(
        string="Attendees",
        comodel_name="res.partner",
        relation="workout_sessions_attendees",
        column1="session_id",
        column2="partner_id",
        # domain="[('field', '=', other)]",
        help="List of atendees.",
    )

    session_date = fields.Datetime(string="Date", )
    taken_seats = fields.Integer(string="Taken Seats", )
    seats = fields.Integer(string="Seats", help="Seats available" )
    attendees_count = fields.Integer(string="Attendees Count", )
    available = fields.Boolean(string="Available", )
    price_per_session = fields.Monetary(string="Price Per Session")
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        ondelete="restrict",
        help="Currency.",
    )