---
layout: post
title: "Advanced Bash"
instructor: Devon
permalink: /advanced_bash/
materials: 
---

# Advanced Bash Scripting

## Loops
Claire already introduced us to a simple for loop in Bash syntax, but let's revisit this to refresh our memories:

~~~
for i in 1 2 3 4 5; do
	echo $i
done
~~~

In this case, we have to spell out every number we wish to loop through. There is an easier way with command substitution, which uses backticks

~~~
for i in `seq 1 10`; do
	echo $i
done
~~~

In general, we can substitute any command between ` ` and use its output as input for another command. Consider this next example:

~~~
for DIR in `ls -d`; do
	cd $DIR;
	ls -la;
	cd ../;
done
~~~

This allows us to print all the files in every subdirectory that exists in our current directory. Cool, huh? Also quite useful sometimes when you have a more complex data and file storage system. 

OK, enough about for loops. What else is there?

~~~
COUNTER=0;
while [ $COUNTER -lt 10 ]; do
	echo The count is $COUNTER;
	let COUNTER=COUNTER+1
done
~~~

This is interesting - we have a new syntactical structure here: [], and -lt. In Bash, the brackets indicate a logical condition that will be evaluated to either True or False (called a Boolean value). In this case, the condition we want to meet is that our counter is -lt 10. But, what is -lt? Less than! Good job. 

There is a whole list of Bash conditional operators to learn, but you can find all of them online [here](http://tldp.org/LDP/abs/html/ops.html). 

The last loop we'll learn about, which is similar to the while loop, is 

~~~
COUNTER=20;
until [ $COUNTER -lt 10 ]; do
	echo The count is $COUNTER;
	let COUNTER-=1
done
~~~

This is simply another way of thinking about the countdown or count-up. It still specifies a conditional statement that is evaluated as T or F. Whereas the "while" loop continues until the conditional statement becomes False, the until loop continues until the conditional statement becomes true. This can be a useful way to structure certain operations you may wish to create. 

## Redirection

Another very useful Bash tool is called "redirection". Simply, this means we take the output of one process and turn it directly into input for another, without manually needing to restart the process each time. For example, say we wish to list all the files in our current directory that contain the string 'prot': proteome, protein, protozoan, etc. We would do this most efficiently like this: 

~~~
ls | grep "prot"
~~~

The "ls" command prints to the screen a list of all the current files in our working directory. This list is the output of the process "ls". The pipe \| then redirects this output to become the input of the grep process, which searches on the string "prot", and returns to the screen only those filenames with "prot", and no others. By itself, "ls" would not have been so specific. 

Another form of redirection uses >, and >>. The single caret takes the output of a process and prints it to a new file. The double caret >> appends, or adds, the output of the preceding process to the end of an existing file. 

Say I'd like to create a list of all the files containing the string "prot". 

~~~
ls | grep "prot" > protfiles.txt
~~~ 

This complex command combines two forms of redirection. You can build incredibly useful and complex commands yourself by taking advantage of these three operators. 

## Regex

Your lives are incomplete. I know you have been searching for something to fulfill that void in your hearts. Well, today is the day that void is filled...with regular expressions! Seriously, regex can change your life. It changed mine more than religion ever could. 

Here are two amazing sites to play with building your very own regular expressions. 
1) [regexr.com](http://regexr.com/)
2) [regex101.com](https://regex101.com/)

Trust me, these will be your favorite things. 

## File Manipulation with sed and awk

Two amazingly useful tools you will combine with your new knowledge of regex are sed and awk. These programs allow you to manipulate the contents of files without ever opening them, using pattern matching and potentially saving you hundreds of hours of having to go file by file manually correcting your mistakes. 

~~~
sed 's/pattern/replacement/g' file
~~~

This is the general form of a sed expression. However, this will exactly replace the string "pattern" with "replacement" in the entire file. But, sed is much more flexible than this, and can incorporate regex as well. Use [this site](https://www.gnu.org/software/sed/manual/html_node/Regular-Expressions.html) to fulfill all your sed regex desires. 

awk is similar to sed, but its syntax is different and it is better equipped for certain tasks, like column manipulation or row manipulation. 

~~~
awk '{ print $1 "\t" $2 }' file
~~~
will print the first and second columns of file, with a tab between them. Remember that awk is a language in and of itself, which is why we use '{}' to contain our arguments. 

Let's say we want to rearrange the columns in a file, using awk:

~~~
awk '{ print $2 "\t" $1 }' file
~~~

However, this is just going to print to our screen the reversed columns. How could we change this within our file? It's a bit more complicated...

~~~
awk '{ print $2 "\t" $1 }' file > file.tmp && mv file.tmp file
~~~

Not too bad, though, right?

## Simple batch file renaming

There exist many ways to rename a huge number of files in just a few lines. My favorite takes advantage of the z-shell, which is an alternative to Bash. You can switch to
z-shell by typing zsh at your prompt, and back to bash by typing bash.

Now, the trick to easy file renaming within the zsh is to use a command called zmv. But, first we need to load it using autoload.

~~
zsh
autoload -U zmv
~~

Once loaded, you can type zmv with some arguments specifying how to change your files. Let's take a quick and easy example. Say we have 1000 files named file_1.txt, file_2.txt, etc. We want to move the number to be before the word "file". This is super super easy with zmv. If all the files are in the same directory, you just have to type:

~~
zmv '(*)_(*).txt' '$2_$1.txt'
~~

This takes advantage of the regular expression * (called splat), which matches anything, while _ matches specifically an underscore, and .txt matches specifically the string .txt. By putting () around the splats, we have "captured" these wildcards and stored them in the variables $1 and $2, which we can then reference when defining our replacement string. Try it!

Oh, quick hint: the command to generate a single new file is

~~
touch filename
~~








## Exercises
1. Loops and renaming
        A. Generate 1000 files with the form <#.file.dat> using any loop you like.
        B. Rename these files to be of the form <file_#.dat> using zmv.

2. We have a file called "regex.txt". It contains the full spectrum of possible characters we may encounter in common practice. Let's use it to practice what we'e learned.
        A. Write a regular expression that will match all non-alphanumeric characters in this text
        B. Write a sed expression to change all ampersands & to the word 'and' in the file
        C. Use awk to switch the order of the columns in the file

3. Write a bash script to run the following pipeline:
        1 - generate 1000 empty text files in the form <file_#.dat>
        2 - rename all these files to the form <#.file.dat>
        3 - populate each file with the contents of regex_test.txt (hint: redirect the output of "more")
        4 - change . to @ in each file
        5 - Switch the columns in each file

Be sure to spot check a random 5-6 files to make sure it all worked!
