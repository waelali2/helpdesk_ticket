from odoo import http, _
from odoo.http import request
import logging

log = logging.getLogger(__name__)


class Attendances(http.Controller):

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
        return args



      

        
       