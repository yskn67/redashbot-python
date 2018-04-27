#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from slackbot.bot import respond_to


@respond_to('^\s*<{}/queries/(\d+)#(\d+)>\s*$'.format(os.environ['REDASH_HOST']))
def screenshot(msg, query_id, visual_id):
    query_url = '{}/queries/{}#{}'.format(
        os.environ['REDASH_HOST'],
        query_id,
        visual_id)
    embed_url = '{}/embed/query/{}/visualization/{}?api_key={}'.format(
        os.environ['REDASH_HOST'],
        query_id,
        visual_id,
        os.environ['REDASH_API_KEY'])
    df, fname = tempfile.mkstemp(suffix='.png', dir='/tmp')

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=720,360')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(720, 360)
    driver.get(embed_url)
    sleep(1)
    driver.save_screenshot(fname)
    driver.quit()

    msg.channel.upload_file(query_url, fname)
    os.remove(fname)
