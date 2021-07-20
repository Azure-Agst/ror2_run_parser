# -*- coding: utf-8 -*-

from runparser import AutoRunParser

import unittest
import os


@unittest.skipIf(os.getenv('CI') == 'true', "Can't be run on CI")
@unittest.skipUnless(os.name == 'nt', "Has to be run on Windows")
class test_AutoRunParser(unittest.TestCase):
    """Basic AutoRunParser test cases."""

    rp: AutoRunParser = None

    def setUp(self):
        """Set up the test cases."""
        self.rp = AutoRunParser()

    def tearDown(self):
        """Tear down the test cases."""
        del self.rp

    def test_AutoRunParser_ParseRuns(self):
        """Test parsing of replay data."""
        self.rp.parse_runs()
