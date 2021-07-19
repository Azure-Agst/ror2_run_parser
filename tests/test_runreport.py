# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Tag
from runparser import RunReport
from pathlib import Path

import unittest
import os
import time

import logging

class test_RunReport(unittest.TestCase):
    """Basic RunReport test cases."""

    report : RunReport = None
    file_root : Tag = None

    def setUp(self):
        """Set up the test cases."""
        file_name = os.path.join(os.path.dirname(__file__), "files/runs/run1.xml")
        with open(file_name, "r") as f:
            self.file_root = BeautifulSoup(f, "html.parser")

        self.report = RunReport(self.file_root)


    def tearDown(self):
        """Tear down the test cases."""
        del self.report
        del self.file_root


    def test_RunReport_GeneralData(self):
        """Tests general run report data."""
        self.assertEqual(self.report.version, 2)
        self.assertEqual(self.report.guid, "1e610e1c-08f9-4321-af86-31fa772d9cd6")
        self.assertEqual(self.report.gamemode, "ClassicRun")
        self.assertEqual(self.report.seed, 12154124160401593415)
        self.assertEqual(self.report.start_timestamp, 5249308319550832228)
        self.assertEqual(self.report.end_timestamp, 5249308344751840833)
        self.assertEqual(self.report.total_time, 2501.105)
        self.assertEqual(self.report.run_time, 2216.018)


    def test_RunReport_RuleData(self):
        """Tests run report's rule data."""
        self.assertEqual(self.report.difficulty, "Easy")
        self.assertNotIn("Command", self.report.artifacts)
        self.assertIn("Tooth", self.report.enabled_items)
        self.assertNotIn("Clover", self.report.enabled_items)
        self.assertIn("Clover", self.report.disabled_items)
        self.assertNotIn("Tooth", self.report.disabled_items)
        self.assertIn("Fruit", self.report.enabled_equipment)
        self.assertNotIn("Meteor", self.report.enabled_equipment)
        self.assertIn("Meteor", self.report.disabled_equipment)
        self.assertNotIn("Fruit", self.report.disabled_equipment)
        self.assertEqual(self.report.misc['StartingMoney'], "15")
        self.assertEqual(self.report.misc['StageOrder'], "Normal")
        self.assertEqual(self.report.misc['KeepMoneyBetweenStages'], "Off")
        self.assertEqual(self.report.misc['AllowDropIn'], "Off")