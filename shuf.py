#!/usr/local/cs/bin/python3

import sys
import argparse
import random

def parse_input_range(r):
    try:
        start, end = map(int, r.split('-'))
        if start > end:
            raise ValueError
        return list(map(str, range(start, end + 1)))
    except:
        raise argparse.ArgumentTypeError("Invalid input range")

def main():
    parser = argparse.ArgumentParser(description='Python version of shuf')
    parser.add_argument('-e', '--echo', action='store_true', help='treat each ARG as an input line')
    parser.add_argument('-i', '--input-range', type=parse_input_range, help='treat range LO-HI as input lines')
    parser.add_argument('-n', '--head-count', type=int, help='output at most COUNT lines')
    parser.add_argument('-r', '--repeat', action='store_true', help='output lines can be repeated')
    parser.add_argument('files', nargs='*', help='input file or - for stdin')

    args = parser.parse_args()

    if args.echo and args.input_range:
        parser.error('cannot combine --echo and --input-range')

    if args.echo:
        lines = args.files
    elif args.input_range:
        lines = args.input_range
    else:
        input_file = None
        if not args.files or args.files == ['-']:
            input_file = sys.stdin
        elif len(args.files) == 1:
            input_file = open(args.files[0])
        else:
            parser.error("extra operand(s): %s" % ' '.join(args.files))

        with input_file:
            lines = input_file.read().splitlines()

    if args.repeat:
        if args.head_count is None:
            while True:
                print(random.choice(lines))
        else:
            for _ in range(args.head_count):
                print(random.choice(lines))
    else:
        random.shuffle(lines)
        output = lines if args.head_count is None else lines[:args.head_count]
        for line in output:
            print(line)

if __name__ == '__main__':
    main()
