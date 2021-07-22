# -*- coding: utf-8 -*-

"""
runparser.models.Stat
~~~~~~~~~~~~

This module implements the class that quantifies item stats/effects

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

import logging

logger = logging.getLogger(__name__)


class Stat():
    """Implements the Stat object."""

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
