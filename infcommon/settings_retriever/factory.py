import os

from infcommon.factory import Factory
from infcommon.settings_retriever.settings_retriever import SettingsRetriever
from infcommon.yaml_reader.yaml_reader import YamlReader


def _config_file(file_name):
    return YamlReader(file_name)


def settings_retriever(config_file_name):
    all_environment_values = dict(os.environ)
    config_file = _config_file(config_file_name)
    return Factory.instance('settings_retriever',
                            lambda: SettingsRetriever(all_environment_values, config_file))
