# -*- coding: utf-8 -*-

"""
runparser.models.Artifact
~~~~~~~~~~~~

This module implements the class that represents each Artifact.

:copyright: (c) 2021 by Andrew Augustine.
:license: Apache2, see LICENSE for more details.
"""

import logging

from ..db import RunParserDB

logger = logging.getLogger(__name__)


class Artifact():
    """Implements the Artifact object."""

    def __init__(self, internal_name: str = None):
        self._reset()
        if internal_name is not None:
            db = RunParserDB()
            artifact_data = db.get_artifact(internal_name=internal_name)
            self._parse(artifact_data)

    def __eq__(self, other):
        return self.internal_name == other.internal_name

    def _reset(self):
        """Resets the item object."""
        self.name: str = None
        self.internal_name: str = None
        self.short_name: str = None
        self.desc: str = None

    def _parse(self, artifact_data: dict):
        """Parses the item data from the db."""
        try:
            self.name = artifact_data['name']
            self.internal_name = artifact_data['internal_name']
            self.short_name = artifact_data['short_name']
            self.desc = artifact_data['desc']

        except KeyError as e:
            raise self.Artifact_ParseFailure(f"Item data missing key: {e}")

    class Artifact_ParseFailure(Exception):
        pass
