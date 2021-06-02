#!/usr/bin/env python3
import sys

def get(x):
	print(x)
	exit(0)

def store(x):
	print(x)
	exit(0)

def erase(x):
	print(x)
	exit(0)

file = 'default_here'
for i in range(0, len(sys.argv), 1):
	if sys.argv[i] == '-f':
		i += 1
		file = open(sys.argv[i], 'r')
	elif sys.argv[i] == 'get':
		get(sys.argv[i:])
		break
	elif sys.argv[i] == 'store':
		store(sys.argv[i:])
		break
	elif sys.argv[i] == 'erase':
		erase(sys.argv[i:])
		break

