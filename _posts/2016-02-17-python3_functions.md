---
layout: post
title: "Python III: Functions and Debugging Strategies"
instructor: Stephanie
permalink: /python3_functions/
materials: files/python3.zip
---

Functions are an integral part of programming. They are self-contained pieces of code which provide instructions for a given task. Functions are *called* with certain input, *execute* the code specified, and then *return* specified value(s) from the calculations performed. The presence of a function in a program does not guarantee that it will run - functions must be explicitly called to run. 

Functions should be an integral component of your scripts/program, allowing for modular, repeatable, and readable programs. Using functions dramatically lowers the chance of bugs occuring in your program and cleans up a lot of clutter. 

**If/when you perform a certain calculation multiple times throughout your program, or you find yourself copy/pasting code into many locations in a program, that code belongs in a function!** 


## Basic Function Syntax

Functions are defined using a `def` statement and their contents are indicated with whitespace (as with if, for, while):

{% highlight python %}
# Basic anatomy of a function which takes a single argument and returns a single value, x
def name_of_function(argument):
    # code
    # more code
    return x
{% endhighlight %}

The input argument (`argument`) exists only with the **scope** of this function, `name_of_function`. Similarly, variables created inside a function only exist inside the function. Arguments can be named arbitrarily, and they do not have to have any correspodence to variables in the main body of your code (see examples below).

For example, we can create a simple function that adds two numbers together. First, think about the actual task of addition itself: you are given two numbers, you add them together, and then you report the result.

{% highlight python %}
# Simple addition function. 
def addition(x, y):
    sum = x + y
    return sum
    
# Another way to write the same function
def addition2(x, y):
    return x + y

>>> # We can now use the function with arbitrary input arguments. 
>>> addition(85, 6)
 91

>>> a = 5
>>> b = -6
>>> addition(a, b)
 -1

>>> # The input variables remained unchanged
>>> print a, b
 5, -6

>>> # Variables defined inside the function only exist inside the function!!
>>> print x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

>>> # Assign the output of a function to a variable
>>> c = addition(a,b)
>>> print c
 -1
 
>>> # Be sure to provide all arguments, or you'll get an error message!
addition(6) # only 1 argument provided
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: addition() takes exactly 2 arguments (1 given)
{% endhighlight %}

Functions can also return multiple values, stored as a *tuple*. This means that the values returned are separated by commas and constitute an *immutable container*. This is good news - as tuples can't be changed once created, the returned values are safe!

{% highlight python %}
# Function to divide two numbers and return the result and remainder
def divide_remain(x, y):
    div = x / y
    rem = x % y
    return div, rem

>>> # Run the function!
>>> divide_remain(77, 12)
(6, 5) # the order div, rem is preserved

>>> # Save the values returned into a single variable, and then use indexing to see the values
>>> a = divide_remain(77, 12)
>>> print a
(6, 5)
>>> type(a)
<type 'tuple'>
>>> print a[0]
6
>>> print a[1]
5

>>> # Save each returned value to its own variable
>>> a, b = divide_remain(77, 12)
>>> print a
6
>>> print type(a)
<type 'int'>

>>> print b
5
>>> print type(b)
<type 'int'>
{% endhighlight %}

## Positional vs. keyword arguments

In the previous examples, all functions took a pre-specified number of arguments in a particular order. These are called *positional* arguments - the order in which you provided the arguments actually matters for how those arguments are used inside the functions. Other types of arguments allowing for more flexibility, however, are possible!

### Keyword arguments
If used in combination with positional arguments, all keyword arguments come at the *end*.
Example, 

{% highlight python %}

# Division function with two positional arguments
def divide_pos(x, y):
    return x / y 

>>> divide_pos(2,4)
2
>>> divide_pos(2,5) #womp womp! 
2

# Division with optional keyword argument, as_float. This function takes two positional arguments and one optional keyword argument.
def divide_key(x, y, as_float = True):
    if as_float:
        return float(x) / y
    else:
        return x / y 

>>> divide_key(2,5)
2.5

>>> # When specifying the non-default value, you must provide the keyword
>>> divide_key(2,5, as_float = False)
2
{% endhighlight %}

A function can have as many keyword arguments as you want. When you call the function, you can specify these arguments in any order as long as they all come *after* all positional arguments. If you intend to use the default behavior of such an argument, no need to supply it! That's why the defaults are there.

{% highlight python %}
def divide(x, y, as_float = True, digits = 3, print_sentence = False, return_remainder = False):
    if as_float:
        div = round(float(x) / float(y), digits)
    else:
        div = round( x / y, digits)
    
    if print_sentence:
        if as_float:
            print "The result of %d / %d is %f." %(x, y, div)
        else:
            print "The result of %d / %d is %d." %(x, y, div)
    
    if return_remainder:
        return div, x%y
    else:
        return div
        
>>> a = divide(6, 767, print_sentence = True, digits = 10, return_remainder = True)
The result of 6 / 767 is 0.007823.

>>> print a # think about what type a will be and why! Also, think about why there are a different number of digits in the print statement and the final dividend returned.
(0.0078226858, 6)
{% endhighlight %}


### Docstrings
It is always (read: **always**) a good idea to incorporate docstrings into your functions. Docstrings are essentially comments placed inside three quotation-mark bounds (`""" words """`) which explain the purpose, functionality, input arguments, and return values for your function. Docstrings are great because they explain to you and others looking at your code what exactly the function accomplishes, without the reader having to fully read and internalize all the code. Also, as a bonus, if you ever want to document your python code, there are awesome tools out there (like Sphinx) which will automatically create beautiful documentation from your python code using these docstrings. 
The docstrings are also shown whenever call `help()` on a given function.

Let's rewrite the most recent `divide()` function with docstrings included.

{% highlight python %}
def divide(x, y, as_float = True, digits = 3, print_sentence = False, return_remainder = False):
    """ Function to divide two numbers.
        Usage: divide(x, y, ...)
        Positional arguments:
            1. x: the numerator
            2. y: the denominator
        Optional keyword arguments:
            1. as_float: boolean argument to perform calculations and return a float value rather than integer (Default: True)
            2. digits: the number of significant digits in the final dividend (Default: 3)
            3. print_sentence: boolean argument for whether a sentence stating the results of the calculation should be printed. (Default: False)
            4. return_remainder: return the remainder between between x and y in addition to the dividend (Default: False)
    """
    if as_float:
        div = round(float(x) / float(y), digits)
    else:
        div = round( x / y, digits)

    if print_sentence:
        if as_float:
            print "The result of %d / %d is %f." %(x, y, div)
        else:
            print "The result of %d / %d is %d." %(x, y, div)

    if return_remainder:
        return div, x%y
    else:
        return div

>>> help(divide)
Help on function divide in module __main__:

divide(x, y, as_float=True, digits=3, print_sentence=False, return_remainder=False)
    Function to divide two numbers.
    Usage: divide(x, y, ...)
    Positional arguments:
        1. x: the numerator
        2. y: the denominator
    Optional keyword arguments:
        1. as_float: boolean argument to perform calculations and return a float value rather than integer (Default: True)
        2. digits: the number of significant digits in the final dividend (Default: 3)
        3. print_sentence: boolean argument for whether a sentence stating the results of the calculation should be printed. (Default: False)
        4. return_remainder: return the remainder between between x and y in addition to the dividend (Default: False)
{% endhighlight %}


### Dealing with poor function input

Generally, we write functions to accomplish a specific task, such as dividing two numbers as described above. However, there are ways for this to go wrong, for instance dividing by zero:
{% highlight python %}
divide(5, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in divide
ZeroDivisionError: integer division or modulo by zero
{% endhighlight %}

Or, perhaps the function is poorly documented and users don't know that it requires arguments to be numbers (this is a trivial example, but goes to show that the wrong **type** of input can cause lots of problems).
{% highlight python %}
divide("five", "ten")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
{% endhighlight %}

We can catch specific errors with `if` statements, for example:

{% highlight python %}
def divide(x, y):
    acceptable_types = [int, float]
    if type(x) in acceptable_types and type(y) in acceptable_types:
        return x/y
    else:
        print "Cannot compute!"
        return None
{% endhighlight %}

However, this `if` only captures one type of input problem, namely when the input arguments are not floats or integers. To catch *any* problem, we can use a construct called **`try/except`**. Syntactically, these statements looks like `if/else` statements. Their purpose is to allow Python to proceed even if errors happen:
{% highlight python %}
def divide(x, y):
    try:
        div = x/y
    except: # if an error is thrown, *within* the try statement, then we go t
        div = None
    return div
{% endhighlight %}

If the code inside the `try` block throws an error of any kind, then code within the `except` block will be executed. Note that `try` **must** have a corresponding `except` statement! If you just want to skip over any errors without putting any explicit code in `except`, use the `pass` statement, for example:
{% highlight python %}
try:
    # code that might or might not work
except:
    pass
{% endhighlight %}

## Scope in Python

The concept of *scope* is very important in computer programming. For a given object, the scope of that object refers to where in the computer program the object's name can be used to refer to its value. In other words, if I define a variable `my_variable`, will Python always know what `my_variable` is? Python is quite flexible in this regard (other languages are not!). The most important point to remember is that Python scope goes top-down: If a variable is defined at the top of a script, then throughout the rest of the script Python knows what that variable is. This is why functions are generally written at the top of a script, so that the functions can be used throughout the main body of a script.

**Importantly**, the scope of variables defined *inside a function* is the function itself - Python considers variables inside functions to exist only within the function. This means that, if you define a variable called `x` inside a function but a variable called `x` exists elsewhere in your script, Python will not get confused.


## Modules

Like other language, Python has **modules** which can be imported for specific functionality. For example, last week we used the [`random`]({{ base.url}}/Biocomputing_Spring2016/python2_controlflow/) module to generate random DNA sequences. Modules are, actually, Python scripts which contain related functions. 

This means we can write our own modules! Why would you do this? Let's say you have several scripts which all perform similar tasks, and therefore require the same functions. One way to do this is simply to include your functions in every script. An alternative (and dare-I-say, better?) strategy is to create a stand-alone python script which contains only functions - this is a module! You can then import this module into the scripts which use these functions. This strategy will help ensure that you don't accidentally introduce bugs from copy/pasting the function, and more importantly allows you to change the function *only one time* as opposed to individually in each script where it's used (no matter how diligent you are, the latter strategy **will** introduce bugs!). 


## Interpreting Error Messages

Although Python error messages might seem initially cryptic, they actually contain lots of useful information! [Follow this link](http://cdn.rawgit.com/sjspielman/ccbb_bigdata2015_python/master/cheatsheets/error_messages_informative.html) to read about interpreting error messages for debugging your code.


## Exercises

Download [this Python script](../files/python3/functions_homework.py) (also available for download with today's Cheatsheet, see home page), which contains poorly-organized Python code in need of modularization! Your task is to rearrange this script such that it contains functions, as described within the script, and is modular!