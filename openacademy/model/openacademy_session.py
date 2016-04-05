# -*- coding: utf-8 -*-

from openerp import fields, models


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digit=(), help="Duration in days.")
    seats = fields.Integer(string="Number of seats")

