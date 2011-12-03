#!/usr/bin/env python

import sys
from collections import defaultdict

#input: <fid1 fid2, 1>
#output: aggregate all fid1 fid2 print its sum
# <fid1 fid2, count>

fidpairdict = defaultdict(int)

for line in sys.stdin:
	line = line.strip()
	wlist = line.split('\t',1)
	fidpairdict[wlist[0]] +=1

for fidpair in fidpairdict:
	print '%s\t%s' %(fidpair, fidpairdict[fidpair])
