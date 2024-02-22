from odoo import models, fields

class modulo(models.Model):
    _name = 'gestion_ciclos_instituto.modulo'
    _description = 'Modulo de un ciclo formativo'
    _rec_name = ''

    nombre = fields.Char(
        string='Modulo',
    )
    