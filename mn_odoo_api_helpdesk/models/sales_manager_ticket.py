from odoo import api, fields, models, _

import logging

logger = logging.getLogger(__name__)


class sale_managers_ticket(models.Model):
    _inherit = "helpdesk.ticket"

    sale_managers = fields.Many2many('res.users', string="sales managers", compute="_managers")

    def _managers(self):
        for rec in self:
            sales = rec.env.ref('sales_team.group_sale_manager').users
            rec.sale_managers = sales