# -*- coding: utf-8 -*-

from platform import uname

# make sure we're running on windows
if 'Windows' not in uname().system:
    ex_string = "This script is only for Windows!"
    if 'Linux' in uname().system and 'microsoft' in uname().release:
        ex_string += "\n\nPsst! We've detected a WSL install. RunParser doesn't work here yet,\nbut it might soon! Stick with a Windows python install for now. :)\n"
    raise Exception(ex_string)

# set up logging
import logging
logging.basicConfig(
    filename='runparser.log', 
    encoding='utf-8', 
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    level=logging.DEBUG
)

# import modules
from .runparser import RunParser
from .models.runreport import RunReport
from .models.player import Player
from .models.profile import Profile