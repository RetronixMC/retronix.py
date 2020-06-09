#!/usr/bin/env python

# Retronix Public API Python Library
# Developed by Ben Foster - All Rights Reserved.
"""lib/types.py > Type: Enum class"""

# Imports
from enum import Enum

class Type(Enum):
    """
    Type Enum, passed to respective functions.
    """
    
    CENSOR = 1
    TLD = 2