# -*- coding: utf-8 -*-

"""
runparser.AutoRunParser
~~~~~~~~~~~~

implements the runparser with functions to automatically find and parse data.

inherits from runparser.RunParser

:copyright: (c) 2021 by Andrew Augustine.
:license: GPL-3.0, see LICENSE for more details.
"""

import os
if os.name == 'nt':
    import winreg
import logging

from . import RunParser

logger = logging.getLogger(__name__)


class AutoRunParser(RunParser):

    def __init__(self):
        # run the super class constructor
        super(AutoRunParser, self).__init__()

        # make sure we're on windows
        if os.name != 'nt':
            raise Exception("Unable to run on non-Windows OS!\nEnsure you are running this on Windows.")

        # try to find replays/profiles
        self.set_replay_dir(self.locate_replays())
        self.set_profile_dir(self.locate_profiles())

    def locate_steam(self):
        """Attempts to find steam's install path via the registry."""

        logger.info("Attempting to find Steam installation path via registry...")
        if winreg is not None:
            try:
                winReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                key = winreg.OpenKey(winReg, r'SOFTWARE\WOW6432Node\Valve\Steam')
                install_path = winreg.QueryValueEx(key, 'InstallPath')[0]
                key.Close()
                winReg.Close()
                return install_path
            except BaseException:
                raise Exception("Unable to find Steam Installation via Registry!")
        else:
            raise Exception("Unable to connect to Windows Registry! Winreg does not exist. Are you on Windows?")

    def locate_replays(self):
        """Attempts to find all replays in default location"""

        # log our attempt
        logger.info("Attempting to find all replays in default location...")

        # if windows, attempt to find the replays using registry
        if os.name == 'nt':
            steam_dir = self.locate_steam()
            replay_dir = os.path.join(steam_dir, 'steamapps\\common\\Risk of Rain 2\\Risk of Rain 2_Data\\RunReports\\History')
        else:
            raise Exception("Unable to run on non-Windows OS!\nEnsure you are running this on Windows.")

        # return replay dir
        return replay_dir

    def locate_profiles(self):
        """Attempts to find all profiles in default location"""

        # log our attempt
        logger.info("Attempting to find all profiles in default location...")

        # if windows, attempt to find the install using registry
        if os.name == 'nt':
            steam_dir = self.locate_steam()
            userdata_dir = os.path.join(steam_dir, 'userdata\\')

            # ok so within here the data is stored in a folder that is named after a random user id.
            # i have no idea how to get that id in code, so we iterate through all the folders in
            # the userdata folder, see if the path patern exists, and return the first valid path.
            # the users can use set_profile_folder(path) to add more if they want, idc

            # iterate through user ids
            userid_list = os.listdir(userdata_dir)
            for user_id in userid_list:
                try:
                    profile_dir = os.path.join(userdata_dir, user_id, '632360\\remote\\UserProfiles')
                    if os.path.isdir(profile_dir):
                        return profile_dir
                except BaseException:
                    pass

            # if we get here, we didn't find a valid path
            raise Exception(
                "Unable to find any user profiles folder!\n\
                Manually pass it in using the set_profile_dir(path) function."
            )
        else:
            raise Exception("Unable to run on non-Windows OS!\nEnsure you are running this on Windows.")
