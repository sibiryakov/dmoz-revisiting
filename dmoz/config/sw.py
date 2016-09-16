# -*- coding: utf-8 -*-
from worker import *
from datetime import timedelta

SQLALCHEMYBACKEND_ENGINE = 'sqlite:///states.sqlite'
LOGGING_CONFIG='logging-sw.conf'
REVISIT_INTERVAL = timedelta(minutes=5)