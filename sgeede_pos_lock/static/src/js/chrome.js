odoo.define('sgeede_pos_lock.chrome', ['point_of_sale.chrome', 'point_of_sale.BaseWidget'], 
    function (require) {
"use strict";

    var PosBaseWidget = require('point_of_sale.BaseWidget');
    var chrome = require('point_of_sale.chrome');

    var LockScreenWidget = PosBaseWidget.extend({
        template: "LockScreenWidget",
        init: function(parent, options) {
            this._super(parent, options);
        }, 
        start: function(){
            var self = this;
            this.$el.click(function() {
                self.gui.show_popup('lockscreen');
            });
        }
    });

    chrome.Chrome.prototype.widgets.unshift({
        'name': 'lockscreen_btn',
        'widget': LockScreenWidget,
        'append': '.pos-rightheader'
    })
});