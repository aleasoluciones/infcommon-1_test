# -*- coding: utf-8 -*-

from infcommon.factory import Factory
from infcommon.yaml_reader.yaml_reader import YamlReader


def yaml_reader(path=None):
    return Factory.instance('yaml_reader', lambda: YamlReader(path))
