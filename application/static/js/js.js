function genUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = crypto.getRandomValues(new Uint8Array(1))[0]%16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}

function showModal(viewModel, bodyTemplateId, headerTemplateId) {
    var element = document.getElementById('message-box');

    if (ko.dataFor(element)) {
        ko.cleanNode(element);
    }

    var body = document.getElementById(bodyTemplateId);
    var head = document.getElementById(headerTemplateId);

    if (body && body.innerHTML) {
        $('#message-box .modal-body p').html(body.innerHTML);
    }

    if (head && head.innerHTML) {
        $('#message-box .modal-header .modal-title').html(head.innerHTML);
    }

    ko.applyBindings(viewModel, element);

    $('#message-box').modal();

}

function flash(message, category) {
    var template = $('#alert-template').html();

    $element = $(template
        .replace('{CATEGORY}', category)
        .replace('{ALERT_ID}', genUUID())
        .replace('{MESSAGE}', message));

    $('.flashes').append($element);

    (function() {
        var $el = $element;

        setTimeout(function() {
            $el.fadeOut('slow', function() { $el.remove(); });
        }, 2000);
    })();
}

ko.bindingHandlers.stopBindings = {
    init: function() {
        return { controlsDescendantBindings: true };
    }
};
