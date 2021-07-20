# -*- coding: utf-8 -*-

"""
runparser.RunParser
~~~~~~~~~~~~

main class lol

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

from bs4 import BeautifulSoup
from pathlib import Path

import os
import logging

from .models.runreport import RunReport
from .models.profile import Profile

logger = logging.getLogger(__name__)


class RunParser():

    def __init__(self, replay_dir: str = None, profile_dir: str = None):
        # reset
        self.clear()

        # handle paths if passed in
        if replay_dir is not None:
            self.set_replay_dir(replay_dir)
        if profile_dir is not None:
            self.set_profile_dir(profile_dir)

    def clear(self):
        self._replayDir: str = None
        self._profileDir: str = None
        self._runList: [str] = []
        self._profileList: [str] = []
        self.runs: [RunReport] = []
        self.profiles: [Profile] = []

    def get_replay_dir(self):
        """Gets the replay directory"""
        return self._replayDir

    def get_profile_dir(self):
        """Gets the replay directory"""
        return self._profileDir

    def set_replay_dir(self, replay_dir: str):
        """Sets the replay directory"""

        # if path is not valid, error. else, set it
        if not os.path.isdir(replay_dir):
            raise Exception("Invalid replay directory! {} does not exist!".format(replay_dir))
        self._replayDir = replay_dir

        # go ahead and log, then find replays in folder
        logger.info("Set replay path to: {}".format(self._replayDir))
        self._runList = self.find_replays()

    def set_profile_dir(self, profile_dir: str):
        """Sets the profile directory"""

        # if path is not valid, error. else, set it
        if not os.path.isdir(profile_dir):
            raise Exception("Invalid profile directory! {} does not exist!".format(profile_dir))
        self._profileDir = profile_dir

        # go ahead and log, then find replays in folder
        logger.info("Set profile path to: {}".format(self._profileDir))
        self._profileList = self.find_profiles()

    def find_replays(self):
        """Finds all replays in _replayDir"""

        # use pathlib to return a list of absolute paths
        r = sorted(Path(self._replayDir).iterdir(), key=os.path.getmtime)
        logger.info("Found {} replays at path {}".format(len(r), self._replayDir))
        return r

    def find_profiles(self):
        """Finds all profiles in _profileDir"""

        # use pathlib to return a list of absolute paths
        p = sorted(Path(self._profileDir).iterdir(), key=os.path.getmtime)
        logger.info("Found {} profiles at path {}".format(len(p), self._profileDir))
        return p

    def parse_runs(self):
        """Attempts to parse all runs in _runList"""

        # iterate over each file, open it,
        # get root tag from bs4, then parse it
        for run_file in self._runList:
            with open(run_file, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
            run = RunReport(soup)
            self.runs.append(run)

    def parse_profiles(self):
        """Attempts to parse all runs in _profileList"""

        # iterate over each file, open it,
        # get root tag from bs4, then parse it
        for profile_file in self._profileList:
            with open(profile_file, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
            profile = Profile(soup)
            self.runs.append(profile)
