#!/usr/bin/env python

import sys
from collections import defaultdict

"""
Final clustering
----------------
Input: (M \t n)
Action: Build a dictionary with M as keys and list of n as values
		Append incoming n to the list for each M
	At the end of the input, number of keys represent number of clusters
Output: (M \t a,b,c,d...)
"""

dic = defaultdict(list)

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if (line == 'nextround'):
		continue
	wlist = []
	wlist = line.split()
	wlist = [int(x) for x in wlist]
	dic[wlist[0]].append(wlist[1])

for M in dic:
	wlist = list(set(dic[M]))
	wliststr = [str(x) for x in wlist]
	wstr = ','.join(wliststr)
	print '%d\t%s'%(M,wstr)
