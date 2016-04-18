FROM python:2.7.11-onbuild
RUN python setup.py install
EXPOSE 6543
CMD ["/usr/local/bin/pserve", "plearn_api.ini", "--reload"]

