# -*- coding: utf-8 -*-

import os
import binascii
import uuid


def gen_token(length=100):
    return binascii.hexlify(os.urandom(length / 2))[:length]


def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format) if date else ''


def gen_uid():
    return uuid.uuid4().hex
