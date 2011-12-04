#!/usr/bin/env python

import sys

"""
Eliminate duplicate tuples
--------------------------

Input: (n M a b)
Action: Let Key = (n M a b), Value = 1
		Emit (Key, Value)
Output: (n M a b \t 1)
"""
for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if (line == 'nextround'):
		continue
	print '%s\t%s'%(line,str(1))
