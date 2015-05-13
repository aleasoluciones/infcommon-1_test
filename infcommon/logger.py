# -*- coding: utf-8 -*-

import logging
import logging.config
import signal
import os

NOTSET = logging.NOTSET
ERROR = logging.ERROR
INFO = logging.INFO
DEBUG = logging.DEBUG


class _LoggerConfiguration(object):

    def __init__(self, configuration):
        self.configuration = configuration
        self.configuration['version'] = 1
        self.configuration['disable_existing_loggers'] = False

        self._is_debug_enabled = False
        self._logger_levels = self._extract_logger_levels()

    def _extract_logger_levels(self):
        return {logger: configuration.get('level', logging.NOTSET) for logger, configuration in self.configuration.get('loggers', {}).iteritems()}

    @property
    def is_debug_enabled(self):
        return self._is_debug_enabled

    def switch_to_normal_configuration(self):
        self._logger_levels = self._extract_logger_levels()
        for logger, configuration in self.configuration.get('loggers', {}).iteritems():
            configuration.update({'level': logging.INFO})

    def switch_to_debug_configuration(self):
        self._logger_levels = self._extract_logger_levels()
        for logger, configuration in self.configuration.get('loggers', {}).iteritems():
            configuration.update({'level': logging.DEBUG})


class Logger(object):

    def __init__(self, name):
        self._logger = logging.getLogger(name)
        self._logger.addHandler(logging.NullHandler())

    def set_level(self, level):
        self._logger.setLevel(level)

    def error(self, message, *args, **kwargs):
        self._logger.error(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self._logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._logger.info(message, *args, **kwargs)


_logger = Logger('felix')
_logger_configuration = None


def set_logger(logger):
    global _logger
    _logger = logger


def configure(**kwargs):
    global _logger_configuration

    _logger_configuration = _LoggerConfiguration(kwargs)

    logging.config.dictConfig(_logger_configuration.configuration)

def set_level(level):
    global _logger
    _logger.set_level(level)


TEST_MODE_NOT_ENABLED = os.environ.get('TEST_MODE') is None

def info(message, *args, **kwargs):
    _log('info', message, args, kwargs)

def debug(message, *args, **kwargs):
    _log('debug', message, args, kwargs)

def error(message, *args, **kwargs):
    _log('error', message, args, kwargs)

def _log(level, message, args, kwargs):
    if TEST_MODE_NOT_ENABLED:
        getattr(_logger, level)(message, *args, **kwargs)

def activate_debug():
    global _logger_configuration

    _logger_configuration.switch_to_debug_configuration()
    logging.config.dictConfig(_logger_configuration.configuration)
    debug('Activating debug log')

def deactivate_debug():
    global _logger_configuration

    _logger_configuration.switch_to_normal_configuration()
    logging.config.dictConfig(_logger_configuration.configuration)
    info('Deactivating debug log')


signal.signal(signal.SIGUSR1, lambda signal, frame: activate_debug())
signal.signal(signal.SIGUSR2, lambda signal, frame: deactivate_debug())


if not _logger_configuration:
    level = DEBUG if os.environ.get('DEBUG_MODE', 'False').lower() in ['true', 'yes', '1'] else INFO

    configure(
        formatters={'fancy': {'format': 'Pid:%(process)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s'}},
        handlers={'console': {'class': 'logging.StreamHandler', 'formatter': 'fancy'}},
        loggers={
            'felix': {'level': level, 'propagate': 0, 'handlers': ['console']},
        },
        root={'level': level, 'handlers': ['console']}
    )
