# -*- coding: utf-8 -*-
{
    'name': "Workout Manager",

    'summary': """
        Workout sessions manager. Modulo de gestion de entrenamientos.
        """,

    'description': """
        Workout sessions manager.
        - Manage classes for gym attendes
        --------------------------------------
        - Administracion de clases de entrenamiento
    """,

    'author': "Accioma",
    'website': "http://www.accioma.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sports and recreation',
    'version': '11.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/workout_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner_view.xml',
        'views/session_view.xml',
        'data/categories.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}