# -*- coding: utf-8 -*-

# Put here settings realted to application, but noto Flask directly.
# Settings from this files must be user via `from application.config import settings`
# Settings from this files mustn't be user for populate Flask config

import os
import logging


LOG_LEVEL = getattr(logging, os.getenv('LOG_LEVEL', 'INFO'))

# NOTE: If you do not need to setup complex Blueprint and simple one-function endpoint is enough
#       then specify routes there and add corresponding file/function to /routes folder

ROUTES = [{
    'module': 'favicon',
    'endpoint': 'favicon',
    'route': '/favicon/<filename>',
    'methods': ['GET'],
#}, {
#    'module': 'routes.image',
#    'endpoint': 'image',
#    'route': '/image/<attachment_uid>',
#    'methods': ['GET']
}]
