#!/usr/bin/python3

import base64

# decode strings that skipped '='
def safe_base64_decode(s):
    r = len(s)%4
    return base64.b64decode(s if r==0 else s+(4-r)*'=')


