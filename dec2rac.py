# -*- coding: utf-8 -*-

# Libraries
import re
from decimal import Decimal
import math

# Regular expretions to detect type of numbers
r1 = re.compile('^[+-]?[0-9]+[.]?$|^[+-]?[0-9]*[.][0]+$') # Integer
r2 = re.compile('^[+-]?[0-9]*[.][0-9]+$') # Float number
r3 = re.compile('^[+-]?[0-9]*[.][p][0]+$') # Integer with decimal period [0]+
r4 = re.compile('^[+-]?[0-9]*[.][0-9]*[p][0-9]+$') # Float number with explicit decimal period

# Functions
def findType(inputStr):
    if Decimal(inputStr) % 1 != 0:
        num = float(inputStr)
        flag = 'decimal'
    else:
        num = int(float(inputStr))
        flag = 'integer'
    return num, flag

def interpreterNum(inputStr):
    if r1.match(inputStr):
        interFlag = "integer"
        interNum = int(float(inputStr))
    elif r2.match(inputStr): # Float
        interFlag = "float"
        interNum = float(inputStr)
    elif r3.match(inputStr) or r4.match(inputStr):
        match = re.search(r'([\w]*).([\w]*)p([\w]*)', inputStr)
        iPart = match.group(1)  # Integer part
        dPart = match.group(2)  # Decimal no period part
        dpPart = match.group(3)  # Decimal period part
        interStrExtra = iPart+'.'+dPart+dpPart

        if int(dPart+dpPart) == 0:
            interFlag = "integer"
            interNum = int(float(interStrExtra))
        elif int(dpPart) == 0:
            interFlag = "float"
            interNum = float(interStrExtra)
        else:
            interFlag = "float with decimal period"
            interNum = str(interStrExtra)+5*dpPart+'...'

    interOutput = 'input: {} <<{}>>'.format(interNum, interFlag)
    
    return interOutput

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
        
        if r1.match(inputStr) or r2.match(inputStr) or r3.match(inputStr) or r4.match(inputStr): #Valid entry
            print(interpreterNum(inputStr))
        else:
            print('"{}" is not valid number'.format(inputStr))
