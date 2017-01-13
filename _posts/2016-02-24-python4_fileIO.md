---
layout: post
title: "Python IV: File Input/Output and Parsing"
instructor: Becca
permalink: /python4_fileio/
materials: files/python4.zip
---


Now that you can make functions, it's time to learn how to use them to manipulate other files.

## Today's Goals ##
1. Read files line by line in python 
2. Write output from python to a file
3. Use the `sys` module to take arguments from the command line 
4. Use the `re` module *briefly* to search file contents
5. Use the `os` module to perform the same script on various files in a directory



## Opening and closing files ##
To interact with files in python, you must open the file and assign it to a variable - this is now a python file object. All operations on the contents of a file must be done using this variable (not the file name itself!). Once all operations are finished, the file must be closed. Importantly, your computer's operating system limits the number of files which can be open at once (type the command `ulimit -n` to the command line to see how many), so it is very important to always close files when you are finished.

There are two basic ways to open and close files. Note that these two chunks of code are equivalent in their output.

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

## The csv module

The **csv module** is a useful python module for parsing comma-separated files, tab-delimited files, or any files with delimited *fields*. The csv module provides functions for parsing a file which has already been opened using `open()`. Note that the `.reader()` method returns an *iterator* object, which is faster than .readlines(), but similar to for-looping over file contents.

{% highlight python %}
import csv

# Read a standard csv file.
with open("file.csv", "r") as f:
	reader = csv.reader(f)
	for row in reader:
 		print row

# Read a file with a different delimiter (e.g. tab)
with open("file.txt", "r") as f:
	reader = csv.reader(f, delimiter = '\t') # Specify the delimiter if it is not a comma!!
	for row in reader:
		print row
		
{% endhighlight %}

## File parsing ##

Several examples of file parsing are available in [python4_files](python4_files/). Please go ahead and download these files. 


The file `parse_delimited.py` contains examples for parsing and extracting information from csv and tab-delimited files (AbilAhuG_uniprot_blastx.txt and AbilAhuG_uniprot_blastx.csv). Note that these are the same file, except one is tab-delimited and one is comma-delimited.


The `parse_hyphy.py` file has four versions of a script that custom parses an output file from the program Hyphy. This is so you can see how writing a script progresses as it is refined.


You may want to use more regular expressions while parsing data. These are found in the **re module**, which I am not covering in detail today. **Regular expressions** are essentially flexible pattern-matching symbols (see the lesson Cheatsheet) for some commonly-used regex's. The `re` module, and indeed regular expressions in general, are extremely powerful and endlessly useful. Note that the `re` module has many, many more available functions associated with it (see the [re module documentation](https://docs.python.org/2/library/re.html)) beyond what is discussed here!! Several examples of `re` functions used to parse the file `mammal_dat.nex` are shown in the file `parse_mammals.py`.


## Homework ##

The file `AbilAhuG_uniprot_blastx.csv` has a few columns with poorly-formatted data. We want to fix these columns and print to a new file. Starting with some of the commands in the file `parser_delimited.py`, do the following:

- Read in the whole file and save it as a list (or, if you choose, iterate over file lines with a for loop)
- Remove the last column ('N/A') from each row
- Split the second to last column (e.g. "Keratin, type I cytoskeletal 16 OS=Mus musculus GN=Krt16 PE=1 SV=3") by Gene name, organism, gene code, and PE, SV values. You will have to be somewhat creative in how you do this. Think about using string indexing and/or the `re` module. Converted column format should read: "Keratin, type I cytoskeletal 16", "Mus musculus", "Krt16", "1", "3". Think about what is constant in this column throughout all rows and use this to help you parse.
- Create a new header for the file based on the new column contents
- Write the altered file contents to a new csv file using the `csv.writer()` method

Bonus: Write your own custom parser for a file type you deal with often.



