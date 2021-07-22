# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Tag
from runparser import Profile

import unittest
import os


class test_Profile(unittest.TestCase):
    """Basic Profile test cases."""

    profile: Profile = None
    file_root: Tag = None

    def setUp(self):
        """Set up the test cases."""
        file_name = os.path.join(os.path.dirname(__file__), "files/profiles/profile.xml")
        with open(file_name, "r") as f:
            self.file_root = BeautifulSoup(f, "html.parser")

        self.profile = Profile(self.file_root)

    def tearDown(self):
        """Tear down the test cases."""
        self.profile = None
        self.file_root = None

    def test_Profile_GeneralData(self):
        """Tests general profile data."""
        self.assertEqual(self.profile.version, 2)
        self.assertEqual(self.profile.name, "Azure")
        self.assertEqual(self.profile.coins, 125)
        self.assertEqual(self.profile.totalLoginSeconds, 161905)
        self.assertEqual(self.profile.totalAliveSeconds, 96865)
        self.assertEqual(self.profile.totalRunSeconds, 102546)
        self.assertEqual(self.profile.totalCoinsFound, 174)

    def test_Profile_StatsGeneralData(self):
        """Tests general data coming from stats key."""
        self.assertEqual(self.profile.gamesPlayed, 87)
        self.assertAlmostEqual(self.profile.timeAlive, 91946.688, places=3)
        self.assertEqual(self.profile.kills, 18031)
        self.assertEqual(self.profile.eliteKills, 2517)
        self.assertEqual(self.profile.minionKills, 2197)
        self.assertEqual(self.profile.bossKills, 643)
        self.assertEqual(self.profile.deaths, 34)
        self.assertEqual(self.profile.burnDeaths, 3)
        self.assertEqual(self.profile.deathsWhileBurning, 7)
        self.assertEqual(self.profile.highestLevel, 22)
        self.assertAlmostEqual(self.profile.totalDistanceTraveled, 1276697.662, places=3)
        self.assertEqual(self.profile.damageTaken, 230633)
        self.assertEqual(self.profile.damageDealt, (16736005, 76167))
        self.assertEqual(self.profile.minionDamageDealt, 1811283)
        self.assertEqual(self.profile.healthHealed, 300861)
        self.assertEqual(self.profile.goldCollected, (569066, 75686))
        self.assertEqual(self.profile.itemsCollected, (1647, 89))
        self.assertEqual(self.profile.stagesCompleted, (264, 12))
        self.assertEqual(self.profile.purchases, {
            "total": (1159, 96),
            "gold": (917, 86),
            "blood": (15, 4),
            "lunar": (31, 5),
            "t1": (16, 10),
            "t2": (1, 1),
            "t3": (0, 0),
            "drones": 82,
            "turrets": 55,
            "greensoup": 17,
            "redsoup": 1
        })
        self.assertEqual(self.profile.hermitCrabCliffKills, 20)

    def test_Profile_StatsSubkeyedData(self):
        """Tests subkeyed data parsing from stats key."""
        self.assertAlmostEqual(self.profile.timeAliveAsCharacter['bandit2'], 19033.251, places=3)
        self.assertEqual(self.profile.totalWinsAsCharacter['huntress'], 6)
        self.assertAlmostEqual(self.profile.longestRunAsCharacter['captain'], 2215.985, places=3)
        self.assertEqual(self.profile.damageDealtTo['clayboss'], 380216)
        self.assertEqual(self.profile.damageDealtAs['engi'], 277059)
        self.assertEqual(self.profile.minionDamageDealtAs['engi'], 599380)
        self.assertEqual(self.profile.damageTakenFrom['imp'], 7961)
        self.assertEqual(self.profile.damageTakenAs['commando'], 4533)
        self.assertEqual(self.profile.killsAgainst['hermitcrab'], 127)
        self.assertEqual(self.profile.killsAgainstElite['jellyfish'], 171)
        self.assertEqual(self.profile.deathsFrom['bell'], 4)
        self.assertEqual(self.profile.killsAs['loader'], 992)
        self.assertEqual(self.profile.minionKillsAs['engi'], 755)
        self.assertEqual(self.profile.deathsAs['mage'], 4)
        self.assertEqual(self.profile.timesPicked['croco'], 27)
        self.assertEqual(self.profile.totalCollected['barrieronkill'], 101)
        self.assertEqual(self.profile.highestCollected['crowbar'], 12)
        self.assertAlmostEqual(self.profile.totalTimeHeld['blackhole'], 15074.884, places=3)
        self.assertEqual(self.profile.totalTimesFired['lightning'], 180)
        self.assertEqual(self.profile.totalTimesVisited['blackbeach'], 59)
        self.assertEqual(self.profile.totalTimesCleared['mysteryspace'], 17)
