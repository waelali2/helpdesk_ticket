odoo.define('ticket_portal.tickets_custom', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    var _t = core._t;

    publicWidget.registry.MyPage = publicWidget.Widget.extend({
        selector: 'tickets_custom',

        // Handle the click event of the delete button
        events: {
            'click .btn-delete': '_onClickDelete',
        },

        // Call the delete_ticket method
        _onClickDelete: function (e) {
            var self = this;
            var ticketId = $(e.currentTarget).data('id');
            ajax.jsonRpc('/web/dataset/call_kw', 'call', {
                model: 'helpdesk.ticket',
                method: 'delete_ticket',
                args: [ticketId],
                kwargs: {},
            }).then(function () {
                // Show a success message
                self.displayNotification({
                    type: 'success',
                    message: _t('Ticket deleted successfully'),
                });
                // Refresh the page
                window.location.reload();
            }).fail(function (error, event) {
                event.preventDefault();
                // Show an error message
                self.displayNotification({
                    type: 'error',
                    message: _t('Error: Could not delete ticket'),
                });
            });
        },
    });

    return publicWidget.registry.MyPage;
});