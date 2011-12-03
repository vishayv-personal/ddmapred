#!/usr/bin/env python
import sys 
from collections import defaultdict
# input file \t bit,score
# the mapper may read the file in any order but we are banking on the fact 
# that the previous reducer's ouput contains all the entries for a file

# this mapper outut the file \t and its sketch 

dict_fs = defaultdict(list)

def print_kv(dict_fs):

	for fil  in dict_fs:
		l = dict_fs[fil]
		#for i in range(len(l)):
		sketch_str = ''.join(l)
		s = "%s\t%s"%(fil,sketch_str)
		#s = "%s\t%s,%s"%(fil,i,l[i])
		print s

for line in sys.stdin:

	line = line.strip()
	if (not line):
		continue
	file_id,bit_score = line.split('\t')
	file_id.strip()
	#if( (not file_id ) or ( not bit_score) ) :
	#	print "incorrect input "
	#	continue
	bit,score = bit_score.split(',')

	curr_file = file_id
	#if( (not bit) or (not score) ):
	#	
	#	print "incorrect bit score for file",curr_file
	#	continue

	# convert to int  
	bit = int(bit)
	score = int(score)
	if curr_file in dict_fs:

		if (score > 0 ): 
			dict_fs[curr_file][bit]= '1'
		else:
			# when score == 0 or -ve 
			dict_fs[curr_file][bit]= '0'
		#if(curr_file == '2'):
		#s = "%s\t%s,%s"%(curr_file,bit,dict_fs[curr_file][bit])
		#print s
	else:
		# init 
		dict_fs[curr_file] = ['$']*64
		# update score
		if (score > 0 ): 
			dict_fs[curr_file][bit]= '1'
		else:
			# when score == 0 or -ve 
			dict_fs[curr_file][bit]= '0'
		
		#if(curr_file == '2'):
		#s = "%s\t%s,%s"%(curr_file,bit,dict_fs[curr_file][bit])
		#print s

	# assumes each file will occur in chunks
print_kv(dict_fs)
"""
for fil in dict_fs:
	l = dict_fs[fil]
	#for i in range(len(l)):
	sketch_str = ''.join(l)
	s = "%s\t%s,%s"%(str(1),fil,sketch_str)
	#s = "%s\t%s,%s"%(fil,i,l[i])
	print s
"""	
