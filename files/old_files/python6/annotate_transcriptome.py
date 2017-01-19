## This file annotates transcriptomes based on blast output.
## Created 8 March 2016 by RDT

import time
import sys
import csv
from Bio import SeqIO

start = time.clock()

def read_blasthits(blast_hits):
	"""
	This function takes a file with blast hits and returns a dictionary of sequences with their annotations.
	"""
	hit_dict={}
	with open(blast_hits, 'rU') as f:
		for line in f:
			line = line.split(',')
# 			print line
			sequence = line[0]
# 			print sequence
			tophit = ' ' + line[1] + ' ' + line[13]
# 			print tophit
			hit_dict[sequence] = tophit
# 	print hit_dict
	return hit_dict

# sequence_annotations = read_blasthits('AbilAhuG_uniprot_blastx.csv')

def annotate_transcriptome(transcriptome,sequence_annotations,blast_hits):
	"""
	This function takes a transcriptome, a dictionary with sequence names and blast hits (from read_blasthits()), and the name of the blast hit file. It parses the transcriptome sequences; for those with annotations in the dictionary, it copies them to a new list with the annotation appended to the sequence description. Then it writes this list of annotated sequences to a file.
	"""
	print sequence_annotations
	annotated_seqs=[]
	with open(transcriptome, 'rU') as f:
		for rec in SeqIO.parse(f, 'fasta'):
			if rec.id in sequence_annotations.keys():
				rec.description += sequence_annotations[rec.id]
				annotated_seqs.append(rec)
				print "%s appended with %s annotation" %(rec.id, sequence_annotations[rec.id])
			else:
				print "%s does not have blast annotation" %rec.id
	outfile = blast_hits.replace('.csv','.fasta')
	print "Printing annotated sequences to outfile %s" %outfile
	with open(outfile,'w') as g:
		SeqIO.write(annotated_seqs, g, 'fasta')
			
			
# annotate_transcriptome('Trinity_AbilAhuG.fasta',sequence_annotations)

def main():
	assert len(sys.argv) == 3, "This function takes two arguments, the blast hit file and the assembled transcriptome"
	blast = sys.argv[1]
	trans = sys.argv[2]
	sequence_annotations = read_blasthits(sys.argv[1])
	annotate_transcriptome(sys.argv[2],sequence_annotations,sys.argv[1])
	print "File parsed in %fs." %(time.clock() - start)
	
main()
	
