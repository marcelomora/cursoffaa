# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WorkoutCategory(models.Model):
    _name = 'workout.category'

    name = fields.Char("Name", size=20, required=True)
    type = fields.Selection(
        string='Type',
        selection=[
            ('cardio', 'Cardio'),
            ('muscle', 'Muscle'),
            ('endurance', 'Endurance')],
        required=True)
    