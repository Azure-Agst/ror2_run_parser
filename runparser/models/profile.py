# -*- coding: utf-8 -*-
# flake8: noqa: E501,C901

"""
runparser.models.Profile
~~~~~~~~~~~~

This module implements the class that represents each profile.

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

from bs4 import Tag

import logging
import re

logger = logging.getLogger(__name__)


class Profile():
    """Implements the profile object."""

    def __init__(self, fileRoot: Tag = None):
        self.reset()
        self._fileRoot = fileRoot
        if self._fileRoot is not None:
            self.parse(self._fileRoot)

    def reset(self):
        self.version: int = 0

        self.name: str = None
        self.coins: int = 0
        self.totalLoginSeconds: int = 0
        self.totalAliveSeconds: int = 0
        self.totalRunSeconds: int = 0
        self.totalCoinsFound: int = 0

        self.gamesPlayed: int = 0
        self.timeAlive: float = 0
        self.kills: int = 0
        self.eliteKills: int = 0
        self.minionKills: int = 0
        self.bossKills: int = 0
        self.deaths: int = 0
        self.burnDeaths: int = 0
        self.deathsWhileBurning: int = 0
        self.highestLevel: int = 0
        self.totalDistanceTraveled: float = 0
        self.damageTaken: int = 0
        self.damageDealt: (int, int) = (0, 0)
        self.minionDamageDealt: int = 0
        self.healthHealed: int = 0
        self.goldCollected: (int, int) = (0, 0)
        self.itemsCollected: (int, int) = (0, 0)
        self.stagesCompleted: (int, int) = (0, 0)
        self.purchases = {
            "total": (0, 0),
            "gold": (0, 0),
            "blood": (0, 0),
            "lunar": (0, 0),
            "t1": (0, 0),
            "t2": (0, 0),
            "t3": (0, 0),
            "drones": 0,
            "turrets": 0,
            "greensoup": 0,
            "redsoup": 0
        }
        self.hermitCrabCliffKills: int = 0

        self.timeAliveAsCharacter: dict = {}
        self.totalWinsAsCharacter: dict = {}
        self.longestRunAsCharacter: dict = {}
        self.damageDealtTo: dict = {}
        self.damageDealtAs: dict = {}
        self.minionDamageDealtAs: dict = {}
        self.damageTakenFrom: dict = {}
        self.damageTakenAs: dict = {}
        self.killsAgainst: dict = {}
        self.killsAgainstElite: dict = {}
        self.deathsFrom: dict = {}
        self.killsAs: dict = {}
        self.minionKillsAs: dict = {}
        self.deathsAs: dict = {}
        self.timesPicked: dict = {}
        self.totalCollected: dict = {}
        self.highestCollected: dict = {}
        self.totalTimeHeld: dict = {}
        self.totalTimesFired: dict = {}
        self.totalTimesVisited: dict = {}
        self.totalTimesCleared: dict = {}

        self.charactersUnlocked: list = []
        self.artifactsUnlocked: list = []
        self.itemsUnlocked: list = []
        self.skillsUnlocked: list = {}

    def parse(self, rootTag: Tag):
        """Parses the player data."""

        # log the start
        logger.debug("Parsing player...")

        self.version = int(rootTag.find('version').text)
        self.name = rootTag.find('name').text
        self.coins = int(rootTag.find('coins').text)
        self.totalLoginSeconds = int(rootTag.find('totalloginseconds').text)
        self.totalAliveSeconds = int(rootTag.find('totalaliveseconds').text)
        self.totalRunSeconds = int(rootTag.find('totalrunseconds').text)
        self.totalCoinsFound = int(rootTag.find('totalcollectedcoins').text)

        stats = rootTag.find('stats')
        self.gamesPlayed = int(stats.find('stat', {'name': 'totalGamesPlayed'}).text)
        self.timeAlive = float(stats.find('stat', {'name': 'totalTimeAlive'}).text)
        self.kills = int(stats.find('stat', {'name': 'totalKills'}).text)
        self.eliteKills = int(stats.find('stat', {'name': 'totalEliteKills'}).text)
        self.minionKills = int(stats.find('stat', {'name': 'totalMinionKills'}).text)
        self.bossKills = int(stats.find('stat', {'name': 'totalTeleporterBossKillsWitnessed'}).text)
        self.deaths = int(stats.find('stat', {'name': 'totalDeaths'}).text)
        self.burnDeaths = int(stats.find('stat', {'name': 'totalBurnDeaths'}).text)
        self.deathsWhileBurning = int(stats.find('stat', {'name': 'totalDeathsWhileBurning'}).text)
        self.highestLevel = int(stats.find('stat', {'name': 'highestLevel'}).text)
        self.totalDistanceTraveled = float(stats.find('stat', {'name': 'totalDistanceTraveled'}).text)
        self.damageTaken = int(stats.find('stat', {'name': 'totalDamageTaken'}).text)
        self.damageDealt = (
            int(stats.find('stat', {'name': 'totalDamageDealt'}).text),
            int(stats.find('stat', {'name': 'highestDamageDealt'}).text)
        )
        self.minionDamageDealt = int(stats.find('stat', {'name': 'totalMinionDamageDealt'}).text)
        self.healthHealed = int(stats.find('stat', {'name': 'totalHealthHealed'}).text)
        self.goldCollected = (
            int(stats.find('stat', {'name': 'totalGoldCollected'}).text),
            int(stats.find('stat', {'name': 'maxGoldCollected'}).text)
        )
        self.itemsCollected = (
            int(stats.find('stat', {'name': 'totalItemsCollected'}).text),
            int(stats.find('stat', {'name': 'highestItemsCollected'}).text)
        )
        self.stagesCompleted = (
            int(stats.find('stat', {'name': 'totalStagesCompleted'}).text),
            int(stats.find('stat', {'name': 'highestStagesCompleted'}).text)
        )
        self.purchases = {
            "total": (
                int(stats.find('stat', {'name': 'totalPurchases'}).text),
                int(stats.find('stat', {'name': 'highestPurchases'}).text)
            ),
            "gold": (
                int(stats.find('stat', {'name': 'totalGoldPurchases'}).text),
                int(stats.find('stat', {'name': 'highestGoldPurchases'}).text)
            ),
            "blood": (
                int(stats.find('stat', {'name': 'totalBloodPurchases'}).text),
                int(stats.find('stat', {'name': 'highestBloodPurchases'}).text)
            ),
            "lunar": (
                int(stats.find('stat', {'name': 'totalLunarPurchases'}).text),
                int(stats.find('stat', {'name': 'highestLunarPurchases'}).text)
            ),
            "t1": (
                int(stats.find('stat', {'name': 'totalTier1Purchases'}).text),
                int(stats.find('stat', {'name': 'highestTier1Purchases'}).text)
            ),
            "t2": (
                int(stats.find('stat', {'name': 'totalTier2Purchases'}).text),
                int(stats.find('stat', {'name': 'highestTier2Purchases'}).text)
            ),
            "t3": (
                int(stats.find('stat', {'name': 'totalTier3Purchases'}).text),
                int(stats.find('stat', {'name': 'highestTier3Purchases'}).text)
            ),
            "drones": int(stats.find('stat', {'name': 'totalDronesPurchased'}).text),
            "turrets": int(stats.find('stat', {'name': 'totalTurretsPurchased'}).text),
            "greensoup": int(stats.find('stat', {'name': 'totalGreenSoupsPurchased'}).text),
            "redsoup": int(stats.find('stat', {'name': 'totalRedSoupsPurchased'}).text)
        }
        self.hermitCrabCliffKills = int(stats.find('stat', {'name': 'suicideHermitCrabsAchievementProgress'}).text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalTimeAlive\..*")}):
            char = tag['name'].replace("totalTimeAlive.", "").replace('Body', '')
            self.timeAliveAsCharacter[char.lower()] = float(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalWins\..*")}):
            char = tag['name'].replace("totalWins.", "").replace('Body', '')
            self.totalWinsAsCharacter[char.lower()] = float(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*longestRun\..*")}):
            char = tag['name'].replace("longestRun.", "").replace('Body', '')
            self.longestRunAsCharacter[char.lower()] = float(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*damageDealtTo\..*")}):
            char = tag['name'].replace("damageDealtTo.", "").replace('Body', '')
            self.damageDealtTo[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*damageDealtAs\..*")}):
            char = tag['name'].replace("damageDealtAs.", "").replace('Body', '')
            self.damageDealtAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*minionDamageDealtAs\..*")}):
            char = tag['name'].replace("minionDamageDealtAs.", "").replace('Body', '')
            self.minionDamageDealtAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*damageTakenFrom\..*")}):
            char = tag['name'].replace("damageTakenFrom.", "").replace('Body', '')
            self.damageTakenFrom[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*damageTakenAs\..*")}):
            char = tag['name'].replace("damageTakenAs.", "").replace('Body', '')
            self.damageTakenAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*killsAgainst\..*")}):
            char = tag['name'].replace("killsAgainst.", "").replace('Body', '')
            self.killsAgainst[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*killsAgainstElite\..*")}):
            char = tag['name'].replace("killsAgainstElite.", "").replace('Body', '')
            self.killsAgainstElite[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*deathsFrom\..*")}):
            char = tag['name'].replace("deathsFrom.", "").replace('Body', '')
            self.deathsFrom[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*killsAs\..*")}):
            char = tag['name'].replace("killsAs.", "").replace('Body', '')
            self.killsAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*minionKillsAs\..*")}):
            char = tag['name'].replace("minionKillsAs.", "").replace('Body', '')
            self.minionKillsAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*deathsAs\..*")}):
            char = tag['name'].replace("deathsAs.", "").replace('Body', '')
            self.deathsAs[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*timesPicked\..*")}):
            char = tag['name'].replace("timesPicked.", "").replace('Body', '')
            self.timesPicked[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalCollected\..*")}):
            char = tag['name'].replace("totalCollected.", "")
            self.totalCollected[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*highestCollected\..*")}):
            char = tag['name'].replace("highestCollected.", "")
            self.highestCollected[char.lower()] = float(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalTimeHeld\..*")}):
            char = tag['name'].replace("totalTimeHeld.", "")
            self.totalTimeHeld[char.lower()] = float(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalTimesFired\..*")}):
            char = tag['name'].replace("totalTimesFired.", "")
            self.totalTimesFired[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalTimesVisited\..*")}):
            char = tag['name'].replace("totalTimesVisited.", "")
            self.totalTimesVisited[char.lower()] = int(tag.text)

        for tag in stats.find_all('stat', {"name": re.compile(r".*totalTimesCleared\..*")}):
            char = tag['name'].replace("totalTimesCleared.", "")
            self.totalTimesCleared[char.lower()] = int(tag.text)

        for tag in stats.find_all('unlock'):
            tag_arr = tag.text.split('.')
            if tag_arr[0] == 'Characters':
                self.charactersUnlocked.append(tag_arr[1])
            if tag_arr[0] == 'Artifacts':
                self.artifactsUnlocked.append(tag_arr[1])
            if tag_arr[0] == 'Items':  # also includes equipment?
                self.artifactsUnlocked.append(tag_arr[1])
            if tag_arr[0] == 'Skills':
                if tag_arr[1] not in self.skillsUnlocked.keys():
                    self.skillsUnlocked[tag_arr[1]] = []
                self.skillsUnlocked[tag_arr[1]].append(tag_arr[2])

        logger.debug("Finished parsing profile: {}".format(self.name))
