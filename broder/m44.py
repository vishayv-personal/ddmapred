#!/usr/bin/env python

import sys

#input: <fid1 fid2, 1>
#output: <fid1 fid2, 1>
#it essentially does nothing. It lets the reducer combine all pairs
#to give final count
for line in sys.stdin:
	line = line.strip()
	print '%s' %(line)
