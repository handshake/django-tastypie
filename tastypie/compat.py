from __future__ import unicode_literals

import django

try:
    from django.urls import NoReverseMatch, reverse, resolve, Resolver404, get_script_prefix  # noqa
except ImportError:  # 1.8 backwards compat
    from django.core.urlresolvers import NoReverseMatch, reverse, resolve, Resolver404, get_script_prefix  # noqa

# Compatability for salted vs unsalted CSRF tokens;
# Django 1.10's _sanitize_token also hashes it, so it can't be compared directly.
# Solution is to call _sanitize_token on both tokens, then unsalt or noop both
try:
    from django.middleware.csrf import _unsalt_cipher_token

    def unsalt_token(token):
        return _unsalt_cipher_token(token)
except ImportError:

    def unsalt_token(token):
        return token
