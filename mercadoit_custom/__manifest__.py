# Copyright (c) 2018 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Mercadoit custom',
    'version': '12.0.1.17.0',
    'depends': [
        'base',
        'sale',
        'sale_analytic',
        'sale_crm',
        'sales_team',
        'stock',
        "web",
        "purchase",
        "account_banking_mandate",
        "account_payment_partner",
        "account_reports",
        "account_invoice_line_lot"
    ],
    'author':  "AvanzOSC",
    'license': "AGPL-3",
    'summary': '''Mercadoit custom''',
    'website': 'http://www.avanzosc.es',
    'data': [
        "security/ir.model.access.csv",
        'views/analytic_view.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        'views/purchase_shipping_method_view.xml',
        'views/purchase_order_view.xml',
        'views/res_partner_take_ous_view.xml',
        'views/res_partner_view.xml',
        'wizard/copy_partner_data_view.xml',
        'report/report_templates.xml',
        'report/sale_order_report.xml',
        'report/purchase_order_report.xml',
        'report/account_invoice_report.xml',
        ],
    'installable': True,
    'auto_install': False,
}
