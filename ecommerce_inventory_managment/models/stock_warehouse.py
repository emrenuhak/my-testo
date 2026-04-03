# -*- coding: utf-8 -*-
# Copyright © 2025 Projet (https://bulutkobi.io)
# Part of BulutKobi License. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_ecommerce_warehouse = fields.Boolean(
        string="Ecommerce Warehouse",
        default=False,
        help="If enabled, products can be sold from this warehouse on the e-commerce website.",
    )
