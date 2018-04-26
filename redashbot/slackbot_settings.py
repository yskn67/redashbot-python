#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os


API_TOKEN = os.environ['SLACK_BOT_TOKEN']
DEFAULT_REPLY = 'Usage: @redashbot {}/queries/<query-number>#<visualization-number>'.format(os.environ['REDASH_HOST'])
PLUGINS = [
    'plugins'
]
