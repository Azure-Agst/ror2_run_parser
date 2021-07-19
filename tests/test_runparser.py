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
        replay_path = os.path.join(os.path.dirname(__file__), "files/runs")
        profile_path = os.path.join(os.path.dirname(__file__), "files/profiles")
        self.rp = RunParser(replay_dir=replay_path, profile_dir=profile_path)


    def tearDown(self):
        """Tear down the test cases."""
        del self.rp


    def test_RunParser_Parse10Runs(self):
        """
        Test parsing of the runs.
        """
        self.rp.parse_runs()
       


