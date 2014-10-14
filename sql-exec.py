#!/usr/bin/env python
__author__ = 'Taio'

import os
import sys
import logging
import json
from django.template import Template, Context
from django.conf import settings
import ConfigParser

config_file = ConfigParser.RawConfigParser(allow_no_value=True)
config_file.read('sql-exec.conf')

settings.configure()





