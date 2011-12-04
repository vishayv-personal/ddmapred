#!/usr/bin/env python

import sys
from collections import defaultdict

"""
Eliminate duplicate tuples
--------------------------
Input: (n M a b \t 1)
Action: Build a dictionary of incoming Keys
		Output Keys
Output: (n M a b)
"""


dic = defaultdict(str)

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if (line == 'nextround'):
		continue
	wlist = line.split('\t')
	dic[wlist[0]] = 1

#wlist = list(set(wlist))

for tupl in dic:
	print '%s'%(tupl)
