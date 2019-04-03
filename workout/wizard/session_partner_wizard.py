# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PartnerSession(models.TransientModel):
    _name = 'partner.session'
    _description = 'Partner Workout Session Wizard'

    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_ids'))

    session_wiz_ids = fields.Many2many(
        'workout.session',
        string="Sessions",
        required=True,
    )

    attendee_wiz_ids = fields.Many2many(
        'res.partner',
        string="Attendees",
        required=True,
        default=_default_partner 
    )

    @api.multi
    def subscribe(self):
        for session_wiz_id in self.session_wiz_ids:
            session_wiz_id.attendee_ids |= self.attendee_wiz_ids
        
        return {}