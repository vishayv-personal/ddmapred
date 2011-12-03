#!/usr/bin/env python
import sys

# this reducer takes 1 \t file,sketch and output  
# and calculated the hamming distance of each file

# reads filenames from a dist cache 
#f = open("file_names.txt")
#text =f.read()
#name_lines = text.split('\n')
DEBUG=False
dict_fname = {} 

def countBits(lxor):

	c = 0 
	while(lxor):
		lxor = lxor & (lxor-1) 
		c = c + 1
	return c	

def getHammingDist(dict_fname):

	# find hamming distance of pairs of files
	files = dict_fname.keys()
	files.sort()

	for i in xrange(len(files)):
		f1 = files[i]
		for j in xrange(i+1,len(files)):
			f2 = files[j]
			if(DEBUG):
				print "file names f1,f2",f1,f2
			sktch1 = dict_fname[f1]
			sktch2 = dict_fname[f2]
			lsktch1 = long(sktch1,2)
			lsktch2 = long(sktch2,2)
			if(DEBUG):
				print "long 1",sktch1
				print "long 2",sktch2
			
			# the hamming distance algo 
			lxor = lsktch1^lsktch2	
			hamdistance = countBits(lxor)
			s = "%s,%s\t%s"%(f1,f2,str(hamdistance))
			print s
					
	 
for line in sys.stdin:
	line = line.strip()
	if( not line):
		continue
	meta,main = line.split('\t')
	fname,sketch = main.split(',')
	fname = fname.strip()
	sketch = sketch.strip()
	if((not fname) or (not sketch)):
		print "incorrect input"
		continue
	dict_fname[fname]=sketch

getHammingDist(dict_fname)
		
	

	
