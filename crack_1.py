#!/usr/bin/python3

import base64

# decode strings that skipped '='
def safe_base64_decode(s):
    r = len(s)%4
    return base64.b64decode(s if r==0 else s+(4-r)*'=')

# Convert hex to string
def convert_hex_to_base64(hex_string):
    base64_string = ""
    for i in range(int(len(hex_string)/2)):
        hae_chars = hex_string[i:i+2]
        base64_string += chr(int(hex_chars,16))
        i += 2
    return base64.b64encode(base64_string.encode(encoding="utf-8"))
    

