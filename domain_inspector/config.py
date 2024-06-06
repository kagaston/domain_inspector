"""
config.py

This module provides a clean interface to access configuration values loaded by settings.py. It can implement
additional logic needed to interpret or manipulate these values before returning them.
"""

import os

from domain_inspector.settings import settings


class Config:
    def __init__(self):
        self.database_url = self.get_config_value('DATABASE_URL', 'sqlite:///default_database.db')
        self.secret_key = self.get_config_value('SECRET_KEY', 'defaultsecretkey')
        self.debug = self.get_config_value('DEBUG', 'False')

    @staticmethod
    def get_config_value(key, default=None):
        value = os.getenv(key, None)
        if value is not None:
            return value

        section, option = key.lower().split('_', 1)
        if settings.conf.has_option(section, option):
            return settings.conf.get(section, option)

        return default

    def get_database_url(self):
        return self.database_url

    def get_secret_key(self):
        return self.secret_key

    def get_debug(self):
        return self.debug
