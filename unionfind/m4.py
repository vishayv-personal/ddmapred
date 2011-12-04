#!/usr/bin/env python

import sys

"""
Final clustering
----------------
Input: (n M a b)
Action: Key = M, Value = n
		Emit(Key,Value)
Output: (M \t n)
"""

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if (line == 'nextround'):
		continue
	wlist = []
	wlist = line.split()
	wlist = [int(x) for x in wlist]
	print '%d\t%d' %(wlist[1],wlist[0])
