---
layout: post
title: "Python II: Control Flow"
instructor: Claire
permalink: /python2_controlflow/
materials: files/python2_cheatsheet.pdf
---

### Today's Goals
1. Broadly understand the importance of logical decision making in computation
2. Become familiar with for loops, if/else, and while statements
3. Continue to use print statements to check output
4. Try out list comprehensions


#### First, some useful tools
- using `%` notation in print statements makes for better output

	%d: insert number here <br>
	%f: insert float here <br>
	%s: insert string here <br>

{% highlight python %}
>>> name="Rebecca"
>>> print "My name is %s." % (name)
My name is Rebecca.

>>> print "Two divided by 5 is %f" %(2.0/5)
Two divided by 5 is 0.400000
>>> print "Two divided by 5 is %0.1f" %(2.0/5)
Two divided by 5 is 0.4
>>> print "Two divided by 5 is %d" %(2.0/5)
Two divided by 5 is 0

{% endhighlight %}

- `random` module is useful for generating fake data

{% highlight python %}
>>> import random
>>> dna = ["A","C","T","G"]
>>> genome=dna*250
>>> random.shuffle(genome)
>>> genome
['A', 'A', 'A', 'A', 'T', 'C', 'T', 'A', 'T', 'G', 'G', 'C', 'A', 'C', 'C', 'G', 'C', 'A', 'C', 'T', 'A', 'A', 'T', 'G', 'C', 'G', 'A', 'etc']
>>> "".join(dna) # method to convert list to string
'AAAATCTATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCTGCTTTTAAGGCGCGAACATACGCTGGTGCTAAGCCCGCTAGTTCAGCACCAATCGACTGTTGCAGATAAGTTCATCTGGTCAAAGATCATTCACACAGTAAGATATTGACCGGGAGCCTAGATCTCCAGATGAACGCTGTGGCGCACCCTCGATTCGCGGGGCGATCCAGAAGCCATGAGGAATATAGTTATCTCGTCTGCCCGTATACCGCGCTCCGTACCAATGCACCTTAATATCGAGGCCGGACACGAGACGTACTTCATTTGACCACGCGGTAGCAGGTTCGTGGCATATGAGCCAGATAGGAGTGTGGCTATCCCCAAGGTCCTACAGGTCACTAGACTTAGCTAGTGTTGCAGTTGGGTGGGCACAATGACACCCGGCAGGAGAGCATTTGGCCGCGTGTTTCGACATTCCCTTTAATGAAAGACTCGCCAGCTCTAATACCACTCAACTTTTACCTCTTTGGAAGACTATTATTAAAGATGCCTACTCAAGGTGGATTTCGACACGGTGCGGTCATGTAATCTCGACACCATGGGTTGCAGTTGCGTTCAGTAACTCAAGACTCTGCCATTCGACTGGACACAGATAAGATGGTCATACGCTCGGTACCGATGAGTTCCTAATCTATCGGAACTAAAGCTCGAACGTATCGCATACCACCATGCCGTTGGTGCTAACGAACTTCTCGGCGCCTGATAGACAGGTTGGAATACTGCTCGGCGAATATCATCAATACAATAAACCGTGCGTTC'
>>> 
{% endhighlight %}

<br><br>

# Decisions and conditions: For, If, While

Remember: we program for Repeatability, Speed, and Automation. Using decisions and conditions we can automate a logical procession of actions.


## For loops

A for loop is a way to iterate through a list, range, dictionary, string, etc. Use it for whenever you are repeating something.

{% highlight python %}
for item in thing: #line leading to an indented block ends with a colon
	do something with item #indenting blocks of code indicates how the program flows
	do other actions with item
	#return to for statement and move to next item
continue with other commands
{% endhighlight %}

Ok, let's test this out with the print statement. Use this statement in for loops often to check for errors and make sure that everything is working as you would expect.

{% highlight python %}
>>> dna='AGCT'
>>> for item in dna:
...     print item  # here the word "item" is completely arbitrary. 
... 
A
G
C
T

{% endhighlight %}

Let's try something a bit more complicated. Here we can do a repeat of a mathematical operation on items in a list. Note that the `x` in `for x in thing` can be whatever you want, you just have to be consistent within the loop.

{% highlight python %}
>>> sequences=['AGTCTA','AGTCAGTCAGTCAGT','ACTAGCTAGCTA','ACGTCAGTATCGTATTTTA','ACAGTCAGTGATCA','AGT','AGCTAGCTAGCTACGATGCTAGCTAGC'] #create our list
>>> for seq in sequences: #for each sequence in the list
...     length=len(seq) #calculate the length
...     Gcontent=seq.count('G') #count the number of Gs
...     Ccontent=seq.count('C') #count the number of Cs
...     Tcontent=seq.count('T') #count the number of Ts
...     Acontent=seq.count('A') #count the number of As
...     GCcontent=(Gcontent+Ccontent)/float(length) #calculate the GC content
...     print "GC content of %s is %f" %(seq,GCcontent) 
... 
GC content of AGTCTA is 0.333333
GC content of AGTCAGTCAGTCAGT is 0.466667
GC content of ACTAGCTAGCTA is 0.416667
GC content of ACGTCAGTATCGTATTTTA is 0.315789
GC content of ACAGTCAGTGATCA is 0.428571
GC content of AGT is 0.333333
GC content of AGCTAGCTAGCTACGATGCTAGCTAGC is 0.518519

{% endhighlight %}

But, if you see in this code, there is a calculation that is repeated four times, so we should also use a for loop in this case too.

{% highlight python %}
>>> GCdict={} #create an empty dictionary that we will fill with GCcontent values
>>> for seq in sequences:
...     seqdict={} #create another empty dictionary to *temporarily* store ACGT counts
...     length=len(seq)
...     for nuc in ['A','G','C','T']: #for each nucleotide
...             seqdict[nuc]=seq.count(nuc) #count the number of nucleotides in the sequence
...     GCcontent=(seqdict['G']+seqdict['C'])/float(length) #what happens if you don't do float()?
...		GCdict[seq]=GCcontent
...     print "GC content of %s is %f" %(seq,GCcontent)
... 
GC content of AGTCTA is 0.333333
GC content of AGTCAGTCAGTCAGT is 0.466667
GC content of ACTAGCTAGCTA is 0.416667
GC content of ACGTCAGTATCGTATTTTA is 0.315789
GC content of ACAGTCAGTGATCA is 0.428571
GC content of AGT is 0.333333
GC content of AGCTAGCTAGCTACGATGCTAGCTAGC is 0.518519

{% endhighlight %}

Now we can check what is in our dictionary.

{% highlight python %}
>>> for key in GCdict:
...     print '%s: %f' %(key,GCdict[key])
... 
ACAGTCAGTGATCA: 0.428571
ACGTCAGTATCGTATTTTA: 0.315789
ACTAGCTAGCTA: 0.416667
AGTCAGTCAGTCAGT: 0.466667
AGCTAGCTAGCTACGATGCTAGCTAGC: 0.518519
AGTCTA: 0.333333
AGT: 0.333333

{% endhighlight %}

A quick note: you can do for loops in bash too!

{% highlight bash %}
#for file in a list of text files in this directory, print filename
for i in *.txt; do echo $i; done
#for file in a list of .fasta files in this directory, cat file to end of newseqs.fasta file
for i in *.fasta; do cat $i >> newseqs.fasta; done
{% endhighlight %}

And in many many other languages: http://rosettacode.org/wiki/Foreach


## if statements

- IF

If statements are used to test if your variable is true for some logical condition in order to determine what the program should do next. These are super handy and are essentially how you get the computer to make decisions for you.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
continue with main commands
{% endhighlight %}

{% highlight python %} 
>>> numbers=range(20)
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> if sum(numbers) >= 20:
...     print "Sum is greater than 20!"
... 
Sum is greater than 20!

>>> if sum(numbers) >= 20:
...     print "%d is greater than 20!" % (sum(numbers))
... 
190 is greater than 20!
>>> 

{% endhighlight %}

- IF ELSE

Adding an else to your statement allows the computer to decide what to do when the conditional is False.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
else:
	do that command
{% endhighlight %}


{% highlight python %}
>>> dna='AGTCTGTAGTCTATAGA'
>>> GC=(dna.count('G') + dna.count('C'))/float(len(dna))
>>> if GC > 0.5:
...     print "GC content (%.2f) is higher than 0.50" %GC
... else:
...     print "GC content (%.2f) is lower than 0.50" %GC
... 
GC content (0.35) is lower than 0.50

{% endhighlight %}



You can do nested if/else statements.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
else:
	if logical condition == True: 
		do this command  
		do this command
	else:
		do this command
{% endhighlight %}


But there is a better way:

- IF ELIF

The if/elif statement can be used when you would otherwise use multiple nested if/else statements. They are performed *in order* and will not go through all of the options if one before the end is True.


{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
elif other logical condition == True:
	do this command
elif other logical condition == True:
	do this command
else:
	do this command
{% endhighlight %}


{% highlight python %}
seqs=['AUUGACAUCGAUCGA','AGACTGATCGATCTAG','JIEONONE']
for seq in seqs:
	if 'U' in seq:
		print '%s is RNA' %seq
	elif 'T' in seq:
		print '%s is DNA' %seq
	else:
		print '%s might be a protein' %seq
{% endhighlight %}


- IF and FOR together!

Using conditionals and for loops together makes your code very powerful. 


{% highlight python %} 
# Print 25-bp kmers from a randomly generated sequence
# (a kmer is an overlapping segment of a DNA sequence)
import random
>>> dna='AGCT'
>>> random.choice(dna)
'G'
>>> seq=[]
>>> for i in range(100):
... 	seq.append(random.choice(dna))
...
>>> seq="".join(seq)
>>> seq
'CGCGCAAAGACCGTTTTTGGCTGCCCAGGATCTCCCGGCTAGGGTATGAGGCCACCAAAAACAGACGGTTCGGCCCGGTATTATAAGAATATCCTAGGAA'
>>> for i in range(len(seq)): # why use range(len(seq)) rather than len(seq)?
...     print seq[i:i+25]
... 
CGCGCAAAGACCGTTTTTGGCTGCC
GCGCAAAGACCGTTTTTGGCTGCCC
CGCAAAGACCGTTTTTGGCTGCCCA
GCAAAGACCGTTTTTGGCTGCCCAG
CAAAGACCGTTTTTGGCTGCCCAGG
AAAGACCGTTTTTGGCTGCCCAGGA
AAGACCGTTTTTGGCTGCCCAGGAT
AGACCGTTTTTGGCTGCCCAGGATC
GACCGTTTTTGGCTGCCCAGGATCT
ACCGTTTTTGGCTGCCCAGGATCTC
CCGTTTTTGGCTGCCCAGGATCTCC
CGTTTTTGGCTGCCCAGGATCTCCC
GTTTTTGGCTGCCCAGGATCTCCCG
TTTTTGGCTGCCCAGGATCTCCCGG
TTTTGGCTGCCCAGGATCTCCCGGC
...
ATTATAAGAATATCCTAGGAA
TTATAAGAATATCCTAGGAA
TATAAGAATATCCTAGGAA
ATAAGAATATCCTAGGAA
TAAGAATATCCTAGGAA
AAGAATATCCTAGGAA
AGAATATCCTAGGAA
GAATATCCTAGGAA
AATATCCTAGGAA
ATATCCTAGGAA
TATCCTAGGAA
ATCCTAGGAA
TCCTAGGAA
CCTAGGAA
CTAGGAA
TAGGAA
AGGAA
GGAA
GAA
AA
A
# but we don't want kmers that are less than 25bp!

>>> for i in range(len(seq)):
...     if len(seq[i:i+25]) < 25:
...             print 'too short! Exiting!'
...             break  # if it does not meet this condition, for loop ends.
...     else:
...             print seq[i:i+25]
... 
CGCGCAAAGACCGTTTTTGGCTGCC
GCGCAAAGACCGTTTTTGGCTGCCC
CGCAAAGACCGTTTTTGGCTGCCCA
GCAAAGACCGTTTTTGGCTGCCCAG
CAAAGACCGTTTTTGGCTGCCCAGG
AAAGACCGTTTTTGGCTGCCCAGGA
AAGACCGTTTTTGGCTGCCCAGGAT
AGACCGTTTTTGGCTGCCCAGGATC
GACCGTTTTTGGCTGCCCAGGATCT
ACCGTTTTTGGCTGCCCAGGATCTC
...
TCGGCCCGGTATTATAAGAATATCC
CGGCCCGGTATTATAAGAATATCCT
GGCCCGGTATTATAAGAATATCCTA
GCCCGGTATTATAAGAATATCCTAG
CCCGGTATTATAAGAATATCCTAGG
CCGGTATTATAAGAATATCCTAGGA
CGGTATTATAAGAATATCCTAGGAA

>>> for i in range(len(seq)):
...     if len(seq[i:i+25]) < 25:
...             print 'too short! continuing'
...             continue # instead of ending the for loop, continue will just skip this one iteration
...     else:
...             print seq[i:i+25]
... 

{% endhighlight %}


- Important tip: You can make a dictionary without knowing/defining a priori what they keys are

{% highlight python %}
>>> dictionary={}
>>> seq='AGTAGTATTTGAGAGTTTAGATATAG'
>>> for letter in seq:
...     if letter in dictionary.keys(): #if the key already exists
...             dictionary[letter]+=1 #augment the value by one
...     else:
...             dictionary[letter]=1 #or else, make the new key
... 
>>> dictionary
{'A': 9, 'T': 10, 'G': 7}

{% endhighlight %}


## While

While loops repeat until some condition becomes False. Be careful as they are prone to infinite loops. If you get caught in one, hit Ctrl+C.

{% highlight python %}
while condition == True:
	do this command
	do that command
continue with normal commands
{% endhighlight %}

Example script with while loop:
{% highlight python %}
import time #useful module for printing timestamps and counting time units during your scripts
i = 5
while i > 0:
        time.sleep(1) #wait one second before proceeding
        i-=1
        print i
print "Time is up!"
{% endhighlight %}

outputs:
{% highlight bash %}
python timer.py
5
4
3
2
1
Time is up!
{% endhighlight %}

While loops can ensure that user input is in the right format. They are also useful when you want to manipulate part of the conditional that is being used within the loop.

Try using this program, which has a test for user input using a while loop:
{% highlight python %}
x=int(input("Give me a number from 1 to 10: ")) #accepts user input, converts to an integer
while x not in range(0,11): #if input was not number between 1 and 10
        print "That's not a number between 1 and 10 :(" #prints a complaint
        x=int(input("Give me a number from 1 to 10: ")) #asks for a new number
print "Thanks!" #thanks the user for being a nice user
{% endhighlight %}

Here we manipulate part of the conditional (x) within the loop. Could you do this with a for loop? Why is the last number less than 40?
{% highlight python %} 
>>> x=2000
>>> while x > 40:
...     x=x/4
...     if x%2 == 0:
...             print "%d is even!" %x
...     else:
...             print "%d is not even!" %x
...             x+=5
... 
500 is even!
125 is not even!
32 is even! 

{% endhighlight %}




## List comprehensions

List comprehensions are faster ways to execute loops that result in lists. Your typical loop structure is shown below followed by the comprehension structure.

{% highlight python %}
list1=[] #make empty list
for item in thing:
	list1.append(item)	

list1 = [item for item in thing]
{% endhighlight %}

examples:

{% highlight python %}
# make a list of 0 to 19, cubed
# LOOP
>>> mylist=[]
>>> for i in range(0,20):
...     mylist.append(i**3)
... 
>>> mylist
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

# COMPREHENSION
>>> mylist=[i**3 for i in range(0,20)]
>>> mylist
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

# from the for loop above, make a random 100-bp DNA sequence
import random
# LOOP
>>> dna='AGCT'
>>> seq=[]
>>> for i in range(100):
... 	seq.append(random.choice(dna))
...
>>> seq=''.join(seq)

# COMPREHENSION
>>> seq=''.join([random.choice(dna) for i in range(100)])

# more comprehension examples
# make a list of sequence lengths
>>> sequences=['AGTCTA','AGTCAGTCAGTCAGT','ACTAGCTAGCTA','ACGTCAGTATCGTATTTTA','ACAGTCAGTGATCA','AGT','AGCTAGCTAGCTACGATGCTAGCTAGC']
>>> mylist=[len(seq) for seq in sequences]
>>> mylist
[6, 15, 12, 19, 14, 3, 27]

# make a list of sequences and their lengths
>>> mylist=[(seq,len(seq)) for seq in sequences]
>>> mylist
[('AGTCTA', 6), ('AGTCAGTCAGTCAGT', 15), ('ACTAGCTAGCTA', 12), ('ACGTCAGTATCGTATTTTA', 19), ('ACAGTCAGTGATCA', 14), ('AGT', 3), ('AGCTAGCTAGCTACGATGCTAGCTAGC', 27)]

# turn into dictionary
>>> dictionary=dict(mylist)
>>> dictionary
{'ACAGTCAGTGATCA': 14, 'ACGTCAGTATCGTATTTTA': 19, 'ACTAGCTAGCTA': 12, 'AGTCAGTCAGTCAGT': 15, 'AGCTAGCTAGCTACGATGCTAGCTAGC': 27, 'AGTCTA': 6, 'AGT': 3}

{% endhighlight %}





# Python 2 Homework

1. Create your own python script that creates a genome with equal base frequencies (but randomly shuffled) of a *user-requested* size. Hint: use `input()`, `random`, and some of the text from the lesson.

2. Now rewrite that code into a for loop that allows you to create 30 sequences of length 100. Save them in a list.

	- Using a for loop and string indexing, print the position of the first T for each sequence in a readable format (use %d with the print statement).
	- Now add a variable to save this number within the loop rather than printing it.
	- Use this variable and the `string` module to cut the part of the sequence that comes before that index out of each sequence. 
	- Repeat the last step but add an if statement so that it only cuts the sequence if the T is one of the first three nucleotides.
	
3. Write a for loop using your sequences that checks whether the sequence 'AAAA' is in them, and if it is, adds one to a counter. At the end of the loop, use the print statement with %d to state how many of your sequences had this subsequence.

