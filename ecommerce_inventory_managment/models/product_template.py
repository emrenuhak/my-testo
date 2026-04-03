# -*- coding: utf-8 -*-
# Copyright © 2025 Projet (https://bulutkobi.io)
# Part of BulutKobi License. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ecommerce_warehouse_ids = fields.Many2many(
        comodel_name='stock.warehouse',
        relation='product_template_ecommerce_warehouse_rel',
        column1='product_tmpl_id',
        column2='warehouse_id',
        string="Ecommerce Warehouses",
        domain="[('is_ecommerce_warehouse', '=', True)]",
        help="Select the warehouses from which this product can be sold on the e-commerce website.",
    )
    ecommerce_stock_qty = fields.Float(
        string="Ecommerce Available Qty",
        compute='_compute_ecommerce_stock_qty',
        help="Total free quantity available for e-commerce sale across selected warehouses.",
    )

    @api.depends('ecommerce_warehouse_ids')
    def _compute_ecommerce_stock_qty(self):
        for template in self:
            total_free_qty = 0.0
            if template.ecommerce_warehouse_ids:
                for product in template.product_variant_ids:
                    for warehouse in template.ecommerce_warehouse_ids:
                        total_free_qty += product.with_context(
                            warehouse=warehouse.id
                        ).free_qty
            template.ecommerce_stock_qty = total_free_qty

    #TODO:this function is override from website_sale_stock, so we need to check it's logic
    def _get_combination_info(
        self,
        combination=False,
        product_id=False,
        add_qty=1,
        pricelist=False,
        parent_combination=False,
        only_template=False,
    ):
        combination_info = super()._get_combination_info(
            combination=combination,
            product_id=product_id,
            add_qty=add_qty,
            pricelist=pricelist,
            parent_combination=parent_combination,
            only_template=only_template,
        )

        if not self.env.context.get('website_sale_stock_get_quantity'):
            return combination_info

        if combination_info['product_id']:
            product = self.env['product.product'].sudo().browse(
                combination_info['product_id']
            )
            template = product.product_tmpl_id
            if template.ecommerce_warehouse_ids:
                total_free_qty = 0.0
                for warehouse in template.ecommerce_warehouse_ids:
                    total_free_qty += product.with_context(
                        warehouse=warehouse.id
                    ).free_qty
                combination_info['free_qty'] = total_free_qty

        return combination_info
