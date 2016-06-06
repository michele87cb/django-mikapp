# coding=utf-8
# ---------------------------------------------------------------
# Project: mikapp
# Date   : 01/06/2016 11:57
# Author : MikeWil
# Source : pages_lib.py
# ---------------------------------------------------------------
# MICHELE GUGLIELMI
# ---------------------------------------------------------------
import json
from _libs import _paths


def load_request(request):
    request.m_config = Config()


class Config(object):

    def __init__(self):
        self.prefs = Preferences()


class Preferences(object):
    def __init__(self):
        dizPref = load_pref()
        self.jsConfirmTheme = dizPref['jsConfirmTheme']
        self.forceLogin = True if dizPref['forceLogin'] in ['True', 'true'] else False

def load_pref():
    pref = {}
    try:
        json_file = open(_paths._cnfdir + 'preferences.json')
        json_data = json_file.read()
        pref = json.loads(json_data)
        json_file.close()
    except Exception:
        pass
    return pref