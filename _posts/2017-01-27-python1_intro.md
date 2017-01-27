---
layout: post
title: "Python I: Operators and Variable types"
instructor: Katie
permalink: /python1_introduction/
materials: files/python1_cheatsheet.pdf
---

## Python: a super-awesome interpreted language
Python (like R) is an **interpreted** language, as opposed to a **compiled** one. In language like C, you must take your code and run it through a compiler before executing it. Python code executes without this extra step. It runs a little slower, but it's so much easier to debug without compiling over and over again.

## Python: an object-oriented language
Python is an object-oriented programming (OOP) language. Simply put, this means that data structures (e.g. variables) have certain properties, in particular **attributes** and **methods**. Attributes are usually descriptive features of the object, and methods are certain actions (functions) you can perform on the object itself. For example, consider a book. Books are physical objects with certain **attributes**, such as number of pages, number of words, dimensions (width, height, depth), cover art, etc. Similarly, there are several actions (**methods**) that we can do with books like reading, writing, throwing at people we hate, and sharing with people we love. A given realization of an object is called an **instance**. To continue with the book metaphor, "The Count of Monte Christo" and "Harry Potter" are each instances of book objects.

While these concepts might seem abstract, python syntax and behavior will make much more sense in light of the OOP paradigm upon which the language is based. In particular, attributes and methods are accessed in systematic ways, as follows:


{% highlight python %}
# Assume mybook is a book instance

# Call an attribute
mybook.number_of_pages
mybook.height
mybook.width

# Call a method
mybook.read()
mybook.write()
mybook.throw_at_bad_people("Voldemort") # methods might take particular arguments, in this case who we're launching books at
{% endhighlight %}

As you see, attributes and methods are called after a `. at the end of the instance name. Unlike attributes, however, methods end with parentheses. Sometimes, methods can take particular **arguments** which relate to their function, for example when we threw the book at Voldemort.

## How to run Python code
If you type "python" or possibly "python3" into a Mac or Linux terminal or Windows cmd window, you will enter the python interpreter. Here, you can type commands directly into the program, **but** it's tricky to save what you did. This is where scripts come in. You can write a script in a text editor and run it directly from the command line using a command like "python myscript.py" with any necessary arguments at the end.

There are also python IDEs (interactive development environments), similar to RStudio for R. IDEs like Spyder or PyCharm allow you to use the interpreter, write scripts, and execute the whole scripts or just certain lines of code.


## Variables
We assign values to a variable using the equals sign, `=`.

{% highlight python %}
>>> a = 5
>>> # Check that the variable was correctly assigned using the print() function
>>> print(a)
5
{% endhighlight %}

## Basic types
There are so many types of objects both in base python and in the additional packages. However, there are a few very basic types that you will work with over and over. If you are familiar with R or another language, you will recognize these types.

Variable Type   | Description | Defining | Casting
---------|--------------|---------
integer | whole number  | int() | int()      
float   | decimal number | float() | int()
string  | ordered, immutable character container | " " or ' ' | str() 
list    | ordered, mutable container | [ ] | list()
dictionary | unordered, mutable container | { } | dict()
tuple | ordered, immutable container | ( ) | tuple()

What do you think is meant by ordered/unordered, mutable/immutable, and container? What about defining and casting?

Remember, every time you create a variable, you are creating an **instance** of that particular variable type. As a consequence, there are certain properties (attributes and methods!) associated with each type of variable.

### Integers and floats
Integers and floats are python's primary types for dealing with numbers. 

Integers are whole numbers only, but floats include decimal places. Whether a variable is an integer or float turns out to matter a lot - if you perform an operation with integers, the result will be an integer (even if the "real" answer is actually a float!)

{% highlight python %}
>>> a = 6
>>> type(a)
<type 'int'>
>>> # We can change the type of a variable by using casting
>>> a = float(a)
>>> type(a)
<type 'float'>

>>> # By adding a decimal point during assignment, we force the variable to be a float
>>> b = 6.
>>> type(b)
<type 'float'>
{% endhighlight %}

## Operators

### Mathematical operators
First, we have the standard operators for addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). Additional mathematical operators include, 

1. Modulus operator `%`, which gives the remainder, e.g. `12 % 5` will result in 2.
2. Exponent operator, `**`, e.g. `5**2` will result in 25.

### Logical operators
In addition to symbols used for basic calculations, Python (like other languages!) has a series of symbols used to compare statements in a True/False context. Such statements are called **logical statements**, and the symbols we used to compare them are called **logical operators**. The most commonly used logical operators include, 

Symbol   | What it does | Example
---------|--------------|---------
  == | Equals       |  `5 == 5` results in True
  != | Not equals       |  `5 != 5` results in False
 > | Greater than       |  `5 > 6` results in False <br> `11 > 6.23` results in True
 >= | Greater than or equal to |  `5 >= 4` results in True
< | Less than  |  `4 < 5` results in True
<= | Less than or equal to |  `4 <= 5` results in True

And above all, it is **very** important to remember that the equals logical comparison requires a **double equals sign** (`==`) - a single equals signs indicates variable assignment (see below).

We can also perform multiple comparisons at once, using the keywords `and` and/or `or`. 
For example, 

{% highlight python %}
>>> # For "and," both logical statements must be true to result in True
>>> 5 == 5 and 6 == 6
True
>>> 5 > 7 and 8 < 10
False

>>> # For "or," at least one logical statement needs to be true to result in True
>>> 5 > 7 or 8 < 10
True

>>> # We can use the keyword "not" to negate a logical statement
>>> 3 < 11 and not 4 >= 7
True
{% endhighlight %}


### Strings
In python, a string is an **immutable** container of **characters**. By "immutable", we mean that it can't be changed - that is, once you create a string, you can't rewrite certain parts of it. It's an all-or-nothing thing. By characters, we basically mean "not numbers".

Strings are also **ordered**. This means we can **index** characters in a string, using brackets `[ ]`. Remember Python indices start with **ZERO**!

{% highlight python %}
>>> # Assign strings using quotation marks
>>> name = "Squidward"
>>> type(name)
<type 'str'>
>>> # Find length with function len() [note that this function works for most variable types]
>>> len(name)
9

>>> # Numbers can also be strings, if they are in quotation marks
>>> number = "100"
>>> type(number)
<type 'str'>

>>> # Even though 100 is a number, we set up the variable number as a string, so no math can be performed with this variable
>>> number - 7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'

>>> # But, since the value 100 is, in fact, a number we can recast the variable as an integer or float and then do maths with it!
>>> int(number) - 7
93
>>> # Again, number is still a string. We'd have to redefine the variable itself to make it an integer (or float) for good
>>> type(number)
<type 'str'>
>>> number = int(number)
>>> type(number)
<type 'int'>

>>> # We can't recast the variable name though, since letters just aren't numbers.
>>> name = float(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: Squidward

>>> # Strings are ordered, so we can index them
>>> name[5]
a
>>> # But strings are also immutable, so we can't edit strings in place.
>>> name[5] = "A"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
{% endhighlight python %}

<br>
Here are some useful **string methods**:

{% highlight python %}
>>> my_string = "This is a really nice string for showing examples."

>>> # .upper() converts your string to upper-case
>>> my_string.upper()
'THIS IS A REALLY NICE STRING FOR SHOWING EXAMPLES.'

>>> # .lower() converts your string to lower-case
>>> my_string.lower()
'this is a really nice string for showing examples.'

>>> # .split() takes an *argument* to split the list on and creates a list containing each chunk
>>> my_string.split('i')
['Th', 's ', 's a really n', 'ce str', 'ng for show', 'ng examples.']

>>> # .strip() removes both leading/trailing whitespace, .rstrip() removes only trailing whitespace, and .lstrip() removes only leading whitespace
>>> # Instead of whitespace, you could also provide an argument to one of these functions to remove instead
>>> dna_string = "AAAAAGTCGAGGTAGCGAAAA"
>>> dna_string.strip("A")
'GTCGAGGTAGCG'
>>> dna_string # but remember, since strings are immutable, calling .strip() will not change the dna_string contents
'AAAAAGTCGAGGTAGCGAAAA'

>>> # .count(arg) returns the number of times "arg" appears in the string
>>> dna_string.count("A")
11

>>> # .replace(old, new, count) replaces all instances of old with new. Last optional argument, count, indicates that the only the first count occurences of old should be replaced (default - all)
>>> dna_string.replace("T", "U")
'AAAAAGUCGAGGUAGCGAAAA'
>>> dna_string.replace("T", "U", 1)
'AAAAAGUCGAGGTAGCGAAAA'
{% endhighlight %}


### Lists
Lists are ordered, mutable containers. They are defined using brackets `[ ]`, and each list item can be any variable type. 

{% highlight python %}
>>> # This list contains only integers
>>> numbers = [1,2,3,4,5]

>>> # This list contains integers and floats and strings
>>> crazy_list = [5, 77.2, -9, "word", -1.32, "more words"]
{% endhighlight %}

<br>
Python lists are incredibly flexible. Like strings, they are ordered, so they support indexing. List items can be removed, changed, and new list items can even be added after they are defined. In other words, lists can be changed **in place** without needed to reassign the variable with an **=**. 

{% highlight python %}
>>> simple = [1,4,9,2,5,11]
>>> simple[4] # grab the 4th entry in this list
2
>>> simple[15] # what happens when the entry doesn't exist? You get an error message
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> # Rewrite the list in place. You don't need to redefine simple - just modify an element using indexing.
>>> simple[2] = 888
simple
[1,4,888,2,5,11]

>>> # Some useful functions you can use on a list. These will NOT modify the list in any way.
>>> len(simple) # How many elements in a list?
6
>>> sorted(simple) # sort the items in ascending order
[1, 2, 4, 5, 11, 888]
>>> max(simple) # but probably only use this when the list has only numbers. (note that min() is the opposite function.)
888
{% endhighlight %}

<br>
Here are some useful **list methods**:

{% highlight python %}
>>> # .append(value) adds value to the end of a list, ultimately modifying the list in place
>>> simple.append(100.33)
simple
[1,4,888,2,5,11,100.33]
>>> len(simple) # The list length changed
7

>>> # .index(value) returns the index for a given value
>>> simple.index(888)
2
{% endhighlight %}

## Indexing/Slicing
In general, indexing follows the paradigm `container[x:y:z]`, where x is the starting index, y is the ending index, and z is the step. However, you do not need to provide all of these value to index.

**Most importantly**, the starting index is *inclusive* but the ending index is *exclusive*. See below for examples.

{% highlight python %}
>>> fib_list = [0,1,1,2,3,5,8,13,21,34,55,89]

>>> # Select the 3rd item
fib_list[3]
1

>>> # Select the 3rd from last item with a negative index
fib_list[-3]
34

>>> # Select multiple items with the syntax [x:y], where x is the starting index and y is the ending index. Note that y is *not* included
>>> # Select items indexed 1-4
>>> fib_list[1:5]
[1, 1, 2, 3]


>>> # If you don't provide x or y, python defaults to either the first or last index
>>> fib_list[:5] # same as writing fib_list[0:5]
[0, 1, 1, 2, 3]
>>> fib_list[5:] # same as writing fib_list[5:12]
[5, 8, 13, 21, 34, 55, 89]

>>> # Change the step of indexing with the format x:y:z (before, z was defaulted to 1!)
>>> fib_list[2:10:3]
[1, 5, 21]
{% endhighlight %}

### Dictionaries
Dictionaries are defined using braces `{ }`, and they are essentially **unordered** lists of key:value pairs, and they are python's version of "associative arrays." Keys and values can be any type, although typically keys are either integers, floats, or strings. Dictionaries are incredibly useful for storing information; all keys must be unique, but values may be repeated.

{% highlight python %}
>>> taxonomy = {'gecko':'vertebrate', 'human':'vertebrate', 'squid':'mollusk', 'butterfly':'insect', 'oak tree': 'plant'}
{% endhighlight %}

Because dictionaries are unordered, we cannot index them using the standard brackets. Instead, we index dictionaries using **keys**. The key:value pairs are fixed, but there is no specific order to the key:value pairs within the dictionary. 

{% highlight python %}>>> taxonomy["gecko"]
'vertebrate'
>>> # Add a new key:value pair
>>> taxonomy["e. coli"] = "bacteria"
>>> taxonomy
t

>>> # the method .keys() pulls up all dictionary keys as a list
taxonomy.keys()
['butterfly', 'oak tree', 'squid', 'e. coli', 'human', 'gecko']

>>> # the method .values() pulls up all dictionary values as a list
taxonomy.values()
['insect', 'plant', 'mollusk', 'bacteria', 'vertebrate', 'vertebrate']

>>> # the methods .items() pulls up all key:value pairs as tuples
>>> taxonomy.items()
[('butterfly', 'insect'), ('oak tree', 'plant'), ('squid', 'mollusk'), ('e. coli', 'bacteria'), ('human', 'vertebrate'), ('gecko', 'vertebrate')]

>>> # Values can be all kinds of things, even lists
>>> meals = {"breakfast": ["coffee", "cereal", "banana"], "lunch": ["salad", "lemonade", "chicken fingers"], "dinner": ["steak", "asparagus", "beer", "more beer"], "dessert": ["ice cream", "chocolate sauce", "sprinkles"] }
{% endhighlight %}

### Tuples

Tuples are essentially immutable (i.e. unchangable) lists, created with parentheses `( )`. This variable type will become very important when we learn about functions in a few weeks.
{% highlight python %}
>>> my_tuple = (4, 5, 6)
>>> # Note that python will not let you change a tuple once it has been defined:
>>> my_tuple[1] = 88 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
{% endhighlight %}


## Other useful functions

The `len()` function returns the length of a container (list, dictionary, string, tuple)
{% highlight python %}
>>> a = [1, 2, 6, 8, 1]
>>> len(a) # Returns the number of entries in 'a'
5
>>> b = "This is a string!"
>>> len(b) # Returns the number of characters in 'b'
17
{% endhighlight %}

<br>
The `range()` function creates an generator (another type of object), by default starting from zero and with a step of 1
{% highlight python %}
>>> simple_range = range(20)
>>> list(simple_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> complex_range = range(5, 20) # start from 5
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> complexer_range = range(5, 20, 3) # start from 5 with a step of 3. look familiar??
[5, 8, 11, 14, 17]
{% endhighlight %}

<br>
The `type()` function tells you the type (e.g. list, int) of a certain variable. This function can be very useful for error checking.
{% highlight python %}
>>> my_list = [4,5,6,7,8]
>>> type(my_list)
<type 'list'>
>>> my_int = 99
>>> type(my_int)
<type 'int'>
{% endhighlight %}


<br>
The `dir()` function tells you what types of methods or actions you can perform on a given variable (ignore the `__action__` formatted output - this is not relevant for now!).
{% highlight python %}
>>> my_list = [4,5,6,7,8]
>>> dir(my_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> my_int = 4
>>> dir(my_int)
{% endhighlight %}


## The print function
Printing information from a script to "stdout" is a critically important compontent of scripting and programming. *Only by printing* can you determine if your code is actually doing what you think it is. Most of the time, your code will have some issues and will need to be "debugged." Printing to screen is one of the best and easiest strategies for ensuring that your code is working as intended.

{% highlight python %}
>>> # Define a variable and print
>>> a = 6
>>> print(a)
6
{% endhighlight %}

You can more or less print anything to screen, and importantly you can print multiple things in the same statement!

{% highlight python %}
>>> # Define a variable and print
>>> mystring = "I am writing a full sentence here as a string variable."
>>> print(mystring)
I am writing a full sentence here as a string variable.

>>> # print two strings together with + 
>>> print("Here is my string: " + mystring)

>>> To concatenate values/variables when printing, they must be of the same type
>>> print(mystring  + 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> print(mystring  + "2")
I am writing a full sentence here as a string variable.2
{% endhighlight %}


## Exercises 

Remember that **printing** is the only way to confirm if your code is behaving as expected. Print print print! We recommend that you perform these exercises in Python scripts (not in an active interpreter session). 

+ Write a script to count the number of each nucleotide (A, C, G, T) in a nucleotide sequence. You should define a variable containing a sequence (**hint**: this variable should be a string!), and you should use the method `.count()` to count each nucleotide. Your script should print out the calculated nucleotide counts, for example:
{% highlight python %}
    Number of A: 10
    Number of C: 5
    Number of G: 9
    Number of T: 8
{% endhighlight %}   

+ Modify your code from the previous exercise to compute the **percentages** (rather than counts) of each nucleotide in given sequence. As before, print out the calculated percentages.

+ Define a variable called `mystring`, which contains a lengthy string of some kind (random letters, your address, song lyrics, a haiku, whatever). Perform the following tasks with this variable:
    + Use the `len()` function to determine how many characters are in your string.
    + Without changing your variable itself, replace the all occurrences of a letter of your choice with the number 6. Use the string method `.replace()` for this task.
    + Redefine mystring such that only the first 3 occurrences of this letter are replaced, again using the string method `.replace()`. (**Hint**: not sure how to do this? Enter `help(replace)` in a Python interpretter session, or google how to use the `replace` method!).
    + Try to use indexing to replace the character in the 5th position of mystring with the letter "X". Did this work? Can you figure out why or why not?
    + Use the `.upper()` method to re-define your string variable to be entirely uppercase. Make sure your variable has been redefined by printing it out!
    + Use the `.split()` method to split your string into a list. Do this two times, the first time using a character that **is** in your string and the second time using a character that *is not* present in your string. Think about why the resulting output looks the way it does.


+ Create a variable called `mylist`, which is a list of numbers (integers or floats, whatever you choose!). Perform the following tasks with this variable:
    + Use the `len()` function to determine how many entries are in your list.
    + Use the `.append()` method to add another number to the end of your list. For example, if you started with `[1, 2, 6, 7]`, you might now have `[1, 2, 6, 7, 3.3]`.
    + Re-assign the 2nd entry (**hint**: which index is this?) of your list to the opposite sign of that entry (i.e. 4 would now be -4, -9 would now be 9).
    + Re-assign the 1st entry of your list to be a **new list**. For example, if you started with `[1, 2, 6, 7]`, you might now have `[ [1,2,3], 2, 6, 7]`. Use the `len()` function to determine how long the list is now. Is it what you expected? Think about why or why not.
    + Use the `len()` function to determine the length of this first entry within your list (**hint**: lots of indexing!).
    

+ Create a variable called `mydict`, which contains this dictionary (you can copy/paste!): `{"dna": "nucleotides", "rna": "nucleotides", "protein": "amino acids"}`.  Perform the following tasks with this variable:
    + Use dictionary indexing to print out the **value** associated with the key **"dna"**.
    + Add this new key:value pair to the dictionary: "molecule" is the key, and "atoms" is the value. 
    + Add this other new key:value pair to the dictionary: "dna":"ACGT". Print out the dictionary. What do you notice? What does the output tell you about dictionary keys and values?
    + Create a new list variable which contains the **keys** in your dictionary. For this exercise, do not type out the keys - use the `.keys()` method.
    + Determine the length of the value associated with the dictionary key "dna". Do this procedure for each key in the dictionary, and calculate the average value length. Print this value to screen.

























