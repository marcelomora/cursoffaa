# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)



class WorkoutSession(models.Model):
    _name = 'workout.session'
    _description = 'Session schedule for workout classes'
    _inherit = ['mail.thread']

    @api.multi
    def name_get(self):
        result = []
        for session in self:
            result.append(
                (session.id,
                "[{}, {}]/{}".format(
                    session.category_id.name,
                    session.coach_id.name,
                    session.session_date)))
                
        return result
    # name = fields.Char("Name")

    @api.onchange("session_date")
    def _onchange_field(self):
        vals = {}

        if self.session_date != False:
            self.state = 'closed'
        else:
            self.state = 'draft'
            return vals
    
        # Remove warning if necessary
        if self.session_date < fields.Date.today():
            vals['warning'] = {
                'title': _('Date Warning'),
                'message': _('Date can not be before today')
            }
    
        return vals

    state = fields.Selection(
        string="State",
        selection=[
                ('draft', 'Draft'),
                ('closed', 'Closed'),
                ('done', 'Done'),
                ('cancel', 'Cancel'),
        ],
        default='draft',
    )

    coach_id = fields.Many2one(
        string="Coach",
        comodel_name="res.partner",
        domain="[('is_coach', '=', True)]",
        ondelete="restrict",
        help="Select coach.",
    )

    category_id = fields.Many2one(
        string="Category",
        comodel_name="workout.category",
        ondelete="restrict",
        help="Workout Category",
    )

    attendee_ids = fields.Many2many(
        string="Attendees",
        comodel_name="res.partner",
        relation="workout_sessions_attendees",
        column1="session_id",
        column2="partner_id",
        domain="[('is_attendee', '=', True)]",
        help="List of atendees.",
    )

    session_date = fields.Datetime(string="Date", track_visibility=True )
    taken_seats = fields.Integer(string="Taken Seats", )
    seats = fields.Integer(string="Seats", help="Seats available" )
    attendees_count = fields.Integer(
        string="Attendees Count",
        compute="_get_attendees_count",
        store=True )
    available = fields.Boolean(string="Available", )
    price_per_session = fields.Monetary(string="Price Per Session")
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        ondelete="restrict",
        help="Currency.",
    )

    responsible_id = fields.Many2one(
        string="Responsible User",
        comodel_name="res.users",
        ondelete="restrict",
        help="Responsible User for session.",
        default=lambda r: r.env.user
    )

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for session in self:
            session.attendees_count = len(session.attendee_ids)

    def _track_subtype(self, init_values):
        if 'session_date' in init_values:
            return 'mail.mt_comment'
        return False

