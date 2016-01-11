# -*- coding: utf-8 -*-

from flask import current_app

strip = lambda s: s.strip() if s is not None else ''
lower = lambda s: s.lower() if s is not None else ''


def app_config_item(name):
    return current_app.config[name]


def app_settings_item(key):
    """
    Jinja filter to retrieve data from settings module.
    Acceptable imput is:
    - dot-separated hierarchycal key, value will be retrieved
        recursively until last one catched. If at one step exception occures
        or False-evaluatable value will be received None returns
    - List or tuple of keys (joined by dot will returns the same string as
        in option 1). Value will be retrieved recursively.
    """

    from creaturecast.config import settings

    def get_setting_value(keys):
        scope = settings

        try:
            for key in keys:
                if type(scope) == dict:
                    scope = scope.get(key, None)
                else:
                    scope = getattr(scope, key, None)

                if not scope:
                    return None

            return scope
        except:
            return None

    if type(key) in [str, unicode]:
        return get_setting_value(key.split('.'))
    elif type(key) in [tuple, list]:
        return get_setting_value(key)

    return ''
