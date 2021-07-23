# -*- coding: utf-8 -*-

"""
runparser.models.Equipment
~~~~~~~~~~~~

This module implements the class that represents each Equipment.

:copyright: (c) 2021 by Andrew Augustine.
:license: GPL-3.0, see LICENSE for more details.
"""

import logging

from ..utils.enums import EquipmentRarityEnum
from ..db import RunParserDBConn

logger = logging.getLogger(__name__)


class Equipment():
    """Implements the Equipment object."""

    def __init__(self, internal_name: str = None):
        self._reset()
        if internal_name is not None:
            db = RunParserDBConn()
            item_data = db.get_equipment(internal_name=internal_name)
            self._parse(item_data)

    def __eq__(self, other):
        return self.internal_name == other.internal_name

    def _reset(self):
        """Resets the item object."""
        self.id: int = 0
        self.name: str = None
        self.internal_name: str = None
        self.rarity: EquipmentRarityEnum = EquipmentRarityEnum.NoTier

        self.cooldown: int = 0
        self.duration: float = 0
        self.quote: str = None
        self.desc: str = None
        self.unlock: str = None
        self.elite: str = None

    def _parse(self, item_data: dict):
        """Parses the item data from the db."""
        try:
            # guaranteed data
            self.id = item_data['id']
            self.name = item_data['name']
            self.internal_name = item_data['internal_name']
            self.rarity = EquipmentRarityEnum(item_data['rarity'])

            # optional data
            if 'cooldown' in item_data:
                self.cooldown = item_data['cooldown']
            if 'duration' in item_data:
                self.duration = item_data['duration']
            if 'quote' in item_data:
                self.quote = item_data['quote']
            if 'desc' in item_data:
                self.desc = item_data['desc']
            if 'unlock' in item_data:
                self.unlock = item_data['unlock']
            if 'elite' in item_data:
                self.elite = item_data['elite']

        except KeyError as e:
            raise self.Equip_ParseFailure(f"Item data missing key: {e}")

    class Equip_ParseFailure(Exception):
        pass
