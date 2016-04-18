"""Request validation (authentication, authorization, validation)
"""
import os
import binascii
import json

from passlib.context import CryptContext
from webob import Response, exc
from cornice import Service

pwd_context = CryptContext(schemes=["sha256_crypt", "ldap_salted_md5"],
                           sha256_crypt__default_rounds=91234,
                           ldap_salted_md5__salt_size=16)

# TODO - users, tokens need to be persisted in a database somewhere

_USERS = {
    "testuser": {
        "password": pwd_context.encrypt("testpassword")
    }
}

class _401(exc.HTTPError):
    def __init__(self, msg='Unauthorized'):
        body = {'status': 401, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = 401
        self.content_type = 'application/json'

def _generate_token():
    return binascii.b2a_hex(os.urandom(20))

def valid_token(request):
    header = 'Authorization'
    htoken = request.headers.get(header)
    if htoken is None:
        raise _401()
    try:
        user, token = htoken.split('-', 1)
    except ValueError:
        raise _401()

    valid = user in _USERS and _USERS[user]["token"] == token
    if not valid:
        raise _401()

    request.validated['user'] = user

def authenticate(request):
    req_json = json.loads(request.body)
    
    username = req_json['username']
    password = req_json['password']
    if username in _USERS:
        if pwd_context.verify(password, _USERS[username]['password']):
            token = _generate_token()
            _USERS[username]["token"] = token
            request.validated['token'] = '%s-%s' % (username, token)
        else:
            raise _401()
    else:
        raise _401()
