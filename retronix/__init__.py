#!/usr/bin/env python

# Retronix Public API Python Library
# Developed by Ben Foster - All Rights Reserved.
"""__init__.py > Library Entrypoint"""

# Copyright and Metadata Smeg
__author__ = "Ben Foster"
__copyright__ = "Copyright 2020, Retronix"
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Ben Foster"
__email__ = "ben@retronixmc.org"
__status__ = "Development"

# Imports would go here
#import asyncio


class Client:
    """
    Retronix API Client

    Attributes:
        censor (list): Censored words list
        tld (list): List of censored Top Level Domains
    """

    def __init__(self, subs:dict=None):
        """
        Initialise a new instance of the Retronix Client.

        Store this as a variable for use as this is what you'll need to interact with the API.

        Parameters:
            subs (dict): (Optional) Dictionary of subscriptions to initialise
        """
        print("Hello World")
    def get(self, op):
        """
        Query API for up-to-date contents of specified list

        Will also update the variables in the process

        Parameters:
            op (Type): (Required) Type of list to query from API

        Returns:
            list: Raw return content from API
        """
        return []