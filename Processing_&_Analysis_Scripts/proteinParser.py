# Author: Gabriel Dell'Accio


# This program searches through a transcriptome for a specific gene provided a contig or accession number.


# Blast parsing file for transcriptome vs transcriptome blasts.
import re
# Initialize states. 
S1 = 1
S2 = 2 
S3 = 3
S4 = 4 
S5 = 5
State = S1


read_in_File = "NMR_transcript_ncbi.fasta"


FileName = "/home/gadellaccio/finalProject/NMR/NMR_annotation/" + read_in_File
BlastFile = open(FileName, 'r')

# Print header line
file = open("proteinOfInterest.txt","w") 
# file.write("Query Contig\tMatch Contig\tE-value\tReading-Frame"+"\n")



# Fill in the query you are searching for here
searchQuery = "004871692"

for Line in BlastFile:
	#print Line
	if State == S1:
		#print "In state one..."
		match = re.search(r'^(>XP_004871692.*)$', Line)
		
		if match:
			#print match.group(0)
			queryContigName = match.group(1)
			# contigLength = match.group(2)
			file.write(queryContigName)
			State = S2
			
	elif State == S2:

		# nextID = re.search(r'^', Line)
		#print "In state two..."
		# group(1) = contig , group(2) = length , group(3) = scoreBits
		# nhf = re.search(r'.*No hits found.*', Line)
		match = re.search(r'^([a-z|A-Z|-]*).*$', Line)
		matchTwo = re.search(r'^>.*$', Line)
		if matchTwo:
			State = S3
		elif match: 
			codonMatch = match.group(1)
			file.write(codonMatch)
			State = S2
			
			
	# elif State == S3:
		
	# 	matchAgain = re.search(r'^\s+Score.*Expect\s=(\s[0-9]*[.][0-9]).*$', Line)
		
	# 	if  matchAgain:
			
	# 		contigExpect = matchAgain.group(1)
			
	# 		State = S4
			
	# elif State == S4:
		
	# 	matchLast = re.search(r'^\s+Strand=(.*)$', Line)
		
	# 	if matchLast:
	# 		contigFrame = matchLast.group(1)
	# 		file.write(queryContigName +"\t"+"\t"+contigMatch +"\t"+"\t"+contigExpect+"\t"+contigFrame+"\n")
	# 		State = S5
		
		
	# elif State == S5:
		
	# 	newQuery = re.search(r'^Query=\s+contig([0-9]*)\s+(length=[0-9]*).*$', Line)
	# 	matchThree = re.search(r'^>\s+contig([0-9]*)\s+length=([0-9]*)\s+numreads=[0-9].*$', Line)
		
	# 	if matchThree:
	# 		contigMatch = matchTwo.group(1)
	# 		lengthMatch = matchTwo.group(2)
	# 		State = S3
	# 	elif newQuery:
	# 		State = S2
	# 	else: 
	# 		State = S1
			
BlastFile.close()
file.close() 
