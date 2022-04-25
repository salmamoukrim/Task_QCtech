from tokenize import Name

from setuptools import Require
from odoo import api, fields, models,_

class task_city(models.Model):
    _name = "task.city"

    name=fields.Char(string="City Name",required=1)