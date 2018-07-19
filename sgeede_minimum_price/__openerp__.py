# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'SGEEDE Minimum Price  Module',
	'version': '1.0',
	'category': 'Tools',
	'summary': """Lock and control your minimum sale price to POS, Sales Order and Invoice""",
	'description': """Lock and control your minimum sale price to POS, Sales Order and Invoice""",
	'author': "SGEEDE",
	'website': "http://www.sgeede.com",
	'depends': ['sale'],
	'init_xml': [],
	'data': [
		'views/product_view.xml',
		'views/account_invoice_workflow.xml',
		'views/point_of_sale.xml',
	],
	'qweb': ['static/src/xml/*.xml'],
	'demo_xml': [],
	'installable': True,
	'active': False,
	'certificate': '',
	'price': 9.99,
	'currency': 'EUR',
	'images': [
		'images/main_screenshot.png',
		'images/sgeede.png',	
	],
}