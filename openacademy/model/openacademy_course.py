from openerp import models, fields, api


'''
The Following Module holds the means to create Models for Courses Attendance
'''


class Course(models.Model):
    '''
    The Following Clas creates the Basic Model for a Course
    '''
    _name = 'openacademy.course'  # Model Odoo Name

    # Field reserved to identify name rec
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
