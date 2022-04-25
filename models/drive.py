from odoo import api, fields, models,_

class partner_part(models.Model):

    _inherit='res.partner'

    is_driver=fields.Boolean()