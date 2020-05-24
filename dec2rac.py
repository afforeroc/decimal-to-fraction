# -*- coding: utf-8 -*-

# Libraries
import re
from decimal import Decimal
import math

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
    if num1 > num2: a, b = num1, num2
    else: a, b = num2, num1
    # Algorithm core
    while b != 0:
        a, b = b, a%b
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

def mixFraction(a, b):
    c = a//b
    r = a%b
    return c, r

# Main
if __name__ == "__main__":
    while True:
        try:
            inputStr = input('>> ')
        except EOFError:
            break
        # Integer
        r1 = re.compile(' ^[+-]?[0-9]+[.]?$ | ^[+-]?[0-9]*[.][0]+$ ')
        
        # Float number
        r2 = re.compile('^[+-]?[0-9]*[.][0-9]+$')

        # Float number with decimal period
        r3 = re.compile('^[+-]?[0-9]*[.][0-9]*[p][0-9]+$') 

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
            if a>b:
                c, r = mixFraction(a, b)
                print('result: {} + {}/{}'.format(c, r, b))
            else:
                print('result: {}/{}'.format(a, b))
        elif r3.match(inputStr):
            flag = "float with decimal period"
            print(flag)
        else:
            print('"{}" is not valid number'.format(inputStr))
