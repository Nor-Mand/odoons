# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import  fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _compute_sale_data_total_amount(self,data):
        res = super(CrmLead,self)._compute_sale_data(data)
        for lead in self:
            total = 0.0
            quotation_cnt = 0
            sale_order_cnt = 0
            company_currency = lead.company_currency or self.env.company.currency_id
            for order in lead.order_ids:
                if order.state in ('draft', 'sent'):
                    quotation_cnt += 1
                if order.state not in ('draft', 'sent', 'cancel'):
                    sale_order_cnt += 1
                    total += order.currency_id._convert(
                        order.amount_total, company_currency, order.company_id, order.date_order or fields.Date.today())
            lead.sale_amount_total = total
            lead.quotation_count = quotation_cnt
            lead.sale_order_count = sale_order_cnt

        return res

