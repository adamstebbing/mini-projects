#!/usr/bin/env python3

'''
Hexdump Tool
by Adam Stebbing
2/5/2019

Hexdump program built for Python3, built by myself with some help from StackOverflow, took me longer than I'd like to admit
'''
import sys
import argparse
from binascii import unhexlify, hexlify

def dump(stdInput, length=16, seperator='.'):
    output = []
    for chunk in range(0, len(stdInput), length):
        temp = stdInput[chunk:chunk+length]
        hx = ''
        isMiddle = False
        for i in range(0, len(temp)):
            if i == length/2:
                hx += ' '
            i = temp[i]
            if not isinstance(i, int):
                i = ord(i)
            i = hex(i).replace('0x','')
            if len(i) == 1:
                i = '0' + i
            hx += i + ' '
        hx = hx.strip(' ')
        text = ''
        for c in temp:
            if not isinstance(c, int):
                c = ord(c)
            if 0x20 <= c < 0x7F:
                text += chr(c)
            else:
                text += seperator
        output.append(('%08X: %-' + str(length*(3)+1)+'s |%s|') % (chunk, hx, text))
    return '\n'.join(output)

def main():
    p = argparse.ArgumentParser(description="Dump the input as hexadecimal.")
    p.add_argument("file", action='store', type=str, help="The name of the file to be examined.")
    p.add_argument("-i", "--input", action='store_true', help="Add this flag to directly dump input, please input string between quotes.")
    args = p.parse_args()
    
    with open(args.file, 'rb') as f:
        stdInput = f.read()
        
    print("\n" + dump(stdInput))

main()
