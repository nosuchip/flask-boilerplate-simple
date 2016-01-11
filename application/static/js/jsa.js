this.creaturecast = this.creaturecast || {};

creaturecast.AdminModel = function (config) {
    var self = this;
    var defaultConfig = {
        productsUrl: '',
        dateFormat: 'YYYY-MM-DD'
    };
    var _config = $.extend({}, defaultConfig, config);

    function onLicenseChanged(e) {
        setPageLoading(true);

        $.ajax({
            url: _config.productsUrl,
            data: {product_license_type_id: $(e.currentTarget).val()},
            type: 'GET'
        })
        .done(function(response) {
            if (!response || !response.data || !response.data.product_license_type) {
                flash('Cannot find corresponding product', 'danger');
                return;
            }

            var data = response.data;

            var expiration_date = data.product_license_type.expiration
                ? moment(new Date()).add(data.product_license_type.expiration, 'days').format(_config.dateFormat)
                : '';
            $('input#expiration_date').val(expiration_date);
            $('input#amount').val(data.product_license_type.price);
        })
        .fail(function() {
            flash('Cannot find corresponding product', 'danger');
        })
        .always(function() {
            setPageLoading(false);
        })
    }

    self.init = function() {
        //License type
        $('#license_type').select2().on("change", onLicenseChanged);
        $('#license_type').select2().trigger('change');
    }

    self.init();
}
