---
layout: post
title: "Building Analysis Pipelines"
instructor: Sean
permalink: /pipelines/
materials: files/pipelines.zip
---
Parts of this lesson borrow heavily from "Bioinformatics Data Skills" by Vince Buffalo.  You can buy it here: http://shop.oreilly.com/product/0636920030157.do **And you should because it's awesome**

## The python `sys` module

The `sys` module interacts with the python interpreter. This module primarily comes with certain **variables** (rather than functions) which are particularly useful, two of which are described below.

### Passing command-line arguments `sys.argv`
Often, you'll want to pass input arguments to a script. All input arguments are stored in the variable `sys.argv` (note that you must import the `sys` module!). For example, you might have a script called `calc_dna.py` which performs certain calculations on a sequence data file, but each time you run the script, you might want to process a different file. One option to pass the file name as an input argument: `python calc_dna.py inputfile.fasta`, where `inputfile.fasta` is the single command-line argument. If you've loaded the `sys` module, all command line arguments will be stored in `sys.argv`:

Assume the following code is included in the script calc_dna.py.
{% highlight python %}
import sys
print sys.argv
{% endhighlight %}
From the command line you run `python calc_dna.py inputfile.fasta` and get back: <br>
`['calc_dna.py', 'inputfile.fasta']`

Notice that the first entry in `sys.argv` is the name of the script. After this come all command line arguments! In addition, all `sys.argv` entries will be **strings**. So remember that if you want to use an input argument as a number, you must convert it to a float or integer.

Generally, you should save the input arguments to a new variable inside the script:
{% highlight python %}
import sys
infile = sys.argv[1]
{% endhighlight %}

Error checking is often very useful here; you might have a script which **requires** two command line arguments. For instance, let's say you have a script (which does something..) which takes a file name and a number as its two arguments. To ensure that this always happens, help yourself out with assertion statements:

{% highlight python %}
import sys
# sys.argv must be of length 3 (script name, inputfile, number)
# print a usage statement if arguments not provided or provided incorrectly
assert( len(sys.argv) == 3 ), "Usage: python my_script.py <inputfile> <number>"
infile = sys.argv[1]
number = int( sys.argv[2] ) # remember to convert from string to int, as needed!
{% endhighlight %}

### Editing the path with `sys.path`

You can view everything in python's path by printing the contents of the list `sys.path`. This variable will you tell which directories on your computer that the current python interpretter is able to access. To edit this path in place, for instance by adding a directory to the path, simply use `.append()`:
{% highlight python %}
import sys
sys.path.append("/path/to/directory/that/python/should/know/about/")
{% endhighlight %}

<br><br>
## The python `os` and `shutil` modules

The `os` and `shutil` modules are useful for interacting with your computer's operating system (typically UNIX). With these modules, you can run commands from your python script which are analogous to UNIX commands like `cd` and `pwd`.
<br>Some examples:

Module | Command  |  Description | Unix equivalent | Example
-------|----------|--------------|-----------------|--------
`os` | `os.listdir`| List all items in a given directory | `ls` | `os.listdir("/directory/of/interest/")`
`os` | `os.remove` | Remove a file | `rm` | `os.remove("i_hate_this_file.txt")`
`os` | `os.rmdir` | Remove a directory | `rm -r`| `os.rmdir("/i/hate/this/directory/")`
`os` | `os.mkdir`  | Create a new directory | `mkdir` |`os.mkdir("/path/to/brand/new/directory/")`
`os` | `os.mkdirs`  | Create many new directories | `mkdir`|`os.mkdir("/path/to/a/brand/new/directory/", "/path/to/another/brand/new/directory/")`
`os` | `os.chdir`  | Change directory where python is running | `cd` | `os.chdir("/another/directory/where/i/want/to/be/")`
`shutil` | `shutil.copy` | Copy a file | `cp` | `shutil.copy("old_file.txt", "new_file.txt")`
`shutil` | `shutil.move` | Move a file | `mv` | `shutil.move("old_file.txt", "new_file.txt")`

### Running external commands with `os`

You will often want to use Python scripting to automate analyses which use external programs or softwares. You can actually call these programs directly from your python script using the function `os.system()`. This function takes a single argument: the command you want to run (as a string). Anything that you could type into the command line can be given to `os.system`!

{% highlight python %}
# Create a multiple sequence alignment in MAFFT from python
import os
# Define input, output files
infile = "unaligned.fasta"
outfile = "aligned.fasta"
command = "mafft " + infile + " > " + outfile
os.system(command)
{% endhighlight %}

We can also incorporate `sys` to provide the input/output file names as arguments!
{% highlight python %}
# Create a multiple sequence alignment in MAFFT from python
import os
import sys

# Check and save input arguments
assert( len(sys.argv) == 3 ), "Usage: python align.py <inputfile> <outputfile>"
infile = sys.argv[1]
outfile = sys.argv[2]

# Run the alignment
command = "mafft " + infile + " > " + outfile
os.system(command)
{% endhighlight %}

Finally, you can check that the command has run properly by saving the output of `os.system()` (basically, save it to a variable). In UNIX, a returned value of 1 means an error occurred, but a returned value of 0 means everything went fine. Therefore, we want to make sure that `os.system()` returns a value of 0, by editing the last few lines:

{% highlight python %}
command = "mafft " + infile + " > " + outfile
aligned_properly = os.system(command)
assert(aligned_properly == 0), "MAFFT didn't work!"
{% endhighlight %}

#### Python is pretty great, if you're into that kind of thing.  We just talked about how to interface with bash from python.  Now lets talk about some of the amazing things you can do with bash.


# Part 2: useful UNIX/Bash one-liners: pipes, `sed`, `awk`, and more!

Why is Unix the language of bioinformatics?  Read about the Unix philosophy here: https://en.wikipedia.org/wiki/Unix_philosophy.  

### Do one thing and do it Well.

Bash is great for getting a quick look at your data and answering questions easily.  While you *can* do all of these things in python with what you've already learned, it's often far easier and quicker to use the huge ecosystem of Unix tools already available and heavily optimized (albeit quirky).
<br>
We're going to look at a lot of commands, so remember, you can always use `man` to look up the specifics of bash commands. Try `man ls` to look at all the options for `ls`.  Pressing `q` will return you to your terminal.

Lets review some basic bash commands:

#### We can use `head` to quickly look at the first lines in a file

~~~ console
head Mus_musculus.GRCm38.75_chr1.bed
~~~
You can change the number of lines returned with the `-n` argument.

#### `tail` is just like `head` but looks at the end of a file
~~~ console
tail Mus_musculus.GRCm38.75_chr1.bed
~~~

#### `history` shows you your recent shell commands
~~~ console
history
~~~

#### and `grep` is a powerful way to search files.
But Stephanie will cover `grep` in GREAT detail later, so we'll mostly just think of it as "find" for now.

~~~ console
history | grep tail
~~~

#### Welcome to the new world.  The new world of `|` or "pipes"
Piping allows you to redirect the output of one unix command to be the input of another command.  This is a *really* powerful idea and critical to effectively using Unix.  We'll come back to it.

#### `less` is a great way to inspect files.
Less actually starts a program that allows you to *view* text at the console.  You won't be able to edit it.  To quit `less` just press `q`.  `space` takes you to the next page, and `b` goes back.  

~~~ console
less contaminated.fasta
~~~

#### `wc` outputs the number of words, lines, and characters in the supplied file, or files
The argument `-l` restricts this to just lines, what we usually care about.

~~~ console
wc Mus_musculus.GRCm38.75_chr1.bed
wc Mus_musculus.GRCm38.75_chr1.bed contaminated.fasta   
~~~

So of course, you can imagine using this to answer some questions.

#### `cut` pulls out specific columns ("fields") from files
It uses tab as the separator by default

~~~ console
cut -f 2 Mus_musculus.GRCm38.75_chr1.bed | head -n 3
~~~
The `-f` argument specifies which column to keep

#### `column` then makes that output pretty to look at in the console

~~~ console
cat Mus_musculus.GRCm38.75_chr1.gtf | column -t
~~~
*Only* use for looking at data in the terminal.  If you output column to a file the variable number of spaces is a mess for other programs to parse.

## Now lets get to some Good Stuff

#### `sort` will, of course, "sort" plain text data.  But its syntax can be confusing, so get familiar with the man page.  

~~~ console
cat example.bed
sort example.bed
sort -k1,1 -k2,2n example.bed
~~~

Command   | Meaning| Example
----------|--------|---------
-b | ignore leading blanks | `sort -b filename > filename.sorted`
-r | reverse | `sort -r filename > filename.sortedr`
-k POS1 | sort by field/character indicated by POS1 | sort by field 2: `sort -k 2 filename` <br> sort by second character in field 2: `sort -k 2.2 filename`
-k POS1,POS2 | sort based on the characters from POS1 to POS2 | sort by characters in fields 2 and 3: `sort -k 2,3 filename` <br> sort starting with second character in field 2 up to and including field 3: `sort -k 2.2,3 filename`

#### `uniq` takes a file or standard input (from a pipe) and removes consecutive duplicates.  It's very simple, but you'll use it a lot.

~~~ console
cat letters.txt
uniq letters.txt
sort letters.txt | uniq
sort letters.txt | uniq -c
~~~

Command | Meaning | Example
-------|--------|---------
-c | prefixes lines with the number of times they occur | `uniq -c filename`
-d | prints only repeated lines | `uniq -d filename`
-u | prints only unique lines | `uniq -u filename > filename.unique`
-f N | skips N number of lines | `uniq -f 30 filename`

`sort | uniq` and `sort | uniq -c` are very commonly used in bioinformatics.  Combined with other unix tools like `grep` and `cut` they are outrageously powerful.

~~~ console
grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3 | sort | uniq -c
grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3 | sort | uniq -c | sort -rn
~~~

#### `awk` is a programming language onto itself.  We'll keep it (pretty) simple, though, and show how simple `awk` "one-liners" can be used as integral components of analysis pipelines.

`awk` statements follow the syntax of `pattern { action }`.  They can be very simple:

~~~ console
awk `{print $0}` example.bed
~~~

`awk` is designed to process columnar data (data separated by fields).  `$1` represents the first field, `$2` the second, etc.

~~~ console
awk '$3 - $2 > 18' example.bed
~~~

~~~
# example using HW csv file
# print columns 2 and 3
cat WEEK_06_python5_HW.csv | awk -F, '{ print ($2,$3) }'
~~~

~~~
# print columns 2 and 3, add a `tab` between the items
cat WEEK_06_python5_HW.csv | awk -F, '{ print ($2"\t"$3) }'
~~~

~~~
# print columns 1 and 2, adding in a `tab` between, a new field "newline", and a new line at the end
cat WEEK_06_python5_HW.csv | awk -F, '{print ($1"\t"$2 "\tnewline\n")}'
~~~

~~~
# more complicated, a for loop that prints each item
cat WEEK_06_python5_HW.csv | awk -F, '{for (i=1;i<=4;i++) {print ($i)}}'
# for each line, from items 1 until 4: `for (i=1;i<=4;i++)`
# print each item: `{print $i}`
~~~

#### Last but not least, lets talk about `sed`.  The Stream editor. Sed reads data from a file or standard input and can edit it a line at a time.    
This is mostly based on regular expression (which Stephanie will explain further), so again just think of it as a simple Find and Replace.

~~~ console
head -n 3 chroms.txt
sed 's/chrom/chr/' chroms.txt | head -n 3
~~~

* General pseudocode: `sed [-E] command/regex/replacement/optionalflag filename > newfile`
* My favorite pseudocode: `sed -E s/OLD/NEW/`
* Mac users must include `-E` to access regular expressions
* `sed` does not understand `\t` and `\n`, see below

~~~ console
# replace first instance of XX with YY for each line
sed s/XX/YY/ filename > newfile
~~~

~~~
# replace all instances of XX with YY
# - `g` flag means 'global' and searches for all instances of the pattern
sed s/XX/YY/g filename > newfile
~~~

~~~
# replace all instances of XX with YY and of AA with ZZ
# - `-e` flag lets you execute multiple sed commands at once
sed -e s/XX/YY/g -e s/AA/ZZ/g filename > newfile
~~~

~~~
# keep only letter and space characters ([a-zA-Z' ']*) that come before a different type of character in each line
# - must escape all () using `\`, ie: \([regex]\)
# - must put whitespace and replacement ('\1\2') in quotes, or else it is interpreted as a separate command
sed -E s/\([a-zA-Z' ']*\)\(.*\)/'\1'/ example
~~~

* To insert tabs (`\t`) you'll have to hit `ctrl + v`, then `Tab` while in the terminal environment
* For newline characters (`\n`), you have to code it directly into the line with `\ + enter`, for example:

```
sed -E s/\([0-9]\)/'\1\
'/ examplefile.txt
```

#### Reminder:  Unix and pipes are awesome.  There are computationally efficient and easy to debug.  They deserve to be a part of your workflow.  But what about when need to do something more?  A lot of things to a lot of files... lets talk about scripting in bash.

# Part 3: Bash Scripts for Pipelines

 Calling all of your shell scripts from Python isn't really efficient.  There's a fair bit of computational overhead when you 'call' the shell from within python.  If you have a python analysis script you want to run on a lot of files, it's better to write a script in bash than to wrap it all in python.  

A bash script is really just a list of commands.  By convention bash scripts end in `.sh` and can be run by typing:

~~~ console
sh my_first_script.sh
~~~

Okay take a look at `head my_first_script`.  How do you want to take a look?  What do you see?  A similar shebang to a python script, and then some parameters.  After the parameters, each line is a separate bash command.

Now lets look at using command line arguments in bash.  Try running the second script.

~~~ console
sh my_second_script.sh
#you can also run scripts like this, but you have to set them to be executable
chmod u+x my_second_script.sh
./my_second_script.sh firstarg secondarg thirdarg
~~~

So command line arguments are pretty easy.  What else is nice about bash scripts?

~~~ console
sh my_third_script.sh
sh my_third_script.sh 15
~~~

Now take a look at that script.  You can do conditionals and for loops in bash!  You can also do while and until loops, and complex conditional statements.  The syntax is weird, though (as in -ne instead of python's !=), so pay attention.  

Okay lets get a little bit more real.  Lets say you have a pipeline of 10 commands you need to run on a bunch of files.  Instead of going command by command and file by file, you can wrap all the commands into a single bash script and call that for each file.  Look at this:

~~~ console
sh a_realer_script.sh contaminated.fastq
sh a_realer_script.sh chroms.txt
~~~

You can of course write new files inside bash scripts using `>` or `>>` and even clean up intermediate files with `rm`.  

Why do we care?  It makes it much easier to make your analysis reproducible and consistent- by using scripts and pipelines, you can ensure you're treating your data in the same way each time.  And, mostly importantly:  It's easier!

There are many POWERFUL ways to expand your bash scripting- globbing, `find`, `xargs`, file arrays, and more!  Play around with it.  You'll be glad you did!
