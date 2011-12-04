#!/usr/bin/env python

import sys

"""
Input: (Did i \t RFP)
Output: (Did \t  min(RFPi))

"""


dic = {}

for line in sys.stdin:
	line = line.strip()
	#split the input got from mapper,
	#maxsplit=2 means, there will be 2 splits leading to 3 elements
	wlist = line.split('\t',1)
	Did_rid = wlist.pop(0)
	RFP = long(wlist[0],16)
	if Did_rid in dic:
		if RFP<dic[Did_rid]:
			dic[Did_rid] = RFP
	else:
		dic[Did_rid] = RFP

for Did_rid in dic:
	Did = Did_rid.split(' ',1)[0]
	print '%s\t%X' % (Did,dic[Did_rid])
