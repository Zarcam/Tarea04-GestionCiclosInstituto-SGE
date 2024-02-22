from odoo import models, fields

class alumno(models.Model):
    _name = 'gestion_ciclos_instituto.alumno'
    _description = 'Alumno matriculado en el instituto'
    _rec_name = ''
    
    nombre = fields.Char(
        string='Nombre',
    )

    apellidos = fields.Char(
        string='Apellidos',
    )

    dni = fields.Char(
        string='DNI',
    )
    
    

    