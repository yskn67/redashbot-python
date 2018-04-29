# Slack Bot for re:dash

This is slack bot for [re:dash](https://redash.io).
This project is inspired by https://github.com/hakobera/redashbot

## Difference

- Writen in python.
- Use headless Chrome.
  - re:dash v4.0.0 use ES6.
  - PhantomJS can't render ES6.

## Environment variables

### SLACK_BOT_TOKEN (required)

Slack's Bot User Token

### REDASH_HOST (required)

Re:dash's URL.

### REDASH_API_KEY (optional)

Re:dash's API Key.

## How to start

```
docker build -t redashbot .
docker run --restart=always -d -e SLACK_BOT_TOKEN="" -e REDASH_HOST="" -e REDASH_API_KEY="" redashbot:latest
```
