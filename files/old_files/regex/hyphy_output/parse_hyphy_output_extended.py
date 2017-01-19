"""
    SJS
    Regular Expressions example script 2.
    
    All files name "rep..._nucfit.txt" in this directory are **real files from Stephanie's research**, produced by the software HyPhy (https://github.com/spond/hyphy). Each file, which is named according to the dataset it describes, contains information about a fitted model of sequence evolution.
    This script will parse all .txt files in the working directory to obtain all nucleotide mutation rates: the nucleotide mutation rate for "AC" (A to C or C to A), which appears in each file like this:
        global AC=0.3562821267007032;
        global AT=0.3561898444276437;
        global CG=0.266526902373061;
        global CT=1.502997839429121;
        global GT=0.2632076545083971;
    All information will be saved to a single .csv file for future use (e.g. data analysis in R!).
    
    This script uses re.findall to find all matching occurrences.
    
"""
# Import needed modules
import os
import re

# Define the final output file name and write a header to the file
output_file = "hyphy_information_extended.csv"
with open(output_file, "w") as f:
    f.write("rep,pitype,biastype,method,mutationtype,mutationrate\n")
    
# Define a list of mutation rates we want to obtain. This makes parsing more flexible
mutation_rates = ["AC", "AT", "CG", "CT", "GT"]

# First, we us the `os` module to list all the files in the current directory
files = os.listdir(".")

# Now, we loop over the files. However, there are lots of other files in this directory that we do not want to parse, so we must make sure to only parse relevant files.
for file in files:
    
    # We only want to parse certain files. We can check that the file name is acceptable, and parse it at the same time!
    # Extract information from the file title, so that we can ultimately save it in our final .csv file. Remember, files are named like this: rep2_vertrho_unequalpi_bias_FUBAR1_nucfit.txt
    find_file = re.match(r"rep(\d+)_vertrho_(\w+)_(\w+)_(\w+)_nucfit.txt", file) # Execute regular expression exact match on this file name
        
    if find_file:   # Did we have a match to this regex?       
            
        # Save information for writing to a file. All captured groups are strings!!
        replicate = find_file.group(1) # Capture first parenthesis group
        pitype    = find_file.group(2) # Capture second parenthesis group
        biastype  = find_file.group(3) # Capture third parenthesis group
        method    = find_file.group(4) # Capture fourth parenthesis group
        
        # Parse file for the mutation rate information by reading in entire file
        with open(file, "r") as handle:
            file_contents = handle.read()
        #print file_contents
        # Use re.findall to find all matches 
        mutations = {}
        find_mutation = re.findall(r"global (\w\w)=(\d+\.\d+);", file_contents) # Search whole file for all occurrences of this regex. When we match with re.findall, a list of TUPLES is returned!
        #print find_mutation
        if find_mutation:
            for entry in find_mutation: # Each entry is a tuple of captured information. The .group() is NOT used with re.findall
                type = entry[0]
                rate = entry[1]
                mutations[type] = rate
        
        # Assert that we have found all the mutation rates we wanted
        assert(len(mutations) == len(mutation_rates)), "\nMissing some mutation rates!"
        
        # Save this line of information to our output csv, by APPENDING! We will write a line for each mutation rate.
        with open(output_file, "a") as handle: # Note the "a" flag!!!
            full_lines = ""
            shared_info = replicate + "," + pitype + "," + biastype + "," + method # Each line will have some shared information, so we avoid mistakes by only defining it once
            for r in mutations:
                full_lines += shared_info + "," + r + "," + mutations[r] + "\n"
            handle.write(full_lines)
        
        
    else:
        print "The file %s will not be searched." %file
            







