# -*- coding: utf-8 -*-
from odoo import fields, models

class Library(models.Model):
    _name = 'library.book'

    name = fields.Char('Title', required=True)
    data_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')