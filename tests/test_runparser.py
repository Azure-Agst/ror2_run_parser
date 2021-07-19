# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Tag
from runparser import RunParser
from pathlib import Path

import unittest
import os
import time

class test_RunParser(unittest.TestCase):
    """Basic Player test cases."""

    rp : RunParser = None

    def setUp(self):
        """Set up the test cases."""
        self.rp = RunParser()


    def tearDown(self):
        """Tear down the test cases."""
        del self.rp


    def test_RunParser_Parse10Runs(self):
        """Test parsing of the runs."""
        self.rp.parse_runs()
       


