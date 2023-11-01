# Multiclipboard

Say you have the boring task of filling out many forms in a web page or software
with several text fields. The clipboard saves you from typing the same text over
and over again. But only one thing can be on the clipboard at a time. If you have
several different pieces of text that you need to copy and paste, you have to keep
highlighting and copying the same few things over and over again.
You can write a Python program to keep track of multiple pieces of text. This
“multiclipboard” will be named mcb.pyw (since “mcb” is shorter to type than
“multiclipboard”). The **.pyw extension means** that Python won’t show a
Terminal window when it runs this program. (See Appendix B for more details.)
The program will save each piece of clipboard text under a keyword. For
example, when you run py mcb.pyw save spam, the current contents of the
clipboard will be saved with the keyword spam. This text can later be loaded to
the clipboard again by running py mcb.pyw spam. And if the user forgets what
keywords they have, they can run py mcb.pyw list to copy a list of all
keywords to the clipboard.

Here’s what the program does:
- The command line argument for the keyword is checked.
- If the argument is save, then the clipboard contents are saved to the keyword.
- If the argument is list, then all the keywords are copied to the clipboard.
- Otherwise, the text for the keyword is copied to the keyboard.
  
This means the code will need to do the following:
- Read the command line arguments from sys.argv.
- Read and write to the clipboard.
- Save and load to a shelf file.
If you use Windows, you can easily run this script from the Run... window by
creating a batch file named **mcb.bat** with the following content:

`@pyw.exe C:\Python34\mcb.pyw %*`


# Extending the Multiclipboard

Extend the multiclipboard program in this chapter so that it has a delete
`<keyword>` command line argument that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords