# SPDX-License-Identifier: AGPL-3.0-or-later
# Part of Parking (PublicStack).
"""Sample task. Replace with real Parking work."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def echo(message: str) -> str:
    """Trivial task — logs and returns its input. Used by smoke tests."""
    logger.info("echo task: %s", message)
    return message
