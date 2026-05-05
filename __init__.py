"""
Block Aurral Plugin for Nicotine+

Blocks users whose usernames start with "aurral_"
"""

try:
    from block_aurral import Plugin
except ImportError:
    import sys
    import os

    current_dir = os.path.dirname(__file__)
    sys.path.insert(0, current_dir)

    from block_aurral import Plugin


__version__ = "1.0.0"
__author__ = "Envy"
__description__ = "Automatically block Aurral users from downloading your shares"

__all__ = ["Plugin"]
