# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
     _name = 'open_academy.course'
     _description = 'Course'

     name = fields.Char(String='Course')
     title = fields.Char(String='Title')
     description = fields.Text(String='Description')

@api.model
def _name_description_search(self, name='',description='', args=None, operator='ilike', limit=100, 
name_get_uid=None, description_get_uid=None):
 return self._search(args, limit=limit, access_rights_uid=name_get_uid,access_rights_uid=description_get_uid)