# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
from zefram import framework

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='Three letter framework code')
    parser.add_argument('-f', help='Full information')
    args = parser.parse_args()

    if len(args.code) != 3:
        raise ValueError('Framework error should have three letters')
    else:
        f = framework(args.code.upper())
        
        code = f.code.center(50, '=') + '\n'

        cell = '\n'.join([
            'Cell parameters',
            '\ta={a:7.3f} Å  b={b:7.3f} Å  c={c:7.3f} Å'.format(a=f.a, b=f.b, c=f.c),
            '\tα={a:7.3f} °  β={b:7.3f} °  γ={c:7.3f} °'.format(a=f.alpha, b=f.beta, c=f.gamma),
            ])

        print(code, cell, sep='\n')

if __name__ == '__main__':
    main()
