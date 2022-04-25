from logging import raiseExceptions
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class picking_ride(models.Model):
    _name = 'picking.ride'

    sequence = fields.Integer(string='Sequence')
    city_id = fields.Many2one('task.city', string='BL')
    source = fields.Many2one('task.city', string='Source')
    destination = fields.Many2one('task.city', string='Destination')
    date_depart = fields.Datetime('Date de depart')
    date_arrive = fields.Datetime('Date arrive')
    chauffeur_id = fields.Many2one('res.partner')
    picking_id = fields.Many2one('stock.picking')
    etat = fields.Selection([('indefini', 'Indefini'), ('encours', 'En cours'), ('fait', 'Fait')])

    @api.onchange('date_depart', 'date_arrive')
    def date_check(self):
        if self.date_depart > self.date_arrive:
            raise ValueError('invalid date')
