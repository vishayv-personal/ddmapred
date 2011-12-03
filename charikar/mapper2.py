#!/usr/bin/env python
import sys 

# input file \t bit,score
# the mapper may read the file in any order but we are banking on the fact 
# that the previous reducer's ouput contains all the entries for a file

# this mapper outut the file \t and its sketch 

for line in sys.stdin:

	line = line.strip()
	if (not line):
		continue
	file_id,bit_score = line.split('\t')
	if( (not file_id ) or ( not bit_score) ) :
		print "incorrect input "
		continue
	bit,score = bit_score.split(',')

	curr_file = file_id

	if( (not bit) or (not score) ):
		print "incorrect bit score for file",curr_file
		continue
	s = "%s\t%s,%s"%(file_id,bit,score)
	print s
