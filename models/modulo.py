from odoo import models, fields

class modulo(models.Model):
    _name = 'gestion_ciclos_instituto.modulo'
    _description = 'Modulo de un ciclo formativo'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Modulo',
    )

    alumno_ids = fields.Many2many(
        string='Alumnos',
        comodel_name='gestion_ciclo_instituto.alumno',
    )
    
    profesor_id = fields.Many2one(
        string='Profesor',
        comodel_name='gestion_ciclos_instituto.profesor',
        ondelete='restrict',
    )
    
    
    
    
    