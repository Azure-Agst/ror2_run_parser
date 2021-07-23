# -*- coding: utf-8 -*-
# flake8: noqa: E401

__title__ = 'RoR2RunParser'
__author__ = 'Andrew Augustine'
__author_email__ = 'me@azureagst.dev'
__license__ = 'GPL-3.0 License'
__version__ = '0.1.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import os
import sys
import logging

# set up logging
filename = 'runparser.log'
encoding = 'utf-8'
output_fmt = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
if os.getenv('CI') == 'true':
    level = logging.WARNING
else:
    level = logging.DEBUG

# if py3.9 or later, add encodings to the logger
if sys.version_info > (3, 9):
    logging.basicConfig(filename=filename, encoding='utf-8', format=output_fmt, level=level)
else:
    logging.basicConfig(filename=filename, format=output_fmt, level=level)


# subpackages
from .db import *
from .models import *
from .utils import *

# main classes
from .runparser import *
from .autorunparser import *
