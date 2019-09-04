# author: YANG CUI
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0
"""

def addBinary(a, b):
    carryBit = 0
    # add paddings to make them of equal length
    lenOfA = len(a)
    lenOfB = len(b)
    if lenOfA < lenOfB:
        for _ in range(lenOfB - lenOfA):
            a = "0" + a
    else:
        for _ in range(lenOfA - lenOfB):
            b = "0" + b
    print(a)
    print(b)
    # add two binary together
    strOut = ""
    Index = (lenOfA if lenOfA > lenOfB else lenOfB) - 1
    while Index >= 0:
        temp = int(a[Index]) + int(b[Index]) + carryBit
        strOut = str(temp % 2) + strOut
        carryBit = temp // 2
        Index -= 1
    if carryBit == 1:
        strOut = "1" + strOut
    return strOut

# print(addBinary("11", "1"))

