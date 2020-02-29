from gevent import monkey
monkey.patch_all()
import gevent

gevent.getcurrent().gr_name = 'MAIN'

import utils.log
utils.log.patch_gevent_hub_print_exception()

import _pytest.logging

_pytest.logging.LoggingPlugin._create_formatter = lambda *_: utils.log.ServerLogFormatter()

from thb.thbunit import inject
inject()