#!/usr/bin/env python
import sys


for line in sys.stdin:

	line = line.strip()
	files,hamd = line.split('\t')
	fil1,fil2 = files.split(',')
	print "%s\t%s,%s"%(hamd,fil1,fil2)
	
