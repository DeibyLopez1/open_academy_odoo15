# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
     _name = 'open_academy.course'
     _description = 'Course'

     name = fields.Char(String='Course')
     title = fields.Char(String='Title')
     description = fields.Text(String='Description')