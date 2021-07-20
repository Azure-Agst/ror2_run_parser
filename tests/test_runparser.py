# -*- coding: utf-8 -*-

from runparser import RunParser

import unittest
import os


class test_RunParser(unittest.TestCase):
    """Basic RunParser test cases."""

    rp: RunParser = None

    def setUp(self):
        """Set up the test cases."""
        replay_path = os.path.join(os.path.dirname(__file__), "files/runs")
        profile_path = os.path.join(os.path.dirname(__file__), "files/profiles")
        self.rp = RunParser(replay_dir=replay_path, profile_dir=profile_path)

    def tearDown(self):
        """Tear down the test cases."""
        del self.rp

    def test_RunParser_ParseRuns(self):
        """Test parsing of replay data."""
        self.rp.parse_runs()
