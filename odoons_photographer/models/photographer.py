# -*- coding: utf-8 -*-
from odoo import fields, models

class Photographer(models.Model):
    _name = 'photographer'
    _description = 'Module for Photographers'

    name = fields.Many2many('res.partner', string = 'Client')