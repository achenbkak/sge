from odoo import models, fields # type: ignore

class Equipo(models.Model):
    _name = "bytemadrid.equipo"
    _description = "Equipo informático"

    name = fields.Char(
        string="Nombre del equipo",
        required=True
    )

    fabricante = fields.Char(
        string="Nombre del fabricante",
        required = True
    )

    modelo = fields.Char(
            string="Nombre del modelo",
        )

    num_serie = fields.Char(
            string="Número de serie",
        )

    precio = fields.Float(
            string="Precio",
        )

    estado = fields.Boolean(
            string="Activo",
            default=True
        )

