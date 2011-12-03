#!/usr/bin/env python

import sys
import string
import re
import os
import subprocess

#N
n=6;
irpoly = open("80irreducibles.txt", 'r')
pattern = re.compile('[\W_]+')
polys = ()
polys = irpoly.readlines()

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	wlist = ()
	wlist = line.split()
	Did = wlist.pop(0)
	Did = re.sub(pattern,'',Did)
	Ngrams = {}
	for i in range(len(wlist) - n + 1):
		shingle = ''.join(wlist[i:i+n])
		shingle = re.sub(pattern,'',shingle)
		if shingle in Ngrams:
			Ngrams[shingle] += 1
		else:
			Ngrams[shingle] = 1
	for ngram in Ngrams:
		i=0
		for poly in polys:
			poly = poly.strip()
			rbf = os.popen("java -jar MyRabinFingerprintTest.jar "+poly+' '+ngram)
			print '%s %d\t%s' %(Did,i,str(rbf.readline()).strip())
			i = i+1
