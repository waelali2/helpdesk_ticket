from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError, MissingError, UserError, Warning
from odoo.osv.expression import AND, OR
from odoo.tools import groupby as groupbyelem

from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager

import logging
log = logging.getLogger(__name__)


class TicketPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        # domain = self._get_portal_default_domain()
        tticket_count = http.request.env['helpdesk.ticket'].search_count([('partner_id', '=', request.env.user.partner_id.id)])
        values.update({
            'tticket_count': tticket_count,
        })
        return values

    # def _get_portal_default_domain(self):
    #     my_employee = request.env.user.employee_id
    #     return [
    #         ('employee_id', '!=', my_employee),
    #         # (request.env.user.employee_id.attendance_ids),
    #     ]
        
       