from pprint import pprint
import requests

from keys import _TELEGRAM_TOKEN

bot_token = _TELEGRAM_TOKEN
url = "<HTTPS_URL>/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())
