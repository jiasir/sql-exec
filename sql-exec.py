#!/usr/bin/env python
__author__ = 'Taio'

import os
import sys
import logging
import json
from django.template import Template, Context
from django.conf import settings
import ConfigParser
from utils.noflib import noflib


config_file = ConfigParser.RawConfigParser(allow_no_value=True)
config_file.read('sql-exec.conf')

settings.configure()
logLevel = config_file.get('logging', 'log_level')

logger = logging.getLogger('sql-exec')
logging.basicConfig(filename='sql-exec.log', level=logLevel,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.info('Getting server section config settings ')
serverIp = config_file.get('server', 'ip')
serverUsername = config_file.get('server', 'username')
serverPassword = config_file.get('server', 'password')

logger.info('Getting sql section config settings')
sqlClient = config_file.get('sql', 'client')
sqlLine = config_file.get('sql', 'line')

logger.info('Getting logging section config settings except log_level')
logLocation = config_file('logging', 'log_location')

cmd = noflib()


def check_client():
    pass


def install_mysql_client():
    out = cmd.execute('sudo', 'yum', 'install', 'mysql-client')
    return out


def install_sqlserver_client():
    pass


def execute_mysql():
    out = cmd.execute('mysql', '-h{}', '-u{}', ' -p{}').format(serverIp, serverUsername, serverPassword)
    return out


def execute_sqlserver():
    pass


if __name__ == 'main':
    if sqlClient == 'mysql-client':
        execute_mysql()


