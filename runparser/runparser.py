# -*- coding: utf-8 -*-

"""
runparser.runparser
~~~~~~~~~~~~

main class lol

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

from bs4 import BeautifulSoup
from pathlib import Path

import os
import sys
import configparser
import winreg
import logging

from .models.runreport import RunReport
from .models.player import Player

logger = logging.getLogger(__name__)

class RunParser():

    steamDir : str = "C:\\Program Files (x86)\\Steam"
    gameDir : str = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Risk of Rain 2"
    replayDir : str = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Risk of Rain 2\\Risk of Rain 2_Data\\RunReports\\History"
    profileDir : str = "C:\\Program Files (x86)\\Steam\\userdata\\999999999\\632360\\remote\\UserProfiles"
    winReg = None
    runList : [ str ] = []
    profileList : [ str ] = []
    parsedRuns : { str : RunReport } = {}
    parsedProfiles : { str : str } = {}


    def __init__(self, steam_dir: str = None):

        # try to locate steam installation
        # is path is provided, use it. otherwise, try to find it ourselves.
        if steam_dir != None:
            logger.info("Steam install specified, validating...")
            self.steamDir = steam_dir
            if not os.path.isdir(self.steamDir) or os.path.exists(os.path.join(self.steamDir, 'steam.exe')):
                raise Exception("Unable to find Steam Installation!\nEnsure steam_dir variable passed to RunParser() is correct.")
        else:
            logger.warning("Steam install path not specified, attempting to find...")
            self.steamDir = self.find_steam()
        logger.info("Steam install located at path \"{}\"!".format(self.steamDir))

        # try to locate replay folder
        found_replays = self.find_replays()
        logger.info("Found {} replays!".format(found_replays))

        # try to find profiles
        found_profiles = self.find_profiles()
        logger.info("Found {} profiles!".format(found_profiles))


    def __del__(self):
        if self.winReg is not None:
            self.winReg.Close()

    
    def find_steam(self):
        try:
            # get connection to registry
            self.winReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

            # find steam install path
            key = winreg.OpenKey(self.winReg, r'SOFTWARE\WOW6432Node\Valve\Steam')
            install_path = winreg.QueryValueEx(key, 'InstallPath')[0]
            key.Close()

            # return path to steam
            return install_path
        
        except BaseException as e:
                raise Exception("Unable to find Steam Installation!\nPlease pass steam_dir variable to RunParser().")


    def find_replays(self):
        try:
            # set game and replay directories
            self.gameDir = os.path.join(self.steamDir + '\\steamapps\\common\\Risk of Rain 2')
            self.replayDir = os.path.join(self.gameDir + '\\Risk of Rain 2_Data\\RunReports\\History')

            # attempt to access saves in that location
            self.runList = sorted(Path(self.replayDir).iterdir(), key=os.path.getmtime)

            # return number of runs found
            return len(self.runList)
        
        except BaseException as e:
            raise Exception("Unable to find replay folder?")


    def find_profiles(self):
        try:
            # find steam userdata directory
            userdata = os.path.join(self.steamDir + '\\userdata')

            # list all user folders in there
            all_users = os.listdir(userdata)

            # iterate through each user, and see if profile folder exists.
            # if user has a profile folder, add contents to the list.
            for user in all_users:
                try:
                    profile_path = os.path.join(userdata, user, "632360\\remote\\UserProfiles")
                    self.profileList += sorted(Path(profile_path).iterdir(), key=os.path.getmtime)
                except BaseException as e:
                    continue

            # return number of profiles found
            return len(self.profileList)

        except BaseException as e:
            raise Exception("Unable to find RoR2 profile folder?")


    def parse_runs(self, count : int = 10):
        """parses latest numbers of runs. default = 10"""

        if self.parsedRuns != None:
            self.parsedRuns.clear()

        for item in self.runList[-count:]:
            with open(item, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
            run = RunReport(soup)
            self.parsedRuns[run.guid] = run