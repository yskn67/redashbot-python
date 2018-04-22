#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from slackbot.bot import Bot


def check_env():
    if 'SLACK_BOT_TOKEN' not in os.environ:
        raise ValueError('\'SLACK_BOT_TOKEN\' ENV is required')
    if 'REDASH_HOST' not in os.environ:
        raise ValueError('\'REDASH_HOST\' ENV is required')
    if 'REDASH_API_KEY' not in os.environ:
        raise ValueError('\'REDASH_API_KEY\' ENV is required')


def main():
    check_env()
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
