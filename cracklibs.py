#!/usr/bin/python3

import base64
import binascii
# decode strings that skipped '='
def safe_base64_decode(s):
    r = len(s)%4
    return base64.b64decode(s if r==0 else s+(4-r)*'=')

# Convert hex to string
def convert_hex_to_base64(hex_string):
    binary_string = binascii.a2b_hex(hex_string)
    return base64.b64encode(binary_string)

# Fixed XOR
def hex_xor(hex_string1,hex_string2):
    int1 = int(hex_string1,16)
    int2 = int(hex_string2,16)
    return hex(int1 ^ int2)[2:]


