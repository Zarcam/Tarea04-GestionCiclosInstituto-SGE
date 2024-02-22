from odoo import models, fields

class ciclo(models.Model):
    _name = 'gestion_ciclos_instituto.ciclo'
    _description = 'Ciclo formativo'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Ciclo'
    )

    modulo_ids = fields.One2many(
        string='Modulo',
        comodel_name='gestion_ciclos_instituto',
        inverse_name='ciclo_id',
    )
    
    