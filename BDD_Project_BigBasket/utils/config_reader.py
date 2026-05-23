from configparser import ConfigParser


config = ConfigParser()
config.read("config/config.ini")


class ConfigReader:

    @staticmethod
    def get(key):
        return config['DEFAULT'][key]