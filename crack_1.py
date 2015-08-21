#!/usr/bin/python3
# challenge 1:Convert hex to base64

import base64
import binascii

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

base64_string = ""
for i in range(int(len(hex_string)/2)):
    hex_chars = hex_string[i:i+2]
    base64_string += chr(int(hex_chars,16))
    i += 2

print ("this is the mid-string:")
print (base64_string)

print ("try first way:")
# print (base64.encode(base64_string))
print (base64.b64encode(base64_string.encode(encoding="utf-8")))
print (base64.urlsafe_b64encode(base64_string.encode(encoding="utf-8")))
print (base64.standard_b64encode(base64_string.encode(encoding="utf-8")))
print ("the first way is not right!")

print ("try second way:")
# binary_string = binascii.a2b_uu(base64_string)
# print (base64.b64encode(binary_string))
binary_string = binascii.a2b_hex(hex_string)
print (base64.b64encode(binary_string))
print ("OK,we got the correct answer!")
