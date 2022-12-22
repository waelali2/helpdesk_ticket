from odoo import http, _
from odoo.exceptions import AccessError, MissingError, UserError, Warning
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import Warning
from odoo.http import Response 
import json
from datetime import date, datetime, timedelta, timezone
import logging
import base64

log = logging.getLogger(__name__)


class Tickets(http.Controller):

    @http.route('/my/ticketsss', type='http', auth='user', website=True, sitemap=False)
    def user_ticket_section(self,  **kw):
        partner = request.env.user.partner_id
        ticketa = http.request.env['helpdesk.ticket'].search([('partner_id', '=', request.env.user.partner_id.id)])
        return http.request.render("ticket_portal.tickets_custom", {'tickets': ticketa, 'page_name': 'tickets_list'})
    
    
    @http.route('/delete_ticketss', type='http', auth='user', website=True, sitemap=False)
    def delete_ticketss(self, ticket_id, **kw ):
        ticket = self.env['helpdesk.ticket'].browse(ticket_id)
        ticket.unlink()
        return http.request.render('/my/ticketsss')


    
        
       