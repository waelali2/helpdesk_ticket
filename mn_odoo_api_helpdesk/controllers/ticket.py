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


    # @http.route('/create_ticket', type='json', auth='user')
    # def create_ticket(self, **rec):
    #     if request.jsonrequest:
    #         print("rec", rec)
    #         if rec["name"]:
    #             vals = {
    #                 'name': rec['name'],
    #                 'team_id': rec['team_id']
    #             }
                
    #             new_ticket = request.env['helpdesk.ticket'].sudo().create(vals)
    #             args = {
    #                 'success': True,
    #                 'ID': new_ticket.id,
    #                 'sale_managers' :
    #             }
               
    #             # mail_template = new_ticket.env.ref('helpdesk.new_ticket_request_email_template')
    #             mail_template = new_ticket.env.ref('mn_odoo_api_helpdesk.mn_new_template')
    #             mail_template.send_mail(new_ticket.id, force_send=True)
    #     return args


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


    
    @http.route('/create_ticket', type='json', auth='user')
    def create_ticket(self, **rec):

        if request.jsonrequest:
            sales_managers = []
        
            vals = {
                'name': rec['name'],
                'team_id': rec['team_id']
            }
                
            new_ticket = request.env['helpdesk.ticket'].sudo().create(vals)
            sales_team = request.env.ref('sales_team.group_sale_manager').users
            
            for user in sales_team.ids:
                teams = request.env['res.users'].sudo().search([('id','=',user)])
                for team in teams:
                    managers = {
                        "id":team.id,
                        "name":team.name
                    }
                    sales_managers.append(managers)
                    email_values = {
                    'email_to': team.email,
                    'email_cc': False,
                    'auto_delete': True,
                    'recipient_ids': [],
                    'partner_ids': [],
                    'scheduled_date': False,
                    }
                new_ticket.env.ref('helpdesk.new_ticket_request_email_template')
                mail_template = new_ticket.env.ref('mn_odoo_api_helpdesk.mn_new_template')
                mail_template.send_mail(new_ticket.id, force_send=True, email_values=email_values)

            args = {
                'success': True,
                'ID': new_ticket.id,
                'sale_managers' : sales_managers
            }
        
            return args