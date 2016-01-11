# -*- coding: utf-8 -*-

from flask import render_template
from flask.views import MethodView
from flask import jsonify


class BasePageView(MethodView):
    def get_template(self):
        raise NotImplemented('View method "get_template" must return template name')

    def get_context(self, **kwargs):
        context = {}
        context.update(**kwargs)

        return context

    def get(self):
        return render_template(self.get_template(), **self.get_context())


class BaseServiceView(MethodView):
    def response_ok(self, message='', data={}):
        return jsonify(**{'success': True, 'message': message, 'data': data}), 200

    def response_fail(self, message='', data={}):
        return jsonify(**{'success': False, 'message': message, 'data': data}), 200

    def response_error(self, message='', data={}):
        return jsonify(**{'success': False, 'message': message, 'data': data}), 500

    def response_unauth(self, message='', data={}):
        return jsonify(**{'success': False, 'message': message, 'data': data}), 401
