# SJS
# UT Peer-led Biocomputing group, Spring 2016
# Functions HW

# Clean up this script such that it contains *3* functions, templates for which are provided.
# Your final script should produce the same output as this script.
# For an extra challenge, write test cases for each function by checking that a simple input provides what you think it should provide. For example try out, an amino acid sequence like "A" or "T". 
# For an extra extra challenge, come up with different coding strategies from what is provided for each function!



# Amino acid definitions. These lists should be kept at the top of the python script and used as global variables.
POLAR_AA    = ['Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'M', 'W']
NONPOLAR_AA = ['A', 'I', 'L', 'F', 'V', 'P', 'G']
CHARGED_AA  = ['R', 'K', 'D', 'E']
AA_WEIGHTS  = {'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15, 'Q': 146.15, 'E': 147.13, 'G': 75.07, 'H': 155.16, 'I': 131.17, 'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13, 'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15}



######################################################################################################
# Here, fill in functions:

# This function should compute percentage of a certain amino acid type (polar, NONPOLAR_AA, CHARGED_AA) for a given sequence
# def compute_percentage_of_type(sequence, type):
    #code
    #code
    #code
    # return x
    
# This function should replace all occurrences of a certain amino acid type (polar, NONPOLAR_AA, CHARGED_AA) with a provided character
# def replace_type_with_character(sequence, type, character):
    #code
    #code
    #code
    # return x
    
# This function should compute the percentage of weight contributed by a given amino acid type.
# def calculate_weight_percent(sequence, type):
    #code
    #code
    #code
    # return x




######################### BELOW THIS LINE IS WHAT NEEDS TO BE CONVERTED TO MODULAR CODING STYLE! ######################

protein_string = "HGYTSTACHWIQSHVIPHTCWNPGSNTQEQWFADDQTKWFYQGNWLAHILQCDTPSMFRVTKIGQSHEFTNYYRW" # Feel free to change this for testing!

# Determine the percentage of POLAR_AA, NONPOLAR_AA, and CHARGED_AA amino acids in the protein sequence, and print the result to screen.
total_polar = 0.
for p in POLAR_AA:
    total_polar += protein_string.count(p)
percent_polar = total_polar / len(protein_string) * 100
print "The percentage of polar residues is", percent_polar

total_nonpolar = 0.
for np in NONPOLAR_AA:
    total_nonpolar += protein_string.count(np)
percent_nonpolar = total_nonpolar / len(protein_string) * 100
print "The percentage of nonpolar residues is", percent_nonpolar


total_charged = 0.
for c in CHARGED_AA:
    total_charged += protein_string.count(c)
percent_charged = total_charged / len(protein_string) * 100
print "The percentage of charged residues is", percent_charged


# From the original protein sequence, create a "subset" protein for each of the three groups (polar, NONPOLAR_AA, CHARGED_AA) in which all non-polar/nonpolar/charged are replaced by a certain character. Here, we define the character as a gap "-".
# Print the resulting sequence to screen.

replace_character = "-"

# Polar sequence. Turn NONPOLAR_AA and CHARGED_AA residues into gaps
polar_only = ""
for residue in protein_string:
    if residue not in POLAR_AA:
        polar_only += replace_character
    else:
        polar_only += residue
print "The polar-only sequence is", polar_only
        
        
# Nonpolar sequence. Turn POLAR_AA and CHARGED_AA residues into gaps
nonpolar_only = ""
for residue in protein_string:
    if residue not in NONPOLAR_AA:
        nonpolar_only += replace_character
    else:
        nonpolar_only += residue
print "The nonpolar-only sequence is", nonpolar_only


# Charged sequence. Turn POLAR_AA and NONPOLAR_AA residues into gaps
charged_only = ""
for residue in protein_string:
    if residue not in CHARGED_AA:
        charged_only += replace_character
    else:
        charged_only += residue
print "The charged-only sequence is", charged_only





# Determine the percentage of weight for of POLAR_AA, NONPOLAR_AA, and CHARGED_AA amino acids in the protein sequence, and print the result to screen.
total_polar = 0.
total_weight = 0.
for aa in protein_string:
    if aa in POLAR_AA:
        total_polar += AA_WEIGHTS[aa]
    total_weight += AA_WEIGHTS[aa]
percent_polar = total_polar / total_weight * 100
print "The percentage of weight from polar residues is", percent_polar

total_nonpolar = 0.
total_weight = 0.
for aa in protein_string:
    if aa in NONPOLAR_AA:
        total_nonpolar += AA_WEIGHTS[aa]
    total_weight += AA_WEIGHTS[aa]
percent_nonpolar = total_nonpolar / total_weight * 100
print "The percentage of weight from nonpolar residues is", percent_nonpolar

total_charged = 0.
total_weight = 0.
for aa in protein_string:
    if aa in CHARGED_AA:
        total_charged += AA_WEIGHTS[aa]
    total_weight += AA_WEIGHTS[aa]
percent_charged = total_charged / total_weight * 100
print "The percentage of weight from charged residues is", percent_charged

