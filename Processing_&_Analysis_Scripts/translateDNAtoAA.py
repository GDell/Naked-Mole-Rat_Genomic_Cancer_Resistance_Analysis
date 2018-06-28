#-----------------------------------------------------------------
# BIOL/CMPU-353 
# Spring 2017 BIOINFORMATICS FINAL PROJECT
# Modified by: Gabriel Dell'Accio & Jordan Peyer
#-----------------------------------------------------------------

# Regular and random expression library 
import re
import random
import math
from difflib import SequenceMatcher

			
Path = "/home/joschwarz/public/mod-mol-evo/"				# mutation rate

NucFile = Path + "hsp70_nuc.fasta.txt"	# files containing
# AAFile = Path + "hsp70_aa.fasta.txt"	# DNA and protein sequences

DNASeq = ""								# strings to hold original
# OrigProtSeq = ""						# DNA and protein sequences

AACodonFileName = Path + "aa-codon-table.txt"

CodonMap = {}	

# main function: called at bottom of file
def main():

		# Global variables
	#Initialize states
	S1 = 1
	S2 = 2
	S3 = 3 

	State = S1

	file = open("CASP8_Homo_aa.fasta","w") 
	FileName = "CASP8/CASP8_Homo_nuc.fasta"
	multiFastaFile = open(FileName, 'r')


	newAminoAcidSequence = ""
	
	createCodonMap()

	for Line in multiFastaFile:

	    # if State == S1:
	    #     speciesQuery = re.search(r'^(>.*)$', Line)

	    #     if speciesQuery:
	    #     	speciesName = speciesQuery.group(1)
	    #     	print(speciesName)
	    #     	file.write(speciesName)
	    #     	State = S2 

	    if State == S1: 
	    	dnaSequence = re.search(r'^([A-Z]*)$',Line)
	    	newSpeciesQuery = re.search(r'^(>.*)$', Line)
	    	
	    	if newSpeciesQuery:

	    		newSpecies = newSpeciesQuery.group(1)
	    		# print(newSpecies)
	    		file.write(newSpecies)

	    	elif dnaSequence:

	    		dnaLine = str(dnaSequence.group(1))

	    		# print(dnaLine)
	    		
	    		newAminoAcidSequence = translate(dnaLine)
	    		# print(newAminoAcidSequence)
	    		file.write(newAminoAcidSequence)
	    		# file.write(translatedDnaLine)
	    		








#---------------\
# createCodonMap \
#--------------------------------------------------------------------
# Summary: populates dictionary for aa lookups by codon
#
def createCodonMap():
    InFile = open(AACodonFileName, 'r')

    for Line in InFile:
        AAlist = Line.split()
        AA = AAlist[0]
        for Codon in AAlist[1:]:
        	CodonMap[Codon] = AA 

    InFile.close()


#----------\
# translate \
#--------------------------------------------------------------------
# Summary: translates DNA strings to proteins
def translate( DNA ):
	Pro = ""
	for Codon in re.findall('(...)', DNA):
		Pro = Pro + CodonMap[Codon]
	return Pro


#--------------\
# readFastaFile \
#--------------------------------------------------------------------
# Summary: read fasta file containing single sequence, return sequence
def readFastaFile( Filename ):
	InFile = open(Filename, 'r')
	InFile.readline()	# ignore tag line
	
	Sequence = ""		# read and concatenate sequence lines
	for Line in InFile:
		Sequence = Sequence + Line.rstrip('\n')
	
	InFile.close()
	return Sequence

main()

# print(calcIdentity("aaa", "aaa"))
