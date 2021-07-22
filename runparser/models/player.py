# -*- coding: utf-8 -*-
# flake8: noqa: E501,C901

"""
runparser.models.Player
~~~~~~~~~~~~

This module implements the class that represents each player.

:copyright: (c) 2021 by Andrew Augustine.
:license: GPL-3.0, see LICENSE for more details.
"""

from bs4 import Tag

import logging
import re

from .item import Item
from .equipment import Equipment
from .survivor import Survivor

logger = logging.getLogger(__name__)


class Player():
    """Implements the player object."""

    def __init__(self, fileRoot: Tag = None):
        self.reset()
        self._fileRoot = fileRoot
        if self._fileRoot is not None:
            self.parse(self._fileRoot)

    def reset(self):
        self.name: str = None
        self.character: Survivor = None
        self.killed: bool = False
        self.killedBy: str = None
        self.equipment: Equipment = None
        self.items: [Item] = []

        self.gamesPlayed: int = 0
        self.maxLevel: int = 0
        self.distanceTravelled: float = 0.0
        self.stagesCompleted: int = 0
        self.timeAlive: float = 0.0

        self.totalKills: int = 0
        self.minionKills: int = 0
        self.eliteKills: int = 0
        self.bossKills: int = 0
        self.totalDmgDealt: int = 0
        self.minionDmgDealt: int = 0
        self.dmgTaken: int = 0
        self.dmgHealed: int = 0

        self.goldCollected: int = 0
        self.itemsCollected: int = 0
        self.totalPurchases: int = 0
        self.goldPurchases: int = 0
        self.lunarPurchases: int = 0
        self.dronesPurchased: int = 0
        self.turretsPurchased: int = 0

        self.timeAliveAsCharacter: dict = {}
        self.longestRunAsCharacter: dict = {}
        self.damageDealtTo: dict = {}
        self.damageDealtAs: dict = {}
        self.minionDamageDealtAs: dict = {}
        self.damageTakenFrom: dict = {}
        self.damageTakenAs: dict = {}
        self.killsAgainst: dict = {}
        self.killsAgainstElite: dict = {}
        self.killsAs: dict = {}
        self.minionKillsAs: dict = {}
        self.timesPicked: dict = {}
        self.totalCollected: dict = {}
        self.totalTimeHeld: dict = {}
        self.totalTimesFired: dict = {}
        self.totalTimesVisited: dict = {}
        self.totalTimesCleared: dict = {}

        self.itemAcquisitionOrder: list = []

    def parse(self, rootTag: Tag):
        """Parses the player data."""

        # log the start
        logger.debug("Parsing player...")

        self.name = rootTag.find('name').text
        self.character = Survivor(rootTag.find('bodyname').text.replace("Body", ""))
        self.killed = rootTag.find('isdead').text == '1'
        self.killedBy = rootTag.find('killerbodyname').text.replace("Body", "").replace("Invalid", "N/A")

        statsheet = rootTag.find('statsheet').fields

        self.gamesPlayed = int(statsheet.find('totalgamesplayed').text) if statsheet.find('totalgamesplayed') != None else 0
        self.maxLevel = int(statsheet.find('highestlevel').text) if statsheet.find('highestlevel') != None else 0
        self.distanceTravelled = float(statsheet.find('totaldistancetraveled').text) if statsheet.find('totaldistancetraveled') != None else 0.0
        self.stagesCompleted = int(statsheet.find('totalstagescompleted').text) if statsheet.find('totalstagescompleted') != None else 0
        self.timeAlive = float(statsheet.find('totaltimealive').text) if statsheet.find('totaltimealive') != None else 0.0
        
        if rootTag.find('equipment') is not None:
            self.equipment = Equipment(rootTag.find('equipment').text)
        
        for item_tag in rootTag.find('itemstacks').find_all():
            self.items.append(Item(item_tag.name, count=int(item_tag.text)))

        self.totalKills = int(statsheet.find('totalkills').text) if statsheet.find('totalgoldcollected') != None else 0
        self.minionKills = int(statsheet.find('totalminionkills').text) if statsheet.find('totalminionkills') != None else 0
        self.eliteKills = int(statsheet.find('totalelitekills').text) if statsheet.find('totalelitekills') != None else 0
        self.bossKills = int(statsheet.find('totalteleporterbosskillswitnessed').text) if statsheet.find('totalteleporterbosskillswitnessed') != None else 0
        self.totalDmgDealt = int(statsheet.find('totaldamagedealt').text) if statsheet.find('totaldamagedealt') != None else 0
        self.minionDmgDealt = int(statsheet.find('totalminiondamagedealt').text) if statsheet.find('totalminiondamagedealt') != None else 0
        self.dmgTaken = int(statsheet.find('totaldamagetaken').text) if statsheet.find('totaldamagetaken') != None else 0
        self.dmgHealed = int(statsheet.find('totalhealthhealed').text) if statsheet.find('totalhealthhealed') != None else 0

        self.goldCollected = int(statsheet.find('totalgoldcollected').text) if statsheet.find('totalgoldcollected') != None else 0
        self.itemsCollected = int(statsheet.find('totalitemscollected').text) if statsheet.find('totalitemscollected') != None else 0
        self.totalPurchases = int(statsheet.find('totalpurchases').text) if statsheet.find('totalpurchases') != None else 0
        self.goldPurchases = int(statsheet.find('totalgoldpurchases').text) if statsheet.find('totalgoldpurchases') != None else 0
        self.lunarPurchases = int(statsheet.find('totallunarpurchases').text) if statsheet.find('totallunarpurchases') != None else 0
        self.dronesPurchased = int(statsheet.find('totaldronespurchased').text) if statsheet.find('totaldronespurchased') != None else 0
        self.turretsPurchased = int(statsheet.find('totalturretspurchased').text) if statsheet.find('totalturretspurchased') != None else 0

        for tag in statsheet.find_all(re.compile(r".*totaltimealive\..*")):
            char = tag.name.replace("totaltimealive.", "").replace('body', '')
            self.timeAliveAsCharacter[char] = float(tag.text)

        for tag in statsheet.find_all(re.compile(r".*longestrun\..*")):
            char = tag.name.replace("longestrun.", "").replace('body', '')
            self.longestRunAsCharacter[char] = float(tag.text)

        for tag in statsheet.find_all(re.compile(r".*damagedealtto\..*")):
            char = tag.name.replace("damagedealtto.", "").replace('body', '')
            self.damageDealtTo[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*damagedealtas\..*")):
            char = tag.name.replace("damagedealtas.", "").replace('body', '')
            self.damageDealtAs[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*miniondamagedealtas\..*")):
            char = tag.name.replace("miniondamagedealtas.", "").replace('body', '')
            self.minionDamageDealtAs[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*damagetakenfrom\..*")):
            char = tag.name.replace("damagetakenfrom.", "").replace('body', '')
            self.damageTakenFrom[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*damagetakenas\..*")):
            char = tag.name.replace("damagetakenas.", "").replace('body', '')
            self.damageTakenAs[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*killsagainst\..*")):
            char = tag.name.replace("killsagainst.", "").replace('body', '')
            self.killsAgainst[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*killsagainstelite\..*")):
            char = tag.name.replace("killsagainstelite.", "").replace('body', '')
            self.killsAgainstElite[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*killsas\..*")):
            char = tag.name.replace("killsas.", "").replace('body', '')
            self.killsAs[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*minionkillsas\..*")):
            char = tag.name.replace("minionkillsas.", "").replace('body', '')
            self.minionKillsAs[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*timespicked\..*")):
            char = tag.name.replace("timespicked.", "").replace('body', '')
            self.timesPicked[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*totalcollected\..*")):
            char = tag.name.replace("totalcollected.", "")
            self.totalCollected[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*totaltimeheld\..*")):
            char = tag.name.replace("totaltimeheld.", "")
            self.totalTimeHeld[char] = float(tag.text)

        for tag in statsheet.find_all(re.compile(r".*totaltimesfired\..*")):
            char = tag.name.replace("totaltimesfired.", "")
            self.totalTimesFired[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*totaltimesvisited\..*")):
            char = tag.name.replace("totaltimesvisited.", "")
            self.totalTimesVisited[char] = int(tag.text)

        for tag in statsheet.find_all(re.compile(r".*totaltimescleared\..*")):
            char = tag.name.replace("totaltimescleared.", "")
            self.totalTimesCleared[char] = int(tag.text)

        self.itemAcquisitionOrder = rootTag.find('itemacquisitionorder').text.split(' ')

        logger.debug("Finished parsing player: {}".format(self.name))
