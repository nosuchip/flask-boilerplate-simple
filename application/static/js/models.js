this.app = this.app || {};

app.PageLoader = function() {
    var self = this;

    self.loadingCount = 0;

    self.loading = function(loading) {
        if (loading) {
           self.loadingCount++;
        } else {
            self.loadingCount--;

            if (self.loadingCount < 0) {
                self.loadingCount = 0;
            }
        }

        ((self.loadingCount > 0) ? $('.page-loader').show : $('.page-loader').hide)();
    };
};

app.MessageModal = function(config) {
    var self = this;

    var defaultConfig = {
        element: 'root',

        headerTemplateId: '',
        bodyTemplateId: '',

        headerTemplate: '',
        bodyTemplate: '',

        onShown: null,
        onHidden: null
    };

    var _config = $.extend({}, defaultConfig, config);

    self.onModalShown = function(e) {
        if (_config.onShown) {
            if (!_config.onShown(e)) {
                return;
            }
        }

        //TODO: Default modal logic
    };

    self.onModalHidden = function(e) {
        if (_config.onHidden) {
            if (!_config.onHidden(e)) {
                return;
            }
        }

        //TODO: Default modal logic
    };

    function bind() {
        var element = document.getElementById(_config.element);

        if (element) {
            if (ko.dataFor(element)) {
                ko.cleanNode(element);
            }

            ko.applyBindings(self, element);
        }

        $(element)
            .on('hidden.bs.modal', self.onModalHidden)
            .on('shown.bs.modal', self.onModalShown);
    }

    self.init = function() {
        //Bind model
        bind();
    };

    self.init();
}

app.RootModel = function (config) {
    var self = this;

    var messages = {
        ERROR: 'Error occurs while performing your request.',
        DATA_LOADING_ERROR: 'Error occures while loading data, please refresh page and try again.',
    };

    var defaultConfig = {
        element: 'root',
    };

    var _config = $.extend({}, defaultConfig, config);

    //Observable properties

    //Handlers

    //Functions

    function bind() {
        var element = document.getElementById(_config.element);
        if (element) {
            ko.applyBindings(self, element);
        }

        //TODO: Replace with message modal created on the fly (by KO)
        $('#message-box').on('hidden.bs.modal', onModalHidden);
    }

    self.init = function() {
        //Bind model
        bind();
    };

    self.init();
}
