# -*- coding: utf-8 -*-
# flake8: noqa: E401

import os
import sys
import logging

# set up logging
filename = 'runparser.log'
encoding = 'utf-8'
output_fmt = '%(asctime)s: %(levelname)s: %(message)s'
if os.getenv('CI') == 'true':
    level = logging.WARNING
else:
    level = logging.DEBUG

# if py3.9 or later, add encodings to the logger
if sys.version_info > (3, 9):
    logging.basicConfig(filename=filename, encoding='utf-8', format=output_fmt, level=level)
else:
    logging.basicConfig(filename=filename, format=output_fmt, level=level)

from .__version__ import __title__, __description__, __url__, __version__, \
    __build__, __author__, __author_email__, __license__, __copyright__

# main classes
from .runparser import RunParser
from .autorunparser import AutoRunParser

# db classes
from .db import RunParserDB, RPDB_EntryNotFoundError, RPDB_ArgumentError

# models
from .models.runreport import RunReport
from .models.player import Player
from .models.profile import Profile
