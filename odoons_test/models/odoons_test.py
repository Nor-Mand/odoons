# -*- coding: utf-8 -*-
from odoo import fields, models

class OdoonsTest(models.Model):
    _name = 'odoons.test'
    _description = 'Module for Testing'

    name = fields.Char('Nombre del producto',)