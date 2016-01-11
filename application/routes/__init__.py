# -*- coding: utf-8 -*-

import os
import importlib
from flask import send_from_directory, render_template
from application.config import settings


def configure_routes(app):
    for module_config in settings.ROUTES:
        module = importlib.import_module('{}.routes.{}'.format(app.config['APP_NAME'],
                                                        module_config['module']))

        endpoint = getattr(module, module_config['endpoint'])
        default_args = module_config.get('defaults', {})

        app.add_url_rule(
            module_config['route'],
            module_config['endpoint'],
            endpoint,
            methods=module_config['methods'],
            **default_args
        )

    @app.errorhandler(404)
    def page_error_404(error):
        return render_template(
            'errors/404.html',
            title='404 error: Not Found',
            text=u'The requested URL was not found on this server.',
            error=error
        ), 404

    @app.errorhandler(500)
    def page_error_404(error):
        return render_template(
            'errors/500.html',
            title='500 error: ARRRRGHHHHH',
            text=u'You broken teh Internet.',
            error=error
        ), 500
