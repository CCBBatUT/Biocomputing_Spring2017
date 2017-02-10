"""
    SJS.
    This module contains functions which are written up during classtime. The functions shown here are the final functions written.
"""

# Global variables often use capital letters to distinguish them as global
NUCLEOTIDE_COMPLEMENT  = {'A': 'T', 'C': 'G', 'G': 'C', 'T':'A'}
TRANSLATION_TABLE  = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAC':'Y', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}
AMBIGUOUS_NUCLEOTIDE = "N"



def complement1(sequence):
    """
        Determine the complement of a nucleotide sequence.
        Takes a nucleotide sequence (string) as argument and returns its complement.
        
        This function works fine, but it suffers from 'hard-coding'.
    """
        
    final_sequence = ""
    for nuc in sequence:
        if nuc == "A":
            final_sequence += "T"
        elif nuc == "C":
            final_sequence += "G"
        elif nuc == "G":
            final_sequence += "C"
        elif nuc == "T":
            final_sequence += "A"
        else:
            final_sequence += "N"
    return final_sequence
    
def complement2(sequence):
    """
        Determine the complement of a nucleotide sequence.
        Takes a nucleotide sequence (string) as argument and returns its complement.
        
        This function is an improved way to write "complement1()". It does not suffer from hard-coding and it handles ambiguous nucleotide exceptions.
    """
    final_sequence = ""
    for nuc in sequence:
        try:
            final_sequence += NUCLEOTIDE_COMPLEMENT[nuc]
        except:
            final_sequence += AMBIGUOUS_NUCLEOTIDE
    return final_sequence
    



def reverse_complement(sequence):
    """
        This function determines the reverse complement for a given nucleotide sequence. 
        Note that is uses the complement2() function.
    """
    comp = complement2(sequence)
    revcomp = list(comp)
    revcomp.reverse()
    revcomp_string = ''.join(revcomp)
    return revcomp_string
    

# Give bad input, and deal with it somehow. This teaches try and except
def translate_sequence1(sequence):
    """
        This function translates a given DNA sequence to amino acids. 
    """
    translated = ''
    for x in range(0, len(sequence), 3):
        codon = sequence[x:x+3]
        aa = TRANSLATION_TABLE[codon]
        translated += aa


def translate_sequence2(sequence):
    """
        This function translates a given DNA sequence to amino acids.
        It is an improved version of translate_sequence1() because it checks whether the codon can even be translated using if/else.
    """
    translated = ''
    for x in range(0, len(sequence), 3):
        codon = sequence[x:x+3]
        if codon in translation_table:
            aa = TRANSLATION_TABLE[codon]
            translated += aa
        else:
            print 'Cannot translate this codon'
            continue # or could do break
            
def translate_sequence(sequence):
    """
        This function translates a given DNA sequence to amino acids.
        It is an improved version of translate_sequence2() because it handles errors more broadly with a try/except statement.
    """
    translated = ''
    for x in range(0, len(sequence), 3):
        codon = sequence[x:x+3]
        if codon in TRANSLATION_TABLE:
            try:
                aa = TRANSLATION_TABLE[codon]
            except:
                pass  # Could also print a failure message, could continue, break, pass, lots of options...
     
                
def compute_letter_counts(sequence):
    """
        This function counts the number of each letter in a sequence, specifically by *building up a dictionary during the for loop*. The function returns a dictionary of counts.
        By building up this dictionary as we go, we ensure that unknown letters do not throw errors.
    """
    letter_counts = {}
    for letter in sequence:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts
    
    
def compute_letter_frequencies(sequence):
    """
        This function computes the frequency of each letter in a sequence. Note that it calls the function compute_letter_counts()!
    """
    letter_freqs = compute_letter_counts(sequence)
    total_count = float(sum(letter_freqs.values()))
    for entry in letter_freqs:
        letter_freqs[entry] /= total_count
    return letter_freqs
    








