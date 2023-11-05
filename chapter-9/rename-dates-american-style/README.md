# Project: Renaming Files with American-Style Dates to European-Style Dates

Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates
(DD-MM-YYYY). This boring task could take all day to do by hand! Let’s write
a program to do it instead.

Here’s what the program does:
- It searches all the filenames in the current working directory for American style dates.
- When one is found, it renames the file with the month and day swapped to
make it European-style.

This means the code will need to do the following:
- Create a regex that can identify the text pattern of American-style dates.
- Call os.listdir() to find all the files in the working directory.
- Loop over each filename, using the regex to check whether it has a date.
- If it has a date, rename the file with shutil.move().

## Ideas for Similar Programs
There are many other reasons why you might want to rename a large number of
files.
- To add a prefix to the start of the filename, such as adding spam_ to rename
eggs.txt to spam_eggs.txt
- To change filenames with European-style dates to American-style dates
- To remove the zeros from files such as spam0042.tx