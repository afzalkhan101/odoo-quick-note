from odoo import fields, models


class QuickNote(models.Model):
    _name = "quick.note"
    _description = "Quick Note"
    _order = "create_date desc"

    

    name = fields.Char(
        string="Title",
        required=True,
    )

    description = fields.Text(
        string="Description",
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        ondelete="cascade",
    )

    category_id = fields.Many2one(
        "quick.note.category",
        string="Category",
    )

    priority = fields.Selection(
        [
            ("0", "Normal"),
            ("1", "Important"),
            ("2", "Urgent"),
        ],
        string="Priority",
        default="0",
    )

    user_id = fields.Many2one(
        "res.users",
        string="Assigned To",
        default=lambda self: self.env.user,
    )

    note_date = fields.Datetime(
            string="Note Date & Time",
            default=fields.Datetime.now,
    )

    active = fields.Boolean(
        default=True,
    )