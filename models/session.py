from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'training.session'
    _description = 'Description'

    name = fields.Char()
