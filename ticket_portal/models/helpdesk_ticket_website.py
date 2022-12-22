from odoo import api, models, exceptions

import logging

logger = logging.getLogger(__name__)


class helpdesk_ticket_website(models.Model):
    _inherit = "helpdesk.ticket"

    def delete_ticket(self):
        print('hiiiiiiiiiiiiiiiiiiii')
        #Check if the user has the necessary permissions
        if not self.env.user.has_group('helpdesk.group_helpdesk_manager'):
            raise exceptions.AccessError("You do not have the necessary permissions to delete this ticket.")

        # Unlink the ticket
        self.unlink()   