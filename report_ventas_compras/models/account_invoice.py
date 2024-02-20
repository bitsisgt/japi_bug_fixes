# -*- encoding: UTF-8 -*-
##############################################################################

from odoo import fields, models, api, _

class AccountInvoice(models.Model):
	_inherit = "account.move"
	
	tax_inovice_old = fields.Selection([
		('True', 'Si'), 
		('False', 'No')],'Impuesto en Factura anterior', help="Si esta activo esta factura es NOTA DE ABONO y saldra como Gravada, dado contrario saldra como Excenta", default="False")
	serie_factura = fields.Char(string="Serie Factura", required=False, help="Serie de la factura de proveedor")
	num_factura = fields.Char(string="Numero Factura", required=False, help="Numero de la factura de proveedor")
	tipo_documento = fields.Selection([
		('FC', 'Factura Cambiaria'),
		('FE', 'Factura Especial'),
		('FCE', 'Factura Electronica'),
                ('FAC', 'Factura'),
                ('FEL', 'FEL'),
		('NC', 'Nota de Credito'),
		('ND', 'Nota de Debito'),
		('FPC', 'Factura Peq. Contribuyente'),
		('DA', 'Declaracion Unica Aduanera'),
		('FA', 'FAUCA'),
		('FO', 'Formulario SAT'),
		('ONAF', 'Otros No Afectos'),
		('EP', 'Escritura Publica')],'Tipo Documento', default='FC', required=True, help="Tipo de documento de gasto que se reflejara en el libro de Ventas/Compras del IVA")

class AccountInvoiceLine(models.Model):
	_inherit = "account.move.line"

	tipo_gasto = fields.Selection([
		('compra', 'Compra/Venta'),
		('servicio', 'Servicios/Honorarios'),
		('combustibles', 'Combustibles/Lubricantes'),
		('importacion', 'Importaciones'),
		('exportacion', 'Exportaciones'), 
		('n/a', 'N/A')],'Tipo Gasto', default="compra", required=False, help="Tipo de gasto que se reflejara en el libro de Ventas/Compras del IVA")

	
	@api.onchange('product_id')
	def onchange_product_gasto(self):
		for record in self:
			if record.product_id and record.product_id.tipo_gasto:
				record.tipo_gasto = record.product_id.tipo_gasto

