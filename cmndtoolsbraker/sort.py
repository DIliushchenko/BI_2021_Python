#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description='Count words, lines or bytes in file')
parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()

data = []
for line in args.input_file:
	data.append(line)

data.sort()
for line in data:
	sys.stdout.write(line)
