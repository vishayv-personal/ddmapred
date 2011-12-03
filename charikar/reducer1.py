#!/usr/bin/env python
import sys

# for this reducer the input will be file_id,bit_number \t +1/-1
# the outout will be the total count 
# i.e the output will <file_id\t bit_num,count>
prev_file = ''
prev_bit = ''

for line in sys.stdin:

	line = line.strip() 
	if(not line):
		continue
	doc_bit,score = line.split('\t')
	if((not doc_bit) or (not score)):
		print "reducer 1 did not get proper input"
		continue
	# get score as int 
	score_int = int(score)
	# now get the file id and bit_num
	doc_bit_lst = doc_bit.split(',')
	file_id = doc_bit_lst[0]
	bit_id  = doc_bit_lst[1]
	#total_count = 0 
	# file id and bit id same then add 
	# we have to take advantage of the fact that we sorted by keys
	curr_file = file_id
	curr_bit  = bit_id 
	if((not prev_file) and (not prev_bit)):
		# first time
		total_count = score_int
		prev_file = curr_file 
		prev_bit  = curr_bit  

	else:
		if(prev_file == curr_file):
			if(prev_bit == curr_bit):
				total_count += score_int
				prev_bit = curr_bit 
				# unnecessary step
				prev_file = curr_file 
			else:
		 		# new bit for same file
		 		# EMIT the curr_bit and curr_file
		 		s  = "%s\t%s,%s"%(prev_file,prev_bit,total_count)
		 		print s
				# update prev bit and total_count 
				prev_bit = curr_bit 
		 		total_count = score_int 
				# unnecessary step
				prev_file = curr_file 
		else:
			# will come here for the first bit of new file 
			# we have a new file now 
		  	# emit previous stuff ie last bit of prev file 
			s = "%s\t%s,%s"%(prev_file,prev_bit,total_count)
			print s	
			# update stuff 
			prev_bit = curr_bit 
			total_count =  score_int 
			prev_file = curr_file
# Print last file last bit  
s = "%s\t%s,%s"%(prev_file,prev_bit,total_count)
print s	
			
			
		 			 





	
	 
	
