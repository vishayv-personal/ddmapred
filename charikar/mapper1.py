#!/usr/bin/env python
import re
import string
import sys
# look for module in distributed cache 
sys.path.append('.')
import smhasher

# This module will hash all the shingle in each input line 
# for each file get al
# FILEID : 1 to 64 hashof shingle # reduce step fileid,1:shingle 
# mapper2 , fileid,1  for all hashes add + 1 or -1  reduce will add those u

k = 8
regex = re.compile('[%s]' % re.escape(string.punctuation))

# TODO remove print statements:

def test_re(s):  # From Vinko's solution, with fix.
    return regex.sub('', s)

# return the num > 0 if bit is set 0 otherwise
def testBit(l_type,offset):

        one = 1
        l_one = long(one)
        mask = l_one << long(offset)
	#print "looking at bit number ",offset
        #print bin(mask)
        #print bin(l_type)
        return (l_type & mask)
	 
	 
for line in sys.stdin:

	line = line.strip()
	if(not line):
		continue
	# split the line by \t 
	doc_id,content = line.split("\t")
	if( (not (doc_id)) or (not(content))):
		print "line not formated properly"	
		break
	# remove punctuations
	content = test_re(content)
	# split into an array of words 	
 	
	content_arr = content.split()
	shingle = ""
	# if line len is less than 8 then just emit the whole line as shingle 
	if( len(content_arr) < k):
		shingle = ''.join(content_arr)
		#s = "%s\t%s"%(doc_id,shingle)
		shing_hash = smhasher.murmur3_x86_64(shingle)
		# now output this 64 times 0 - 63 
		for j in xrange(64):
			# calculate the hash of shingle 
			# test j'th Bit 
			bit_num = testBit(shing_hash,j)
			# set bit_out = 1 if its set and bit out = 0 if not
			if bit_num > 0:
				bit_out = 1
			else:
				bit_out = -1
			#print "bit num",j,"is =",bit_out
			# we have to pass the bit as string( can hadoop accept bints / floats )	
			s = "%s,%s\t%s"%(doc_id,str(j),str(bit_out))
			# to avoid overhead of copying why dont u just output +1 			or -1 	
			print s

	else:
		for i in xrange(len(content_arr) - k + 1):
			shingle = ''.join(content_arr[i:i+k])
			# now take a hash of each shingle 
			shing_hash = smhasher.murmur3_x86_64(shingle)
			# now output each shingle 's j th bit 
			for j in xrange(64):

				bit_num = testBit(shing_hash,j)
				#print "bit_num ",bit_num
				#print shing_hash
				#print "for jth val ==",j
				# set bit_out = 1 if its set and bit out = 0 if not
				if bit_num > 0:
					bit_out = 1
				else:
					bit_out = -1
				#print "bit num",j,"is =",bit_out
				s = "%s,%s\t%s"%(doc_id,str(j),str(bit_out))	
				print s
