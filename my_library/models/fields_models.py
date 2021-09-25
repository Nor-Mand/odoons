# -*- coding: utf-8 -*-
from odoo import fields,models,api
from datetime import date, datetime

class FieldsModels(models.Model):
    _name = 'fields.models'
    _description = 'Fields Models'

    type_char = fields.Char('Type Char')
    type_text = fields.Text('Type Text')
    type_select = fields.Selection([('1','Draft'),('2','Available'),('3','Unvailable')], string='Type Select')
    type_html = fields.Html('Type Html')
    type_binary = fields.Binary('Type Binary')
    type_boolean = fields.Boolean('Type Boolean')
    type_date = fields.Date('Type Date', default=date.today())
    type_datetime = fields.Datetime('Type Datatime', default=datetime.now())
    type_integer = fields.Integer('Type Integer')
    type_float = fields.Float('Type Float')