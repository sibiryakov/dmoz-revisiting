# -*- coding: utf-8 -*-
from datetime import timedelta

BACKEND = 'frontera.contrib.backends.sqlalchemy.revisiting.Backend'
SQLALCHEMYBACKEND_ENGINE = 'sqlite:///frontera.sqlite'
SQLALCHEMYBACKEND_ENGINE_ECHO = False
SQLALCHEMYBACKEND_DROP_ALL_TABLES = False
SQLALCHEMYBACKEND_CLEAR_CONTENT = False

SQLALCHEMYBACKEND_REVISIT_INTERVAL = timedelta(seconds=43200)

MAX_NEXT_REQUESTS = 512
NEW_BATCH_DELAY = 3.0