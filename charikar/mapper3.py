#!/usr/bin/env python
import sys

# this reducer takes 1 \t file,sketch and output  
# and calculated the hamming distance of each file

# reads filenames from a dist cache 
for line in sys.stdin:
	line = line.strip()
	if( not line):
		continue
	fname,sketch = line.split('\t')
	fname = fname.strip()
	sketch = sketch.strip()
	if((not fname) or (not sketch)):
		print "incorrect input"
		continue
	print "%s\t%s,%s"%(str(1),fname,sketch)		
	

	
