#!/usr/bin/env python
import sys 

# input file \t bit,score
# the mapper may read the file in any order but we are banking on the fact 
# that the previous reducer's ouput contains all the entries for a file

# this mapper outut the file \t and its sketch 

prev_file = "" 
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

	# convert to int  
	bit = int(bit)
	score = int(score)
	# assumes each file will occur in chunks 
	if(not prev_file):
		# first file
		# init arr 
		sketch = [0 for x in xrange(64)]
		# set first score 
		if (score > 0 ): 
			sketch[bit] = '1'
		else:
			# when score == 0 or -ve 
			sketch[bit] = '0'
		# set prev file 
		prev_file = curr_file
	else:
		if(prev_file == curr_file ):
			# set sketch bit
			if (score > 0 ): 
				sketch[bit] = '1'
			else:
				# when score == 0 or -ve 
				sketch[bit] = '0'
			# update prev file 
			prev_file = curr_file

		else:
		# we have a new file so we emit the prev file
		#emit stuff
			sketch_str = ''.join(sketch)
			s = "%s\t%s,%s"%(str(1),prev_file,sketch_str)
			print s
			prev_file = curr_file	
			# reinitialize the sketch list
			sketch = [0 for x in xrange(64)]
			# set first score 
			if (score > 0 ): 
				sketch[bit] = '1'
			else:
				# when score == 0 or -ve 
				sketch[bit] = '0'

# Last file
sketch_str = ''.join(sketch)
s = "%s\t%s,%s"%(str(1),prev_file,sketch_str)
print s

	
