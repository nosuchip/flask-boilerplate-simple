# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask.views import MethodView
from application.common.views import BasePageView


module = Blueprint('default', __name__)


class DefaultView(BasePageView):
    def get_template(self):
        return 'default/index.html'

module.add_url_rule('/', view_func=DefaultView.as_view('index'), methods=['GET', 'POST', 'PUT', 'DELETE'])
