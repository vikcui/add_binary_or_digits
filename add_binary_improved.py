# author: YANG CUI
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0
"""

def addBinary(a, b):
    result = bin(int(a,2) + int(b,2))
    return result[2:]

print(addBinary("11",'1'))
