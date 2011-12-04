#!/usr/bin/env python

import sys

#input <fid, RFP> pairs
#output <RFP, fid>
#let the reducer combine filenames with same RFP

for line in sys.stdin:
	line = line.strip()
	wlist = line.split('\t',1)
	print '%s\t%s' %(wlist[1],wlist[0])
