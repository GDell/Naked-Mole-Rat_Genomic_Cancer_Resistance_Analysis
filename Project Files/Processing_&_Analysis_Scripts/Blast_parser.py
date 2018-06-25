

import re

#----------------------------------------------------------------
# FSM: Finite State Machine (has states and transitions)

# Here is what each state represents: 
#
# S1: looking for the contig in the query
# S2: looking for the accession info or "no hits found" 
# S3: looking for species and gene name
# S4: looking for e-value
# S5: looking for reading frame
#
# Here is a table representation of the state transition function 
# with initial state S1. 
#
# From-State  To-State  if Line match =
# ----------  --------  ---------------
#     S1         S2     "Query="
#     S2         S3     "> sp | "
#     S2         S1     "No hits found"
#     S3         S4     "OS= " and "GN= "
#     S4         S5     "Expect = "
#	  S5		 S1		"Frame = "
#----------------------------------------------------------------

# initialize states S1 - S5, and start state
S1 = 1
S2 = 2
S3 = 3
S4 = 4
S5 = 5
S6 = 6
State = S1
count = 0

# Print header line for three (3) tab-separated columns
print "Contig\tAccession\tSpecies\tGene ID\tGene Name\tE-value\tReading Frame"

FileName = "rightblast_NMR_genes_v_SwissProt.blastx"
BlastFile = open(FileName, 'r')

file = open("NMR_blast_parse_output.txt", "w")
file.write("Contig Number\tAccession\tSpecies\tGene ID\tGene Name\tE-value\tReading Frame"+"\n")

for Line in BlastFile:

    if State == S1:
        contigQuery = re.search(r'^Query=\s+(.*)', Line)
        if contigQuery:
            contig = contigQuery.group(1)
            State = S2
            
    elif State == S2:

        nhf = re.search(r'No hits found', Line)
        access = re.search(r'^>\s*sp\|(.*)\|', Line)
        Name = re.search(r'^>\s*sp\|(.*)\|(\w+)\s+(.*)', Line)
        if nhf:
        	State = S1
        elif access:
            ID = access.group(1)
            GeneName = Name.group(3)
            State = S3
            
    elif State == S3:
    	specname = re.search(r'OS=((\w+)\s+(\w+))', Line)
    	if specname:
    		species = specname.group(1)
    		State = S4

    elif State == S4:
    	genID = re.search(r'GN=(.*)\s+PE=', Line)
    	if genID:
    		gene = genID.group(1)
    		State = S5

    elif State == S5:
    	expect = re.search(r'Expect\s+=\s+(.+),\s+', Line)
    	if expect:
    		e = expect.group(1)
    		State = S6

    elif State == S6:
    	rframe = re.search(r'Frame\s+=\s+(.+)\s+', Line)
        if rframe:
        	frame = rframe.group(1)
        	file.write(contig+"\t"+ID+"\t"+species+"\t"+gene+"\t"+GeneName+"\t"+e+"\t"+"\n")
        	
        	count = count+1
        	State = S1

    else:
        print "===> Error processing BLAST output: this line shouldn't print"

BlastFile.close()

file.close()
print count
