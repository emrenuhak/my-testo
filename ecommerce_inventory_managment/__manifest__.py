# -*- coding: utf-8 -*-
# Copyright © 2025 Projet (https://bulutkobi.io)
# Part of BulutKobi License. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ecommerce: Inventory Management',
    'website': 'https://bulutkobi.io',
    'version': '1.0',
    'category': 'Website',
    'license': 'LGPL-3',
    'author': 'Projet',
    'depends': ['stock', 'website_sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_warehouse_views.xml',
        'views/product_template_views.xml',
    ],
}
