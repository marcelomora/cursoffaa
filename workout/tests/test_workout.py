# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase

class WorkoutTestCase(TransactionCase):
    def setUp(self):
        super(WorkoutTestAttendee, self).setUp()
        print("----------------Set Up --------------------")
        self.demo_user = self.env.ref('base.user_demo')

    def test_10_create_category(self):
        Category = self.env['workout.category'].sudo(self.demo_user)
        category = Category.create(
            {'name': 'Test Category', 
             'type': 'cardio'})
        print("-------------Testing-----------------")
        self.assertEqual(category.name, "Category")
