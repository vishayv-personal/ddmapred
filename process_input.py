import re
import sys 

filename = "hctext.pages"
SPLIT_PATTERN = "==P=>>>>=i===<<<<=T===>=A===<=!Junghoo!==>\n"
#PAGE_DATA ="URL:(.*?)\nDate:.*?\nPosition:.*?\nDocId:(.*?)\n\nHTTP/1.0\s+(.*?)\nServer:.*?\nDate:.*?\n(.*)"
PAGE_DATA ="URL:(.*?)\nDate:.*?\nPosition:.*?\nDocId:(.*?)\n\nHTTP/1.\d\s+(.*?)\n(.*)"
REMOVE_CONT_NL = '(\n\s*\n)+'
REMOVE_CONT_NL_R = '\n'
KEY_VALUE_PATT = "(.*?):(.*?)"
CSS_PATT = ".*?{.*?\}"
C_P = re.compile(CSS_PATT,re.DOTALL)
space_patt = "\s+"

def f_read(filename):
	f = open(filename)
	text = f.read()
	return text
	#remove crap key:value
	re.sub()
	#remove css if there 



def smash_text(text):

	# text has lot of crap like css delete css  
	text = re.sub(REMOVE_CONT_NL,REMOVE_CONT_NL_R,text)

	# DELETES EVERYTHING UNTIL THE LAST CSS  Assumes there is no text between css or there is not css after the main text 
	text = re.sub(C_P,"",text)
	# remove the \s and \n in betwween the text 
	text = re.sub('\n',' ',text)
	# remove consecutive spaces to single space 
	text = re.sub(space_patt,' ',text)
	return text 
	#print text
	#print "****"


def split_pages(text):
	
	# text looks like delimiter,text,delimited, ..however some pages are not extracted 
	pages = re.split(SPLIT_PATTERN,text)
	# remove first and last elements of split array	
	pages = pages[1:]
	pages = pages[:-1]
	#print pages[4]
	count = 0 
	# from each split remove the relevant data and store it in a list
	for page in pages:
		m = re.match(PAGE_DATA,page,re.DOTALL)
		if m:
			if (m.group(3) == "404 Not found" or m.group(3) == "302 Found"):
				#print "page with DocId",m.group(2)," was not extracted properly "
				continue 
			elif(m.group(3) == "200 OK"):
					doc_id = m.group(2)
					url = m.group(1)
					page_text = m.group(4)
					# strip the strings 
					doc_id = doc_id.strip()
					url = url.strip()
					page_text = page_text.strip()
					#print "processing Docid ",doc_id
					page_text_line = smash_text(page_text)
					print "%s\t%s" %(doc_id,page_text_line)
					#print "DocID=",doc_id 
					#print "URL=",url 
					##print "TEXT=",page_text
			else:
				#print "strange behaviour Page with DocId",m.group(2),"has a message of ",m.group(3)
				sys.stderr.write("strange behaviour Page with DocId"+m.group(2)+"has a message of "+m.group(3))
				continue 

		else:
			#print "PATTERN DID NOT MATCH"
			print "data",page 
			sys.stderr.write("PAGE DATA PATTERN DID NOT MATCH")
			continue 

if __name__ =="__main__":

	text = f_read(filename)
	split_pages(text)

