"""
settings.py

This module is responsible for loading and managing configuration data, including environment variables
and .conf files. It gathers and organizes configuration data but does not return values or perform business logic.
"""

import os
import sys
import configparser
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        # Determine the base directory (root of the project)
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.module_dir = os.path.join(self.base_dir, 'my_project')
        self.config_file = os.path.join(self.module_dir, 'config.py')

        # Ensure the base directory and module directory are in the PYTHONPATH
        if self.base_dir not in sys.path:
            sys.path.insert(0, self.base_dir)
        if self.module_dir not in sys.path:
            sys.path.insert(0, self.module_dir)

        # Load environment variables from .env file in the project root
        self.load_dotenv()

        # Load configuration from .conf file in the project root
        self.conf = self.load_conf()

    def load_dotenv(self):
        # Path to the .env file in the project root
        env_path = os.path.join(self.base_dir, '.env')
        if os.path.exists(env_path):
            load_dotenv(env_path)
        else:
            print(f"{env_path} not found, skipping .env loading")

    def load_conf(self):
        # Path to the .conf file in the project root
        conf_path = os.path.join(self.base_dir, 'config.conf')
        config = configparser.ConfigParser()
        if os.path.exists(conf_path):
            config.read(conf_path)
            self.substitute_env_variables(config)
        else:
            print(f"{conf_path} not found, skipping .conf loading")
        return config

    def substitute_env_variables(self, config):
        # Substitute environment variables in the .conf file
        for section in config.sections():
            for key, value in config.items(section):
                config.set(section, key, os.path.expandvars(value.replace('${', '{')))


# Instantiate and store settings globally
settings = Settings()
