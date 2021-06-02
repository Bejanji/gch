#!/usr/bin/env python3
import sys
import os

store_dir = '/etc/git.wowee'

def get(x):
	if os.path.exists(store_dir):
		f = open(store_dir, 'r')
		for x in f.readlines():
			print(x, end="")
	exit(0)

def store(x):
	f = open(store_dir, 'w')
	for v in sys.stdin:
		if v.strip() == '':
			continue
		f.write(v)
	f.flush()
	f.close()
	exit(0)

def erase(x):
	os.remove(store_dir)
	exit(0)

for i in range(0, len(sys.argv), 1):
	if sys.argv[i] == '-f':
		i += 1
		store_dir = sys.argv[i]
	elif sys.argv[i] == 'get':
		get(sys.argv[i:])
		break
	elif sys.argv[i] == 'store':
		store(sys.argv[i:])
		break
	elif sys.argv[i] == 'erase':
		erase(sys.argv[i:])
		break

