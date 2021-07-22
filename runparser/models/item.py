# -*- coding: utf-8 -*-

"""
runparser.models.Item
~~~~~~~~~~~~

This module implements the class that represents each Item.

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

import logging

from ..utils.enums import ItemRarityEnum
from ..db import RunParserDB

logger = logging.getLogger(__name__)


class Item():
    """Implements the Item object."""

    def __init__(self, internal_name: str = None, count: int = None):
        self._reset()
        if internal_name is not None:
            db = RunParserDB()
            item_data = db.get_item(internal_name=internal_name)
            self._parse(item_data)
        self.count = count

    def __eq__(self, other):
        return self.internal_name == other.internal_name

    def _reset(self):
        """Resets the item object."""
        self.id: int = 0
        self.name: str = None
        self.internal_name: str = None
        self.rarity: ItemRarityEnum = ItemRarityEnum.NoTier
        self.categories: [str] = []

        self.quote: str = None
        self.desc: str = None
        self.stats: [self.Stat] = []
        self.unlock: str = None
        self.boss: str = None

        self.count: int = 0

    def _parse(self, item_data: dict):
        """Parses the item data from the db."""
        try:
            # guaranteed data
            self.id = item_data['id']
            self.name = item_data['name']
            self.internal_name = item_data['internal_name']
            self.rarity = ItemRarityEnum(item_data['rarity'])
            self.categories = item_data['category']

            # optional data
            if 'quote' in item_data:
                self.quote = item_data['quote']
            if 'desc' in item_data:
                self.desc = item_data['desc']
            if 'stats' in item_data:
                self.stats = [self.Stat(stat_data) for stat_data in item_data['stats']]
            if 'unlock' in item_data:
                self.unlock = item_data['unlock']
            if 'boss' in item_data:
                self.boss = item_data['boss']

        except KeyError as e:
            raise self.Item_ParseFailure(f"Item data missing key: {e}")

    class Stat():
        """Implements the class that quantifies item stats/effects"""

        def __init__(self, data: dict = None):
            self._reset()
            if data is not None:
                self._parse(data)

        def _reset(self):
            """Resets the Stat object."""
            self.stat: str = 0
            self.value = None
            self.stack: str = None
            self.stack_add = None

        def _parse(self, data: dict):
            """Parses the stat data from the given dict."""
            try:
                self.stat = data['stat']
                self.value = data['value']
                self.stack = data['stack']
                self.stack_add = data['stack_add']
            except KeyError as e:
                raise self.Stat_ParseFailure(f'Missing key: {e}')

        class Stat_ParseFailure(Exception):
            pass

    class Item_ParseFailure(Exception):
        pass
