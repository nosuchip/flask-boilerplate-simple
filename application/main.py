# -*- coding: utf-8 -*-

from flask import Flask
from application.routes import configure_routes
from application.config import settings
from application.common import filters

import logging


def init(name):
    app = Flask(name)

    configure_app(app)
    configure_extensions(app)
    configure_routes(app)
    configure_blueprint(app)

    return app


def configure_app(app):
    app.logger.setLevel(settings.LOG_LEVEL)
    app.config.from_object('application.config.app_config')

    app.jinja_env.filters['app_config_item'] = filters.app_config_item
    app.jinja_env.filters['app_settings_item'] = filters.app_settings_item


def configure_extensions(app):
    pass


def configure_blueprint(app):
    from application.default.views import module as default_module
    app.register_blueprint(default_module, url_prefix='')


app = init(__name__)
