""" Plearn services.
"""
from cornice import Service
from request_validation import *

login = Service(name='login', path='/login', description="Get a token")

@login.post(validators=authenticate)
def create_token(request):
    """Get a token"""
    return {'token': request.validated['token']}

plearn = Service(name='plearn', path='/', description="A teaching system that learns")

@plearn.get(validators=valid_token)
def get_info(request):
    """Ask a question"""
    return {'Hello': 'World'}

