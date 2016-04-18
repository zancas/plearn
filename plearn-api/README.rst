Documentation
=============

Plearn is about plearning, but every project needs an API.  Pyramid_ is a mature WSGI framework, on top of which a REST framework called Cornice_ has been built.

.. _Pyramid: http://docs.pylonsproject.org/projects/pyramid/en/latest/
.. _Cornice: https://cornice.readthedocs.org/en/latest/index.html

To build the API documentation(from plearn-api directory)::

   sphinx-build docs/source docs/build

To start the server from this directory::

   python setup.py install
   pserve plearn.ini --reload

TODO: how to query the API



