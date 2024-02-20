# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _
from odoo.addons.num_to_words.models.numero_letras import numero_a_letras, numero_a_moneda

class AccountInvoice(models.Model):
    _inherit = "account.move"

    text_amount = fields.Char(string="Monto en letras", required=False, compute="amount_to_words" )
    text_amount_fe = fields.Char(string="Monto en letras_", required=False, compute="amount_to_words_fe")

    @api.depends('amount_total')
    def amount_to_words(self):
        for record in self:
            record.text_amount = numero_a_moneda(record.amount_total)

    @api.depends('amount_total')
    def amount_to_words_fe(self):
        total = 0
        for data in self.invoice_line_ids:
            total += data.price_subtotal + data.no_fe_taxes
        self.text_amount_fe = numero_a_moneda(total)