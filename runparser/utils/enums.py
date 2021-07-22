# -*- coding: utf-8 -*-

"""
runparser.enums.*
~~~~~~~~~~~~

all of the enumerations the library uses

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

from enum import Enum


class ItemRarityEnum(int, Enum):
    NoTier = 0
    Common = 1
    Uncommon = 2
    Legendary = 3
    Boss = 4
    Lunar = 5


class EquipmentRarityEnum(int, Enum):
    NoTier = 0
    Standard = 1
    Lunar = 2
    Elite = 3
