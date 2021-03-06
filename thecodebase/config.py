
import os
import json
import logging

logger = logging.getLogger(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

CONFIG = {}

def cache_config():
    with open(CONFIG_PATH) as f:
        print("Config cached from %s" % CONFIG_PATH)
        CONFIG.update(json.load(f))

if os.path.isfile(CONFIG_PATH):
    cache_config()
else:
    print("Config missing, website not operational")
