import argparse

def organize_coasts(inputfile, separator):

    westcoast = ['california', 'oregon']
    eastcoast = ['maryland', 'new_york']

    #Stage output files to write to

    west_output = open("westcoast_samples.csv", "w") # Staging a new file to write to
    east_output = open("eastcoast_samples.csv", "w") # Staging a new file to write to

    #Stage input file we're getting data from
    input_handle = open(inputfile, "r") # Open as read-only

    #.readlines() makes each line in a file an element of a list

    data = input_handle.readlines() # Read contents of file and save to contents variable

    #data looks like ['mouse1 california\n', 'mouse2 maryland\n', 'mouse3 new_york\n', 'mouse4 oregon\n']     

    for raw_line in data:
        #The first line looks like: 'mouse1 california\n'
    
        line = raw_line.strip("\n") #The end line character of a line is invisible, but generally you get rid of it right away
    
        #The formatted line looks like: 'mouse1 california'

        samp_loc = line.split(separator)

        #The listified line looks like ['mouse1', 'california']
    
        #Check where the sample comes from and save it to the appropriate file
        if samp_loc[1] in westcoast:   
    
            west_output.write(raw_line)
    
        elif samp_loc[1] in eastcoast:
    
            east_output.write(raw_line)
     
    
    input_handle.close() # Close file when finished (important!!)
    east_output.close()
    west_output.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='A function to divide samples by geographic origin into new files')

    parser.add_argument('filename', action="store", type=str,  help="one group per line")
    parser.add_argument('--sep', action="store", dest="separator", type=str, default=' ', required=False, help="separator for input file")
    inputs = parser.parse_args()
    organize_coasts(inputs.filename, inputs.separator)


