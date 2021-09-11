# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Library(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release asc, name'
    _rec_name = 'short_name'

    name = fields.Char('Title', required=True) #ok
    author_ids = fields.Many2many('res.partner', string='Authors') #ok
    short_name = fields.Char('Short Title', required=True) #ok
    notes = fields.Text('Internal Notes') #ok
    state = fields.Selection(
        [('draft','Not Available'),('available','Available'),('lost','Lost')],'State') #ok
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover') #ok
    out_of_print = fields.Boolean('Out of Print?') #ok
    date_release = fields.Date('Release Date') #ok
    date_updated = fields.Datetime('Last Updated') #ok
    pages = fields.Integer('Number of Pages') #ok
    reader_rating = fields.Float('Reader Average Rating', digits=(14,4)) #ok
    cost_price = fields.Float(
        'Book Cost', digits='Book Prices') #ok
    currency_id = fields.Many2one('res.currency', string='Currency')#ok
    retail_price = fields.Monetary('Retail Price', currency_id='currencey_id') #ok
    publisher_id = fields.Many2one('res.partner', string='Publisher') #ok
    category_id = fields.Many2one('library.book.category') #ok
    age_days = fields.Float(string='Days Since Release',
                            compute='_compute_age',
                            inverse='_inverse_age',
                            search='_search_age') #ok

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)',
         'Book title must be unique.'),
        ('positive_page', 'CHECK (pages>0)',
         'Number of pages must be positive')
    ]

    @api.depends('date_release')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0
    def _inverse_age(self):
        today = fields.Date.today()
        for book in self.filtered('date_release'):
            d = today - timedelta(days=book.age_days)
            book.date_release = d

    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError(
                'Release date must be in the past'
                )

class ResPartner(models.Model):
    _inherit = 'res.partner'

    published_book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')
    authored_book_ids = fields.Many2many('library.book', string='Authored Books')