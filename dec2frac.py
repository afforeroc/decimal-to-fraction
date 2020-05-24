# -*- coding: utf-8 -*-

# Libraries
import re
from decimal import Decimal

# Functions
def findType(inputStr):
    if Decimal(inputStr) % 1 != 0:
        num = float(inputStr)
        flag = 'decimal'
    else:
        num = int(float(inputStr))
        flag = 'integer'
    return num, flag

def euclides(num1, num2):
    # Check section
    if (type(num1) != int or type(num2) != int):
        return 'Euclides algorithm only admits integers numbers'
    # Order input numbers
    if num1 > num2:
        a, b = num1, num2
    else:
        a, b = num2, num1
    # Algorithm core
    while b !=0:
        mod = a%b
        a, b = b, mod
    # Output
    mcd = a
    mcm = num1*num2//mcd
    return mcd, mcm

def decimalToFraction(s):
    match = re.search(r'([\w]*).([\w]*)', s)
    if match:
        iPart = match.group(1)  # Integer part
        dPart = match.group(2)  # Decimal part
    a = int(iPart + dPart)
    b = int(pow(10, len(dPart)))
    mcd, _ = euclides(a, b)
    a, b = a//mcd, b//mcd
    return a, b

# Main
if __name__ == "__main__":
    while True:
        try:
            inputStr = input('>> ')
        except EOFError:
            break
        # Really integer number: (+-[D] | +-[D].) | +-[D].[0] | +- .[0]; [D]: set of digits, [0]: set of zeros
        r1 = re.compile('^[+-]?[0-9]+[.]?$|^[+-]?[0-9]+[.][0]*$|^[+-]?[.][0]*$')
        
        # Really float number
        r2 = re.compile('^[+-]?[0-9]*[.][0-9]+$')   # Like decimal +-.X | +-X.X

        if r1.match(inputStr):
            interInput = int(float(inputStr))
            flag = "integer"
            print('input: {} <<{}>>'.format(interInput, flag))
            print('result: {}'.format(interInput))
        elif r2.match(inputStr):
            interInput = float(inputStr)
            flag = "float"
            print('input: {} <<{}>>'.format(interInput, flag))
            a, b = decimalToFraction(inputStr)
            print('result: {}/{}'.format(a, b))
        else:
            print('"{}" is not valid number'.format(inputStr))
