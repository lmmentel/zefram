
from __future__ import print_function

import argparse
from zefram import framework

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='Three letter framework code')
    args = parser.parse_args()

    if len(args.code) != 3:
        raise ValueError('Framework error should have three letters')
    else:
        fram = framework(args.code.upper())
        fname = fram.code + '.cif'
        with open(fname, 'w') as out:
            out.write(fram.cif)
        print('Wrote to file: {}'.format(fname))

if __name__ == '__main__':
    main()
