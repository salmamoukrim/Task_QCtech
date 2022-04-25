import string
from odoo import api, fields, models, _


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    source = fields.Many2one('task.city', string='Source')
    destination = fields.Many2one('task.city', string='Destination')
    ride_ids = fields.One2many('picking.ride', 'picking_id')
