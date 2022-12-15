from odoo import http, _
from odoo.http import request
import logging

log = logging.getLogger(__name__)


class Ticket(http.Controller):

    @http.route('/get_user', type='json', auth='user')
    def get_user(self):
        user_logged = request.env.user
        test = user_logged.name

        data = {test, user_logged.name}
        return data


    @http.route('/create_ticket', type='json', auth='user')
    def create_ticket(self, **rec):
        if request.jsonrequest:
            print("rec", rec)
            if rec["name"]:
                vals = {
                    'name': rec['name'],
                    'team_id': rec['team_id']
                }
                
                new_ticket = request.env['helpdesk.ticket'].sudo().create(vals)
                args = {
                    'success': True,
                    'ID': new_ticket.id
                }
                email_values = {
                    'recipient_ids': new_ticket.env.user.partner_id,
                    'email_from': new_ticket.env.user.email
                                }
                # mail_template = new_ticket.env.ref('helpdesk.new_ticket_request_email_template')
                mail_template = new_ticket.env.ref('mn_odoo_api_helpdesk.mn_new_template')
                mail_template.send_mail(new_ticket.id, email_values=email_values, force_send=True)
        return args


    @http.route('/web/session/authenticate', type='json', auth="none")
    def authenticate(self, db, login, password, base_location=None):
            request.session.authenticate(db, login, password)
            result = request.env["ir.http"].session_info()
            # avoid to rotate the session outside of the scope of this method
            # to ensure that the session ID does not change after this method
            result["session"] = {
                "sid": request.session.sid,
            }
            return result
        # @http.route('/web/session/authenticate', type='json', auth='user')
        # def authenticate(self, db, login, password, base_location=None):
        #     uid = None
        #     session_info = None
        #     uid = request.session.authenticate(db, login, password)
        #     session_info = request.env['ir.http'].session_info()
        #     return session_info
            
       