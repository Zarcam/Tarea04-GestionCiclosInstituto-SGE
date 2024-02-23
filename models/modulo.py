from odoo import models, fields

class modulo(models.Model):
    _name = 'gestion_ciclos_instituto.modulo'
    _description = 'Modulo de un ciclo formativo'
    _rec_name = 'modulo'

    modulo = fields.Char(
        string='Modulo',
    )
    
    ciclo_id = fields.Many2one(
        string='Ciclo',
        comodel_name='gestion_ciclos_instituto.modulo',
        ondelete='cascade',
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
    
    
    
    
    