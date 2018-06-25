# Characterizing Cancer Resistance Genes in Naked Mole Rats
Project by Gabriel Dell'Accio and Jordan Peyer

## Project Structure

### Blast Annotation
First, we annotated the NMR transcriptome we found at www.naked-mole-rat.org by Blasting it against Swiss Prot at an e-val of 10. The results of our blast annotation and parsing of the blast results is located in the "Blast Annotation" file within our google drive, or the "NMR_annotation" file in my finalProject/NMR/ folder on jr. The entire raw Blast result file is located on jr in this directory. We only included the parsed results of our blast annotation in our google drive as the raw file is huge. In order to fully annotate and parse the results of the Blast search, I wrote a blast parse program discussed below in the Analsis Scripts section. The primary things we parsed for were e-val, gene name, accession number, gene-id, and contig.

### Identifying and Parsing Proteins of Interest
After performing the blast annotation, we identified five cancer related genes in the parsed annotation results that were shared by both humans and NMRs. We identified these genes by researching NMR and human cancer literature for specific proteins of interest. The chosen proteins of interest are located in the "Gene Analysis" folder in our google drive and are located in the "proteins" folder in my (Gabriel Dell'Accio's) jr directory within my "finalProject" and "NMR" directories. In the proteins folder, we have 5 directories that are named after the 5 particular cancer related genes that we chose to examine. In order to retrieve the DNA sequences of these 5 proteins from the NMR transcriptome, I developed a program, the proteinParser.py discussed in the Analysis Scripts section below, that would search through the NMR transcriptome and write the specified DNA sequence to a new file in fasta format.  


### Clustal Alignments and Analysis
In order to prepare for the clustal alignments in the next step, I wrote a program, the translateDNAtoAA.py program discussed below, that would translate a DNA fasta file to a amino acid fasta file. I used this program to translate all five of the NMR and human dna protein sequences of interest to amino acid sequences and then created amino acid and DNA multi-fasta files to plug through the clustal alignment website. We ran the Clustal alignments and then placed the output files on our google drive. Inside each protein directory in the google drive and Jr file, we have the clustal alignment results for both nucleotide and amino acid clustal alignments, in addition to the output files from our analyzation of these alignments.
In order to analyze these DNA and amino acid sequence alignments, I wrote an alignment parser program discussed below in the Analysis Scripts section. This program goes through DNA and amino acid clustal alignment output files in FASTA format and analyzes differences between NMR's and humans in proteins of interest. It calculates the percent identity of the alignment with and without dashes. In addition, provided a list of key amino acid positions, it parses through amino acid aligments to see whether there were any SNPs that occurred in those positions. Thus, the analyzation output files list all of the positions of any SNPS in the clustal alignments and make note of any SNPS in key regions. We placed protein files on Jr and on the google drive in addition to all of the FASTA format files of the protein of interest for both NMR's and Humans, which we used to perform the clustal alignments.

### Analysis Scripts

In this folder located in both JR and in our google drive doc, we have the four scripts discussed above that were used in order to do the blast annotation and gene analysis for this project. If you are interested in analyzing any of the following scripts in more detail, I would advise you to open the scripts and read my comments as they should guide you through how the program works. Here is a general overview of the function of each:

- 1)  translateDNAtoAA.py

	This program takes in a DNA sequence in fasta format and translates it to an amino acid chain. We used this program in order to translate the DNA sequences of our proteins of interest for both Humans and NMR's.

- 2)  proteinParser.py

	This program takes in the label for a protein of interest in FASTA format and then searches through the NMR transcriptome file to pull out that protein in FASTA format. We used this program in order to isolate our genes of interest from the NMR transcriptome in order to run our clustal alignments and generate the Amino Acid sequence for that protein.

- 3)  Blast_parser.py

	We used this program in order to parse through the results of Blasting our NMR transcriptome. This state machine compiles contig numbers, accession numbers, species, gene-id, name, and e-val for each gene in the Blast output file. We used this program in order to produce a list of genes shared by humans and NMR's that we could begin to sift through and research in order to identify cancer related genes of interest for further clustal analysis.

- 4)  alignmentParse.py

	We used this program in order to parse through the results of clustal alignments in order to analyze differences between NMR's and humans in proteins of interes. It calculates the percent identity of the alignment with and without dashes. In addition, provided a list of key amino acid positions, it parses through an amino acid aligment to see whether there were any SNPs that occurred in those positions.
