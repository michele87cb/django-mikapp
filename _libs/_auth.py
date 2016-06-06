# coding=utf-8
# ---------------------------------------------------------------
# Project: mikapp
# Date   : 01/06/2016 09:57
# Author : MikeWil
# Source : _auth.py
# ---------------------------------------------------------------
# MICHELE GUGLIELMI
# ---------------------------------------------------------------
import hashlib
from Crypto.Cipher import AES
import base64
import os
cr_ky = hashlib.sha256(os.urandom(32)).digest()[:16]


def sha256(val):
    try:
        val = val.encode('utf-8')
        val = hashlib.sha256(val)
        return val.hexdigest()
    except Exception:
        return ''


def crypt(val):
    secret_key = cr_ky
    cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
    return base64.b64encode(cipher.encrypt(val.rjust(32))).strip()


def decrypt(val, decode_type='utf-8'):
    secret_key = cr_ky
    cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
    return cipher.decrypt(base64.b64decode(val.rjust(32))).decode(decode_type).strip()


def check_login(usr, pwd):
    if usr == 'admin' and sha256(pwd) == '9067ce5de92f8016c1e769108b06d21b94b2c80333424fa50e22a4870815ed56':
        return True
    return False