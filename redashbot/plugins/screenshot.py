#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from slackbot.bot import import respond_to


@respond_to('^\s*({}/queries/\d+#\d+)\s*$'.format(os.environ['REDASH_HOST']))
def screenshot(msg):
    pass
