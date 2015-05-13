# -*- coding: utf-8 -*-

import os
import socket

class AttributesComparison(object):

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "%s %s" % (self.__class_name_without_module(), self.__dict__)

    def __hash__(self):
        return hash(str(self))

    def __class_name_without_module(self):
        return self.__class__.__name__.split('.')[-1]


class Factory(object):
    _instances = {}

    @classmethod
    def instance(cls, id, create_instance):
        if id not in cls._instances:
            cls._instances[id] = create_instance()

        return cls._instances[id]


def extract_package(path):
    return os.path.split(os.path.dirname(path))[-1]

def local_net_name():
    net_name_from_hostname = socket.gethostname().split('-')[0]
    return os.environ.get('LOCAL_NETWORK', net_name_from_hostname)

