#!/usr/bin/env python3
import sys
import os

store_dir = '/etc/git.wowee'

# Git, at least for get(x), sends stdin:
#
# protocol=https
# host=github.com
#
# Therefore, we can separate logins, if
# it were ever necessary. :^)
# 
# stdin is accessible through a for loop:
# for x in sys.stdin...
# which will continue until stdin is closed.
# This is something git will do on its own.

def get(x):
	if os.path.exists(store_dir):
		f = open(store_dir, 'r')
		for x in f.readlines():
			print(x, end="")
	exit(0)

def store(x):
	f = open(store_dir, 'w')
	for v in sys.stdin:
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

