# -*- encoding: UTF-8 -*-
##############################################################################

{
	'name': 'Reporte de Ventas y Compras',
	'summary': """Reporte de Ventas y Compras""",
	'version': '1.0.',
	'description': """Permite Generar Reporte de Ventas y Compras de IVA""",
	'author': 'Anonimo',
	'maintainer': 'Palo Blanco',
	'website': '',
	'category': 'account',
	'depends': ['account', 'account_reports'],
	'license': 'AGPL-3',
	'data': [
		'security/ir.model.access.csv',
		'data/paperformat_data.xml',
		'views/product_template_view.xml',
		'views/account_invocie_view.xml',
		#'views/views.xml',
		'wizard/wizard_ventas_compras_view.xml',
		'views/ab_reports.xml',
		'views/report_purchase_book_template.xml',
		'views/report_sale_book_template.xml',
	],
	'assets': {
		'web.assets_backend': [
        	'report_ventas_compras/static/src/css/invoice.css'
    	],
	},
	'demo': [],
	'installable': True,
	'auto_install': False,
}
