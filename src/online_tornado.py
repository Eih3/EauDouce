#!/usr/bin/python -O
# -*- coding: utf-8 -*-
"""
    EauDouce.online_tornado
    ~~~~~~~~~~~~~~

    This is the start of the production environment, using the tornado.

    :copyright: (c) 2017 by Mr.tao.
    :license: MIT, see LICENSE for more details.
"""

from main import app
from config import GLOBAL
from utils.tool import logger

Host = "0.0.0.0"
Port = GLOBAL.get('Port')
Environment = GLOBAL.get('Environment')
ProcessName = GLOBAL.get('ProcessName')

try:
    import setproctitle
except ImportError, e:
    logger.warn("%s, try to pip install setproctitle, otherwise, you can't use the process to customize the function" %e)
else:
    setproctitle.setproctitle(ProcessName)
    logger.info("The process is %s" % ProcessName)

try:
    msg = '%s has been launched, %s:%s' %(ProcessName, Host, Port)
    print(msg)
    logger.info(msg)
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(Port)
    IOLoop.instance().start()

except Exception,e:
    print(e)
    logger.error(e, exc_info=True)