#!/usr/bin/env python

import sys

"""
Input: (Did i \t RFP)
Output: (Did i \t RFP)
"""

for line in sys.stdin:
	line = line.strip()
	wlist = line.split('\t',1)
	#Did_rid = wlist.pop(0)
	print '%s\t%s' %(wlist[0],wlist[1])
