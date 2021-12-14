#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description='Count words, lines or bytes in file')
parser.add_argument('-l', dest='lines', default=False, action = 'store_true', help='count lines')
parser.add_argument('-w', dest='words', default=False, action = 'store_true', help='count words')
parser.add_argument('-c', dest='bytes', default=False, action = 'store_true', help='count bytes')
parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()

res = [0,0,0]

for line in args.input_file:
		
		res[0] += 1
		res[1] += len(line.split())
		res[2] += sys.getsizeof(line)


if not args.lines and not args.words and not args.bytes:
	print(' '.join(str(x) for x in res))
if args.lines:
	print(res[0], 'lines')
if args.words:
	print(res[1], 'words')
if args.bytes:
	print(res[2], 'bytes')
