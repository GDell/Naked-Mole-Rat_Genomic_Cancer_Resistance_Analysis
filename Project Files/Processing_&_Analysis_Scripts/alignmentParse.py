# Author: Gabriel Dell'Accio & Jordan Peyer


# This script analyzes an alignment in order to determine whether 
# there are any differences in key active sites across both organisms. 



import re
import numpy as np
# Initialize states. 
S1 = 1
S2 = 2 

State = S1


readFile = "CASP8/Clustal/CASP8_alignment_nuc.fasta"
count = 0
FileName = readFile
alignmentFile = open(FileName, 'r')
file = open("CASP8_nuc_analyzed.txt","w") 

file.write("The following is nucleotide output for the TELOMERE gene alignment: \n ")

# returns a number 0 - 5. The lesser the number, the less variation for that codon position
def variationMetric(Seq1):

	isA = 0
	isT = 0 
	isG = 0 
	isC = 0
	isDash = 0

	for each in Seq1:
		if each == "a" or each == "A":
			isA = 1
		elif each == "t" or each == "T":
			isT = 1
		elif each == "g" or each == "G":
			isG = 1
		elif each == "c" or each == "C":
			isC = 1
		elif each == "-":
			isDash = 1


	return (isA + isT + isG + isC + isDash)

def createDelimittedString(Seq1):

	tempString = ""

	for each in Seq1:
		tempString = tempString + str(each) + ","


	return (tempString)

theSequences = []

geneCount = 0

theCurrentSequence = ""



for Line in alignmentFile:

	if State == S1:

		match = re.search(r'^>.*$', Line)

		

		otherMatch = re.search(r'^([a-z|A-Z|-]*)', Line)

		if match:


			# print(match.group(0))
			
			State = S1 
			# print("This is the current sequence: " + theCurrentSequence)
			# theSequences.append([theCurrentSequence]) 
			theCurrentSequence = ""


		elif otherMatch:

			sequenceAdd = str(otherMatch.group(1))

			# print(sequenceAdd)

			theCurrentSequence = theCurrentSequence + sequenceAdd
			theSequences.append([theCurrentSequence])
			


theSequences.append([theCurrentSequence]) 

alignmentFile.close()


# print(theSequences)

numberOfGenes = len(theSequences)
lengthOfGene = len(theSequences[0])
# print("The total number of genes: " + str(numberOfGenes + 1))

seq1 = createDelimittedString(theSequences[0])
seq2 = createDelimittedString(theSequences[1])

# print(seq1)
# print(seq2)


zippedSeqs = zip(seq1,seq2)

# print(zippedSeqs)

count = 0.0
numberNonMatch = 0 
numberNonMatchInclude = 0


nonmatchIndexList = []

nonmatchDifferences = []

#360, 376
keySites = []

mutationInKeySites = []

for aa1,aa2 in zippedSeqs:

	count = count + 1

	collection = [aa1,aa2]

	if aa1 != aa2: 

		if aa1 == "-" or aa2 == "-":
			numberNonMatchInclude = numberNonMatchInclude + 1
		else:
			numberNonMatchInclude = numberNonMatchInclude + 1
			numberNonMatch = numberNonMatch + 1

		if count in keySites:

			mutationInKeySites.append(count)


		indexResult = "index :" + str(count) + " is a non match" + "\n"
		mismatchPair = "The following are the mismatch: " + str(collection) +"\n"

		file.write(indexResult)
		file.write(mismatchPair)

		# print(indexResult)
		# print(mismatchPair)
		# nonmatchIndexList.append(count)
		# nonmatchDifferences.append([aa1,aa2])

if len(mutationInKeySites) >= 1:
	print("THERE WERE MUTATIONS IN KEY SITES")
	keySNPS = "There were mutations in the following key sites: " +  str(mutationInKeySites) + "\n"
	file.write(keySNPS)
else :
	print("THERE WERE NO MUTATIONS IN KEY SITES")
	keySNPS = "There were no mutations in key sites" +"\n"
	file.write(keySNPS)


percentageSame = "The percent similarity for these two genes without dashes: " + str(1- ((numberNonMatch *1.0)/count)) + "\n"
percentageSameInclude = "The percent similarity for these two genes with dashes: " + str(1- ((numberNonMatchInclude *1.0)/count)) + "\n"

totalNumberChecked = "The total number of indexes searched: " + str(count) + "\n"
totalNumberofNonMatches = "The total number of nonmatches was: " + str(numberNonMatch) + "\n"

file.write(percentageSame)
file.write(percentageSameInclude)
file.write(totalNumberChecked)
file.write(totalNumberofNonMatches)



file.close() 


