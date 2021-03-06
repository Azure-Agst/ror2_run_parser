# -*- coding: utf-8 -*-

from runparser.db import RunParserDB, RunParserDBConn

import unittest


class test_RunParserDB(unittest.TestCase):
    """Basic RunParserDB test cases."""

    def setUp(self):
        """Set up the test cases."""
        self.db = RunParserDBConn()

    def test_RunParserDB_Items(self):
        """Test getting Item data."""

        # get item by internal name
        item = self.db.get_item("LunarBadLuck")
        self.assertEqual(item['name'], "Purity")

        # get item by actual name
        item = self.db.get_item(name="Fuel Cell")
        self.assertEqual(item['internal_name'], "EquipmentMagazine")

        # get nonexistent item by internal name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_item("thisdoesnotexist")

        # get nonexistent item by actual name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_item(name="Fake Item")

        # call with no arguments
        with self.assertRaises(RunParserDB.Controller.ArgumentError):
            self.db.get_item()

    def test_RunParserDB_Equipment(self):
        """Test getting Equipment data."""

        # get equipment by internal name
        item = self.db.get_equipment("lightning")
        self.assertEqual(item['name'], "Royal Capacitor")

        # get equipment by actual name
        item = self.db.get_equipment(name="Glowing Meteorite")
        self.assertEqual(item['internal_name'], "Meteor")

        # get nonexistent equipment by internal name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_equipment("thisdoesnotexist")

        # get nonexistent equipment by actual name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_equipment(name="Fake Equipment")

        # call with no arguments
        with self.assertRaises(RunParserDB.Controller.ArgumentError):
            self.db.get_equipment()

    def test_RunParserDB_Artifacts(self):
        """Test getting Artifact data."""

        # get artifact by internal name
        item = self.db.get_artifact("shadowclone")
        self.assertEqual(item['name'], "Artifact of Vengeance")

        # get artifact by actual name
        item = self.db.get_artifact(name="Artifact of Sacrifice")
        self.assertEqual(item['internal_name'], "Sacrifice")

        # get artifact equipment by internal name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_artifact("thisdoesnotexist")

        # get artifact equipment by actual name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_artifact(name="Fake Artifact")

        # call with no arguments
        with self.assertRaises(RunParserDB.Controller.ArgumentError):
            self.db.get_artifact()

    def test_RunParserDB_Survivors(self):
        """Test getting Survivor data."""

        # get survivor by internal name
        item = self.db.get_survivor("bandit2")
        self.assertEqual(item['name'], "Bandit")

        # get survivor by actual name
        item = self.db.get_survivor(name="MUL-T")
        self.assertEqual(item['internal_name'], "Toolbot")

        # get survivor equipment by internal name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_survivor("thisdoesnotexist")

        # get survivor equipment by actual name
        with self.assertRaises(RunParserDB.Controller.EntryNotFoundError):
            self.db.get_survivor(name="Fake Survivor")

        # call with no arguments
        with self.assertRaises(RunParserDB.Controller.ArgumentError):
            self.db.get_survivor()
