#!/usr/bin/env python

import sys
import re

"""
Input: Input: (Did \t contents of the file)
-cacheFile: 80irreducibles.txt
Action: Extract Did
	break the contents into shingles
	store generated shingles in a dictionary to avoid duplicates
	Read 80 irreducible polynimials
	Emit Key = (Did,i) Value = (IRP,Shingle)
Output: (Did i \t IRP Shingle)
"""

n=8;
pattern = re.compile('[\W_]+')

irpoly = open("./80irreducibles.txt", 'r')
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
		shingle = shingle.strip()
		shingle = shingle.strip('\n')
		if (shingle):
			if shingle in Ngrams:
				Ngrams[shingle] += 1
			else:
				Ngrams[shingle] = 1
	for ngram in Ngrams:
		i=0
		for poly in polys:
			poly = poly.strip()
			print '%s %d\t%s %s' %(Did,i,poly,ngram)
			i=i+1
