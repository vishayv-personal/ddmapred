#!/usr/bin/env python

import sys

"""
Input: (a b	J)

Action: if J > threshold, {
		M = min(a,b)
		Emit (a,M,a,b)
		Emit (b,M,a,b)
	}

Output: (n M a b)
"""
threshold = 0.7

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	wlist = []
	wlist = line.split()
	wlist = [int(x) for x in wlist]
	#pop last element
	jc = wlist.pop()
	if(jc >= threshold*80):
		M = min(wlist[0],wlist[1])
		print '%d %d %d %d' %(wlist[0],M,wlist[0],wlist[1])
		print '%d %d %d %d' %(wlist[1],M,wlist[0],wlist[1])
