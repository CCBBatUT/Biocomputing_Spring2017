---
layout: post
title: "Version control with git and github"
instructor: Devon
permalink: /version_control_git/
materials: 
---


Have you ever created multiple copies of a folder in order to try
different things with your code without losing previous parts that have worked?
Well, there's an easier way, with version control!

Version control allows you to keep a hidden record of changes you make to files.
These are stored in a special hidden directory, .git

Using git on your local machine is a great way to keep track of changes you make
as you develop your code over the course of a project. However, it also
interfaces with the online site Github, which allows you to share code with
collaborators and the public in order to get more eyes on you code, or to
provide it for others to use. This is the heart of open-source research, because
we all want to share our hard work with our colleagues to save them time and
help science progress faster!

Note that git and Github are not the same thing. Git is a command language that
comes with every operating system, while Github is a website created to help
share your work once saved with git. It's possible to use git without Github,
but not possible to use Github without git.

## Basics of git

From now on, when you start a new project involving code, create a new directory
using git. Where  you used to type

~~~
mkdir new_project
~~~

now try

~~~
git init new_project
~~~

This initializes a new folder with version control from the get-go, and is good
practice to get in the habit of.

You can check the status of your version control using the command

~~~
git status
~~~

Let's try initializing a new repo and checking it's status. If you've done it
correctly up to this point, you should see printed to the screen

~~~
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
~~~

Now, we can create files! After creating files, we need to add them to the staging
area in order to begin tracking changes we make.

~~~
git add new_file.py
~~~

Now, all changes we make to new_file.py will be tracked and recorded by git.
However, we don't store these changes until we commit them. They are being tracked,
to in order to save them as a version of our work, we must commit them.
We commit with a message that tells us what changes we have made, and what they are
meant to accomplish. In the case of the first commit to this repo, we can just
tell git that it's our initial commit

~~~
git commit -m "initial commit"
~~~

Other comments might include "fixes bug in code at line 198", "adds a new functions
to do x", etc.

Those are the basics!

## Introduction to Github

Now that we've saved our work in a local repository with git, we may wish to
share our work with collaborators. This is where we use Github.

To begin, we need to create an empty .git repository on Github. This is pretty
easy to do, but let's walk through an example together. Let's create a repo
called "new_project"

Ok, now that we've initialized the github repo, we can copy its URL and add it to
the configuration of our local repo.

~~~
git remote add origin URL
git remote -v
~~~

Now, we just need to push all our changes to the online repository on Github!

~~~
git push -u origin master
~~~

Now, you're all set! But there are a few more things to keep in mind when using
Github. A couple best practices to get into the habit of, because they will make
your life easier.

1) you should always begin working for the day in your version controlled repo
by first pulling all changes from Github to your local machine. This ensures
that there aren't any conflicts.

~~~
git pull
~~~

2) Now, any new changes you make in your local repository will be completely new.
In order to send them to Github, go back through the steps of

~~~
git add files
git commit -m "commit message"
~~~

But now, to push it all to Github, we need one final command after committing:

~~~
git push
~~~

Be sure to check your status again with

~~~
git status
~~~

to make sure everything is up to date, and that all the files you want to be
tracked are being correctly tracked.

##Ignoring parts of your repo

It takes memory to keep files under version control, because a hidden repository
is created that contains copies of those files each time you commit a change.
We don't always want to version control everything in our repo, so we can ignore
certain things (such as test directories, data files, etc) using a .gitignore
file.

~~~
touch .gitignore
~~~

Keeping this in the same git repo will force git to ignore the files listed
within this file. I usually use .gitignore for large directories of data.

## Troubleshooting

Many problems can arise with git, and drive you a little crazy. For help, you
can always check out [this website](https://www.atlassian.com/git/tutorials/undoing-changes#git-checkout)
for help and more tutorials.

And, as usual, any particular problems you may have can always be Googled!
Google is your best friend, as is StackOverflow. 
