# -*- coding: utf-8 -*-

from openerp import models, fields


'''
The Following Module holds the means to create Models for Courses Attendance
'''


class Course(models.Model):
    '''
    The Following Class creates the Basic Model for a Course
    '''
    _name = 'openacademy.course'  # Model Odoo Name

    # Field reserved to identify name rec
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    responsible_id = fields.Many2one('res.users', ondelete='set null',
                                        string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session',
                                    'course_id', string="Sessions")
