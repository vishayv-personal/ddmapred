#!/usr/bin/env python

import sys
#import subprocess
import os

"""
Input: (Did i \t Irpoly Shingle)
CacheFile: MyRabinFingerprintTest.jar
Action: Generate RFP for the corresponding shingle
Output: (Did i \t RFP
"""

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	wlist = ()
	Did,Rid,Irpoly,Shingle = line.split()

	rbf = os.popen("java -jar ./MyRabinFingerprintTest.jar "+Irpoly+' '+Shingle)
	Rfp = str(rbf.readline()).strip()
	print '%s %s\t%s' %(Did,Rid,Rfp)
