#!/usr/bin/env python

import sys
from collections import defaultdict

"""
Input: Key=n, Value = (M a b)

Action: for each n, 
		iterate over all corresponding V
			M' = min(M',V.M)
		iterate again over all corresponding V
			Emit (V.a,M',V.a,V.b)
			Emit (V.b,M',V.a,V.b)

Output: (n M a b)

Repeat this job untill there is no M'>M. This is indicated by variable nextround
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
	n = wlist.pop(0)
	#remaining is a list of integers say V = {M,a,b}
	#append this list to dictionary
	dic[n].append(wlist)

nextround = 0

for n in dic:
	Mprime = 99999999
	ll = dic[n]
	#l has the format {M,a,b}
	for l  in ll:
		#check whether you need to repeat mapreduce job-2
		if((Mprime > l[0]) and (Mprime != 99999999)):
			nextround = 1
		Mprime = min(Mprime, l[0])

	for l in ll:
		print "%d %d %d %d" %(l[1],Mprime,l[1],l[2])
		print "%d %d %d %d" %(l[2],Mprime,l[1],l[2])

if(nextround == 1):
	print "nextround"
