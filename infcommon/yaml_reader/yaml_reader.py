# -*- coding: utf-8 -*-

import yaml

from infcommon.info_container.info_container import InfoContainer


class YamlReader(object):

    def __init__(self, path):
        self._path = path

    def get(self, key):
        return self._load_file().get(key)

    def get_info_container(self):
        return InfoContainer(self._load_file(), return_none=True)

    def __getitem__(self, key):
        return self._load_file()[key]

    def _load_file(self):
        with open(self._path) as f:
            return yaml.load(f)
