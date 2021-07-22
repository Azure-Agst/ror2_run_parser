# -*- coding: utf-8 -*-

"""
runparser.models.Survivor
~~~~~~~~~~~~

This module implements the class that represents each Survivor.

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

import logging

from ..db import RunParserDB

logger = logging.getLogger(__name__)


class Survivor():
    """Implements the Survivor object."""

    def __init__(self, internal_name: str = None):
        self._reset()
        if internal_name is not None:
            db = RunParserDB()
            survivor_data = db.get_survivor(internal_name=internal_name)
            self._parse(survivor_data)

    def __eq__(self, other):
        return self.internal_name == other.internal_name

    def _reset(self):
        """Resets the item object."""
        self.name: str = None
        self.internal_name: str = None
        self.skill_prefix: str = None
        self.desc: str = None

    def _parse(self, survivor_data: dict):
        """Parses the item data from the db."""
        try:
            self.name = survivor_data['name']
            self.internal_name = survivor_data['internal_name']
            self.skill_prefix = survivor_data['skill_prefix']
            self.desc = survivor_data['desc']

        except KeyError as e:
            raise self.Survivor_ParseFailure(f"Item data missing key: {e}")

    class Survivor_ParseFailure(Exception):
        pass
