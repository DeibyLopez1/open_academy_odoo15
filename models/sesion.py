import string
from odoo import models, fields, api
name = fields.Char(string='Title')
description = fields.Text()


class Session(models.Model):
    _name = 'open_academy.session'

    name = fields.Char(String='Course')
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id=fields.Many2many('res.partner', string="Instuctor")
    course_id=fields.Many2many('open_academy.course', ondelete='cascade', string="course",required=True)
    