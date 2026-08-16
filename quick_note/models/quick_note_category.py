from odoo import fields, models


class QuickNoteCategory(models.Model):
    _name = "quick.note.category"
    _description = "Quick Note Category"

    name = fields.Char(
        string="Category Name",
        required=True,
    )

    description = fields.Text(
        string="Description",
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )