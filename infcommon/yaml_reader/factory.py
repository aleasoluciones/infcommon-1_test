# -*- coding: utf-8 -*-

import os

from infcommon.factory.factory import Factory
from infcommon.yaml_reader.yaml_reader import YamlReader

def yaml_reader(file_conf=None):
    return Factory.instance('config', lambda: YamlReader(file_conf or os.environ['CONF_FILE']))
