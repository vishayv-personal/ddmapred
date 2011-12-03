#!/usr/bin/env python
import sys

# this reducer takes 1 \t file,sketch and output  
# and calculated the hamming distance of each file

# reads filenames from a dist cache 
f = open("file_names.txt")
text =f.read()
name_lines = text.split('\n')
for line in sys.stdin():
	line = line.strip()
	if( not line):
		continue
	fname,sketch = line.split('\t')
	fname = fname.strip()
	sketch = sketch.strip()
	if((not fname) or (not sketch)):
		print "incorrect input"
		continue
	for name in name_lines:
		name = name.strip()
		# we dont want to calculate hamming distance for same files
		if(name == fname):
			continue 
		
	

	
