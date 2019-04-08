# -*- encoding: utf-8 -*-

from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)

class WorkoutAttendee(models.Model):
    _inherit = 'res.partner'

    is_attendee = fields.Boolean(string="Attendee", default=lambda r: r.env.context.get('is_attendee', False) )
    is_coach = fields.Boolean(string="Coach", )


    @api.multi
    def partners_by_country(self):
        sql = """SELECT country_id, array_agg(id)
               FROM res_partner
               WHERE active=true AND country_id IS NOT NULL
               GROUP BY country_id
               """

        self.env.cr.execute(sql)

        Country = self.env['res.country']
        result = {}

        for country_id, partner_ids in self.env.cr.fetchall():
            country = Country.browse(country_id)
            partners = self.search(
                [('id', 'in', tuple(partner_ids))]
            )
            result[country.id] = [partner.id for partner in partners]
        _logger.info(result)
        return result
