# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, Tag
from runparser import Player

import unittest
import os


class test_Player(unittest.TestCase):
    """Basic Player test cases."""

    player: Player = None
    file_root: Tag = None

    def setUp(self):
        """Set up the test cases."""
        file_name = os.path.join(os.path.dirname(__file__), "files/player.xml")
        with open(file_name, "r") as f:
            self.file_root = BeautifulSoup(f, "html.parser")

        self.player = Player(self.file_root)

    def tearDown(self):
        """Tear down the test cases."""
        del self.player
        del self.file_root

    def test_Player_GeneralData(self):
        """Tests general player data."""
        self.assertEqual(self.player.name, "Azure")
        self.assertEqual(self.player.character, "Captain")
        self.assertEqual(self.player.killed, False)
        self.assertEqual(self.player.killedBy, "N/A")

    def test_Player_GameData(self):
        """Tests run specific generic data."""
        self.assertEqual(self.player.gamesPlayed, 1)
        self.assertEqual(self.player.maxLevel, 16)
        self.assertAlmostEqual(self.player.distanceTravelled, 35257.767, places=3)
        self.assertEqual(self.player.stagesCompleted, 8)
        self.assertAlmostEqual(self.player.timeAlive, 2214.100, places=3)
        self.assertEqual(self.player.equipment, "Lightning")
        self.assertEqual(self.player.items[4].count, 3)
        self.assertEqual(self.player.items[4].name, "Ghor's Tome")
        self.assertEqual(self.player.itemAcquisitionOrder[7], "Medkit")

    def test_Player_KillData(self):
        """Tests kill/damage specific data."""
        self.assertEqual(self.player.totalKills, 436)
        self.assertEqual(self.player.minionKills, 70)
        self.assertEqual(self.player.eliteKills, 67)
        self.assertEqual(self.player.bossKills, 11)
        self.assertEqual(self.player.totalDmgDealt, 342060)
        self.assertEqual(self.player.minionDmgDealt, 82460)
        self.assertEqual(self.player.dmgTaken, 3502)
        self.assertEqual(self.player.dmgHealed, 16288)

    def test_Player_StoreData(self):
        """Tests store/purchase specific data."""
        self.assertEqual(self.player.goldCollected, 17410)
        self.assertEqual(self.player.itemsCollected, 35)
        self.assertEqual(self.player.totalPurchases, 34)
        self.assertEqual(self.player.goldPurchases, 31)
        self.assertEqual(self.player.lunarPurchases, 1)
        self.assertEqual(self.player.dronesPurchased, 4)
        self.assertEqual(self.player.turretsPurchased, 1)

    def test_Player_StatData(self):
        """Tests stats specific data."""
        # no way i'm testing all of this, random sampling will do
        self.assertAlmostEqual(self.player.timeAliveAsCharacter['captain'], 2213.967, places=3)
        self.assertAlmostEqual(self.player.longestRunAsCharacter['captain'], 2215.985, places=3)
        self.assertEqual(self.player.damageDealtTo['clayboss'], 4417)
        self.assertEqual(self.player.damageDealtAs['captain'], 342060)
        self.assertEqual(self.player.minionDamageDealtAs['captain'], 82460)
        self.assertEqual(self.player.damageTakenFrom['imp'], 44)
        self.assertEqual(self.player.damageTakenAs['captain'], 3502)
        self.assertEqual(self.player.killsAgainst['lemurian'], 86)
        self.assertEqual(self.player.killsAgainstElite['minimushroom'], 1)
        self.assertEqual(self.player.killsAs['captain'], 436)
        self.assertEqual(self.player.minionKillsAs['captain'], 70)
        self.assertEqual(self.player.timesPicked['captain'], 1)
        self.assertEqual(self.player.totalCollected['focusconvergence'], 1)
        self.assertAlmostEqual(self.player.totalTimeHeld['bfg'], 743.950, places=3)
        self.assertEqual(self.player.totalTimesFired['lightning'], 12)
        self.assertEqual(self.player.totalTimesVisited['blackbeach'], 2)
        self.assertEqual(self.player.totalTimesCleared['mysteryspace'], 1)
