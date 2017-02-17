---
layout: post
title: "Python IV: File Input/Output and Parsing"
instructor: Claire
permalink: /python4_fileio/
materials: files/python4.zip
---

## Dealing with files

Much of your time will be spent manipulating a file in some way, for example, running a calculation, plotting, or reformatting data.


1. Calculating distributions of sequence lengths
2. Making a new summary column for a data table 
3. Discuss

I'm going to demonstrate a few different ways to open and look at files, and we can talk about when to use each one. 


### Method 1: Line by line parsing

Here's an example of a script to read a list of species and locations and split into east and west coast samples. 

I have an input file of mice and their geographic origin, and I want to separate into two files of mice from the east coast and from the west coast. 


identified_samples.txt
---

mouse1 california
mouse2 maryland
mouse3 new_york
mouse4 oregon

sort_coasts.py
{% highlight python %}

    westcoast = ['california', 'oregon']
    eastcoast = ['maryland', 'new_york']
    
    #Stage output files to write to
    
    west_output = open("westcoast_samples.csv", "w") # Staging a new file to write to
    east_output = open("eastcoast_samples.csv", "w") # Staging a new file to write to
    
    #Stage input file we're getting data from
    input_handle = open("identified_samples.txt", "r") # Open as read-only

    #.readlines() makes each line in a file an element of a list

    data = input_handle.readlines() # Read contents of file and save to contents variable

    #data looks like ['mouse1 california\n', 'mouse2 maryland\n', 'mouse3 new_york\n', 'mouse4 oregon\n']     

    for raw_line in data:
        #The first line looks like: 'mouse1 california\n'
    
        line = raw_line.strip("\n") #The end line character of a line is invisible, but generally you get rid of it right away
    
        #The formatted line looks like: 'mouse1 california'

        samp_loc = line.split(" ")

        #The listified line looks like ['mouse1', 'california']
    
        #Check where the sample comes from and save it to the appropriate file
        if samp_loc[1] in westcoast:   
    
            west_output.write(raw_line)
    
        elif samp_loc[1] in eastcoast:
    
            east_output.write(raw_line)
     
    
    input_handle.close() # Close file when finished (important!!)
    east_output.close()
    west_output.close()

{% endhighlight %}


### Method 2: Pandas dataframe

Pandas is a package for looking at data in a table format
You can imagine each pandas dataframe as an excel sheet, with rows and columns and values

{% highlight python %}
    import pandas as pd

    westcoast = ['california', 'oregon']
    eastcoast = ['maryland', 'new_york']


    df = pd.read_table("identified_samples.txt", sep=" ", header=None)
    print("raw dataframe")
    print(df)
    
    #Give the columns names
    # You could also just use columns numbers, but I like to name my columns
    df.columns = ['ID', 'location']
    print("with named columns")
    print(df)
    
    #Filter values.
    #Syntax is 'get rows where it's true that the value in 'location' is in the list westcoast'
    west_df = df[df['location'].isin(westcoast)]
    east_df = df[df['location'].isin(eastcoast)]
    
    west_df.to_csv('westcoast_samples.csv', index=False, header=False)
    east_df.to_csv('westcoast_samples.csv', index=False, header=False)
{% endhighlight %}


# Adding command line input.

So far, I hard coded these filenames into my scripts.

What if I want an all purpose script that I can apply to any file without having to change the script?

like: $ python sort_coasts.py identified_samples_february.txt 

### Method 1: 'sys' module

With sys, anything you put after the python x.py is stored as a list that you can then access.

{% highlight python %}
    import sys

    filename = sys.argv[1]

    input_handle = open(filename, sep=" ")
{% endhighlight %}


### Method 2: 'argparse'

argparse is a module that let you get a lot more control over the options you give to a script

What if I want to add an optional option to tell the program what the delimiter of the input file is?

ex. $ python sort_coasts.py identified_samples_march.txt --sep=','

{% highlight python %}
    import argparse
 
    parser = argparse.ArgumentParser(description='A function to divide samples by geographic origin into new files')

    parser.add_argument('filename', action="store", type=str,  help="one group per line")
    parser.add_argument('--sep', action="store", dest="separator", type=str, default=' ', required=False, help="separator for input file")
    inputs = parser.parse_args()
    df = pd.read_table(inputs.filename, sep=inputs.separator, header=None)



{% endhighlight %}


## File parsing ##

Several examples of file parsing are available in [files](files/python4_files_io/). Please go ahead and download these files. 


The file `parse_delimited.py` contains examples for parsing and extracting information from csv and tab-delimited files (AbilAhuG_uniprot_blastx.txt and AbilAhuG_uniprot_blastx.csv). Note that these are the same file, except one is tab-delimited and one is comma-delimited.


The `parse_hyphy.py` file has four versions of a script that custom parses an output file from the program Hyphy. This is so you can see how writing a script progresses as it is refined.


## Homework ##

The file `AbilAhuG_uniprot_blastx.csv` has a few columns with poorly-formatted data. We want to fix these columns and print to a new file. Starting with some of the commands in the file `parser_delimited.py`, do the following:

- Read in the whole file and save it as a list (or, if you choose, iterate over file lines with a for loop)
- Remove the last column ('N/A') from each row
- Split the second to last column (e.g. "Keratin, type I cytoskeletal 16 OS=Mus musculus GN=Krt16 PE=1 SV=3") by Gene name, organism, gene code, and PE, SV values. You will have to be somewhat creative in how you do this. Think about using string indexing and/or the pandas module. Converted column format should read: "Keratin, type I cytoskeletal 16", "Mus musculus", "Krt16", "1", "3". Think about what is constant in this column throughout all rows and use this to help you parse.
- Create a new header for the file based on the new column contents
- Write the altered file contents to a new csv file

Bonus: Write your own custom parser for a file type you deal with often.





#### More variants of file IO

Open and close with open() and close()
{% highlight python %}  
    file_handle = open("important_file.txt", "r") # Open as read-only
    contents = file_handle.readlines() # Read contents of file and save to contents variable
    file_handle.close() # Close file when finished (important!!)
{% endhighlight %}

Open with the *with* control flow command. The file automatically closes outside the scope of the with. This is what I prefer to use.
{% highlight python %}
    with open("important_file.txt", "r") as file_handle:
        contents = file_handle.readlines()
{% endhighlight %}

The `open()` function takes two arguments: i) the *name* (including full or relative path!) of the file to open, and ii) the *mode* in which the file should be read. Modes include read-only (`"r"`), write-only (`"w"`), append (`"a"`), or read+write (`"rw"` for PCs and `"r+"` for Mac/Linux). Writing and appending are similar to the bash operators `>` and `>>`; write will overwrite the file, but append will add to the bottom of an existing file. Note that if you open a file for writing (or appending), that file doesn't need to exist already, and a new file will be created with the specified name. Alternatively, if you attempt to open a file that does not exist for reading, you'll receive an error message.

{% highlight python %}
    # Open a file for writing, and write to it
    file_handle = open("file_to_fill.txt", "w") # Open file for writing
    file_handle.write("I'm writing a sentence to this file!")
    file_handle.close()
{% endhighlight %}

Open a file for appending, and append text to it
{% highlight python %}
    file_handle = open("file_to_fill.txt", "a")
    file_handle.write("I'm writing another line to this existing file!")
    file_handle.close()
{% endhighlight %}


## Looping over file contents ##

When interacting with files, we usually want to examine and perform computations with the file content. To do this, we need to read in the file contents after opening the file. There are two basic file methods, `.readlines()` and `.read()`, that exist in native Python for this purpose. Both of these read in the entire file and save it either as a list (using newline characters to separate lines) or as a long string. If you have a large file you may just want to loop through it line by line without using either of these methods.


## Other ways to do it
{% highlight python %}
    # Read file line-by-line with .readlines() [Note that this is slow for *MASSIVE* files because it reads in and stores the whole file]
    with open("file.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print line
        # To loop another time, you must direct the readlines iterator to start from the top! The same would go for .read().
        f.seek(0)
        for line in lines:
            print line
            
    # Read file as one line, and then break into separate lines using the newline character
    with open("file.txt", "r") as f:
        contents = f.read()
        contents_list = contents.split("\n") # Split file contents on newline character
        for line in contents_list:
            print line
            
    # To go line by line, you could also use a simple for loop. This avoids saving the whole file.
    with open("file.txt", "r") as f:
        for line in f:
            print line
            
{% endhighlight %}

