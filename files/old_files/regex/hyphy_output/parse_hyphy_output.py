"""
    Regular Expressions example script.
    
    All files name "rep..._nucfit.txt" in this directory are **real files from Stephanie's research**, produced by the software HyPhy (https://github.com/spond/hyphy). Each file, which is named according to the dataset it describes, contains information about a fitted model of sequence evolution.
    This script will parse all .txt files in the working directory to obtain the nucleotide mutation rate for "AC" (A to C or C to A), which appears in each file like this:
        global AC=0.3562821267007032;
    All information will be saved to a single .csv file for future use (e.g. data analysis in R!).
    
    Importantly, we do not know on which line this information appears, and we do not know how many digits long it is. We do know how the line is formatted, which informs our regular expression usage.


    For an extra challenge, we can parse each file to obtain **all** mutation rates, for example all of this information:
        global AC=0.3562821267007032;
        global AT=0.3561898444276437;
        global CG=0.266526902373061;
        global CT=1.502997839429121;
        global GT=0.2632076545083971;
    A script to perform this task is in parse_hyphy_output_extended.py .
    
"""
# Import needed modules
import os
import re

desired_mutation_rate = "AC" # Avoid hard-coding AC in the script, in case you want to change later!!!

# Define the final output file name and write a header to the file
output_file = "hyphy_information.csv"
with open(output_file, "w") as f:
    f.write("rep,pitype,biastype,method," + desired_mutation_rate + "\n")


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
        
        # Parse file for the AC information ONLY
        with open(file, "r") as handle:
            for line in handle:
                find_mutation = re.search(r"^global " + desired_mutation_rate + "=(\d+\.\d+);", line) # Search each file line for this regex
                if find_mutation:
                    mutation = find_mutation.group(1) # Again, this is a string! If we want to manipulate it as a number, we have to re-cast to float
                    break # Stop looping over file once we've found the information we need, to save time and memory
        
        # Save this line of information to our output csv, by APPENDING!     
        with open(output_file, "a") as handle: # Note the "a" flag!!!
            handle.write(replicate + "," + pitype + "," + biastype + "," + method + "," + mutation + "\n")
        
        
    else:
        print "The file %s will not be searched." %file
            







