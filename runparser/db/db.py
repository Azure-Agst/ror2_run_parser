# -*- coding: utf-8 -*-

"""
runparser.db.RunParserDB
~~~~~~~~~~~~

uses tinydb to get data on entries in the game

:copyright: (c) 2021 by Andrew Augustine.
:license: GPL-3.0, see LICENSE for more details.
"""

from tinydb import TinyDB, Query

import os
import re


class RunParserDB():
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "db.json")
        self.db = TinyDB(self.path, sort_keys=True, indent=4, separators=(',', ': '))

    def __del__(self):
        self.db.close()

    def get_item(self, internal_name: str = None, name: str = None):
        table = self.db.table('items')
        Item = Query()

        # if internal_name is passed in
        if internal_name is not None:
            res = table.search(Item.internal_name.matches(internal_name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Item with internal_name '{internal_name}' does not exist in database.")

        # else, if name is passed in
        elif name is not None:
            res = table.search(Item.name.matches(name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Item with name '{name}' does not exist in database.")

        # else, throw error
        else:
            raise self.RPDB_ArgumentError("Either 'internal_name' or 'name' must be passed in.")

        return res[0]

    def get_equipment(self, internal_name: str = None, name: str = None):
        table = self.db.table('equipment')
        Equipment = Query()

        # if internal_name is passed in
        if internal_name is not None:
            res = table.search(Equipment.internal_name.matches(internal_name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Equipment with internal_name '{internal_name}' does not exist in database.")

        # else, if name is passed in
        elif name is not None:
            res = table.search(Equipment.name.matches(name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Equipment with name '{name}' does not exist in database.")

        # else, throw error
        else:
            raise self.RPDB_ArgumentError("Either 'internal_name' or 'name' must be passed in.")

        return res[0]

    def get_artifact(self, internal_name: str = None, name: str = None):
        table = self.db.table('artifacts')
        Artifact = Query()

        # if internal_name is passed in
        if internal_name is not None:
            res = table.search(Artifact.internal_name.matches(internal_name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Artifact with internal_name '{internal_name}' does not exist in database.")

        # else, if name is passed in
        elif name is not None:
            res = table.search(Artifact.name.matches(name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Artifact with name '{name}' does not exist in database.")

        # else, throw error
        else:
            raise self.RPDB_ArgumentError("Either 'internal_name' or 'name' must be passed in.")

        return res[0]

    def get_survivor(self, internal_name: str = None, name: str = None):
        table = self.db.table('survivors')
        Survivor = Query()

        # if internal_name is passed in
        if internal_name is not None:
            res = table.search(Survivor.internal_name.matches(internal_name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Survivor with internal_name '{internal_name}' does not exist in database.")

        # else, if name is passed in
        elif name is not None:
            res = table.search(Survivor.name.matches(name, flags=re.IGNORECASE))
            if len(res) == 0:
                raise self.RPDB_EntryNotFoundError(f"Survivor with name '{name}' does not exist in database.")

        # else, throw error
        else:
            raise self.RPDB_ArgumentError("Either 'internal_name' or 'name' must be passed in.")

        return res[0]

    class RPDB_EntryNotFoundError(Exception):
        pass

    class RPDB_ArgumentError(Exception):
        pass
