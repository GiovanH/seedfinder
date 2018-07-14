#!/bin/python3

import argparse
import binascii
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--private', type=str, default='./private',
                    help='Path to your sd:/Nintendo/contents/private file. Defaults to ./private')
parser.add_argument('--save', type=str, default='S:/save/8000000000000043',
                    help='Path to your SYSTEMNAND:/save/8000000000000043 file. Defaults to S:/save/8000000000000043')
                    
key_size = 2**4 # 16 bytes

def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))

def hxfmt(b):
    return " ".join(split2len(str(b.upper())[2:-1],2))

args = parser.parse_args()
#private.
with open(args.private,'rb') as private:
    print('Your private file:')
    while True:
        piece = private.read(key_size)
        if piece == b'':
            break # end of file
            #Should only loop once
        privatehex = binascii.hexlify(piece)
    print(privatehex)
    print(hxfmt(privatehex))

#save

with open(args.save,'rb') as save:
    print('\nYour SD seed:')
    jump_size = 16
    piece = privatehex
    while True:
        piece = piece[jump_size:key_size] + save.read(jump_size)
        if piece == b'':
            print('FAIL. Are you sure the files match?')
            break # end of file
        match = binascii.hexlify(piece)
        if match == privatehex:
            sdseed = binascii.hexlify(save.read(key_size))
            print(sdseed)
            print(hxfmt(sdseed))
            break
