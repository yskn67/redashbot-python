#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os


API_TOKEN = os.environ['SLACK_API_TOKEN']
DEFAULT_REPLY = 'Usage: @redashbot https://{}/queries/<query-number>#<visualization-number>'.format(os.environ['REDASH_HOST'])
PLUGINS = [
    'plugins'
]
