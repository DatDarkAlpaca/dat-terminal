import configparser
import os.path
from dataclasses import dataclass

from .utils.string_utils import convert_to_bool


@dataclass
class ConfigResponse:
    response: str = ''

    def as_bool(self) -> bool:
        return convert_to_bool(self.response)


class NullResponse(ConfigResponse):
    response = '<null>'


class ConfigHandler:
    config_file_path = './config.ini'

    @staticmethod
    def initialize():
        if not os.path.isfile(ConfigHandler.config_file_path):
            ConfigHandler._create_default_config_file()

    @staticmethod
    def _create_default_config_file():
        config = configparser.ConfigParser()

        config['General'] = {
            'PREFIX': '>',
            'PRIMARY_COLOR': 'white',
            'SECONDARY_COLOR': 'blue',
            'WARNING_COLOR': 'yellow',
            'ERROR_COLOR': 'red'
        }

        with open(ConfigHandler.config_file_path, mode='w') as configfile:
            config.write(configfile)

    @staticmethod
    def get(section_name: str, entry: str) -> ConfigResponse:
        config = configparser.ConfigParser()
        config.read(ConfigHandler.config_file_path)

        try:
            value = config[section_name][entry]
            return ConfigResponse(response=value)

        except KeyError:
            # Todo: use the logger to display the error.
            print('Fatal: invalid section name or entry.')

        return NullResponse()

    @staticmethod
    def set(section_name: str, entry: str, value: str) -> None:
        config = configparser.ConfigParser()
        config.read(ConfigHandler.config_file_path)
        config.set(section_name, entry, value)

        with open(ConfigHandler.config_file_path, mode='w') as configfile:
            config.write(configfile)

    @staticmethod
    def general(entry: str) -> ConfigResponse:
        return ConfigHandler.get('General', entry)
