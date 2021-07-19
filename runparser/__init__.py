# -*- coding: utf-8 -*-

from platform import uname

import sys
import logging

# make sure we're running on windows
if 'Windows' not in uname().system:
    ex_string = "This script is only for Windows!"
    if 'Linux' in uname().system and 'microsoft' in uname().release:
        ex_string += "\n\nPsst! We've detected a WSL install. RunParser doesn't work here yet,\nbut it might soon! Stick with a Windows python install for now. :)\n"
    raise Exception(ex_string)

# set up logging
filename = 'runparser.log'
encoding = 'utf-8'
output_fmt = '%(asctime)s: %(levelname)s: %(message)s'
level = logging.WARNING
if sys.version_info > (3, 9):
    # if py3.9 or later, add encodings to the logger
    logging.basicConfig(filename=filename, encoding='utf-8', format=output_fmt, level=level)
else:
    logging.basicConfig(filename=filename, format=output_fmt, level=level)

# import modules
from .runparser import RunParser
from .models.runreport import RunReport
from .models.player import Player
from .models.profile import Profile
