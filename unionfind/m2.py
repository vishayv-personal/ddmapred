#!/usr/bin/env python

import sys

"""
Input: (n,M,a,b)
Output: Key=n Value=(M,a,b)
"""

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if (line == 'nextround'):
		continue
	wlist = []
	wlist = line.split()
	wlist = [int(x) for x in wlist]
	print '%d\t%d %d %d' %(wlist[0],wlist[1],wlist[2],wlist[3])
