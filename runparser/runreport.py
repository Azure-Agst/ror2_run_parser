# -*- coding: utf-8 -*-

"""
runparser.runreport
~~~~~~~~~~~~

This module implements the class that to parses each run.

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

from bs4 import BeautifulSoup, Tag
from pathlib import Path

import logging

from .player import Player

logger = logging.getLogger(__name__)

class RunReport():
    """This class parses the run report."""

    version : int = 0
    guid : str = None
    gamemode : str = None
    ending : str = None
    seed : int = 0
    start_timestamp : int = 0
    end_timestamp : int = 0
    total_time : float = 0.0
    run_time : float = 0.0
    artifacts : list = []
    enabled_items : list = []
    disabled_items : list = []
    enabled_equipment : list = []
    disabled_equipment : list = []
    players : list = []
    misc : dict = {}


    def __init__(self, fileRoot: Tag = None):
        self.reset()
        self._fileRoot = fileRoot
        if self._fileRoot is not None:
            self.parse(self._fileRoot)
    

    def reset(self):
        self.version : int = 0
        self.guid : str = None
        self.gamemode : str = None
        self.ending : str = None
        self.seed : int = 0
        self.start_timestamp : int = 0
        self.end_timestamp : int = 0
        self.total_time : float = 0.0
        self.run_time : float = 0.0
        self.artifacts : list = []
        self.enabled_items : list = []
        self.disabled_items : list = []
        self.enabled_equipment : list = []
        self.disabled_equipment : list = []
        self.players : list = []
        self.misc : dict = {}

    
    def parse(self, rootTag: Tag):
        """Parses the run report."""

        # log the start
        logger.debug("Parsing run report...")

        # parse run metadata
        runreport = rootTag.find('runreport')
        self.version = int(runreport.find('version').text)
        self.guid = runreport.find('runguid').text
        self.gamemode = runreport.find('gamemodename').text
        self.ending = runreport.find('gameending').text
        self.seed = int(runreport.find('seed').text)
        self.start_timestamp = int(runreport.find('runstarttimeutc').text)
        self.end_timestamp = int(runreport.find('snapshottimeutc').text)
        self.total_time = float(runreport.find('snapshotruntime').text)
        self.run_time = float(runreport.find('runstopwatchvalue').text)

        # parse rules
        rule_list = runreport.find('rulebook').text.split(" ")
        for rule in rule_list:
            rule_arr = rule.split('.')
            if rule_arr[0] == "Difficulty":
                self.difficulty = rule_arr[1]
            if rule_arr[0] == "Artifacts" and rule_arr[2] == "On":
                self.artifacts.append(rule_arr[1])
            if rule_arr[0] == "Items":
                if rule_arr[2] == "On":
                    self.enabled_items.append(rule_arr[1])
                else:
                    self.disabled_items.append(rule_arr[1])
            if rule_arr[0] == "Equipment":
                if rule_arr[2] == "On":
                    self.enabled_equipment.append(rule_arr[1])
                else:
                    self.disabled_equipment.append(rule_arr[1])
            if rule_arr[0] == "Misc":
                self.misc[rule_arr[1]] = rule_arr[2]
        
        # loop over each player
        self.players = []
        player_list = runreport.find('playerinfos').find_all('playerinfo')
        for player_data in player_list:
            self.players.append(Player(player_data))

        logger.debug("Finished parsing run report: {}".format(self.guid))


            
