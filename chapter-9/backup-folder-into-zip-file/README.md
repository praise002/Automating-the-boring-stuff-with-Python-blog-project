# Project: Backing Up a Folder into a ZIP File

Say you’re working on a project whose files you keep in a folder named
C:\AlsPythonBook. You’re worried about losing your work, so you’d like to
create ZIP file “snapshots” of the entire folder. You’d like to keep different
versions, so you want the ZIP file’s filename to increment each time it is made;
for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip,
and so on. You could do this by hand, but it is rather annoying, and you might
accidentally misnumber the ZIP files’ names. It would be much simpler to run a
program that does this boring task for you.
For this project, open a new file editor window and save it as backupToZip.py.


**How this program works**:
If you have ever used a version control such as git, you know that a version control keeps track of changes we make in our code.
First we initialize the git repo using 'git init'
Next we stage the changes using 'git add .'
Next we commit the changes using 'git commit -m ""'

What git is doing is that it is keeping a snapshot of our code and we can always revert back to previous 
state of the code.

So this project will replicate the git functonality. It is nothing as complex as git but here is how 
the program works.
TODO: UPDATE THE README GUIDE
1. When you run the program using an absolute path of a folder it creates a zip folder using the base_name(folder_name)
   and increments number by one.
2. The backup folder is saved into the main folder as a zip file.
3. Each time you run the program it increments it by one.
4. This way you have a backup of previous changes and can always revert back to it.

**Advanced**
The user specifies an output folder. This is how it works:
1. If a user doesn't specify an output folder it assumes the user wants to save it into the source folder. 
This approach is simple and doesn't require much writing of code.
2. If the user specifies an output folder, it gets the basename and saves it as `basename_backup` folder. So
   the zip file is saved into the folder. This is how it works:
   source folder: C:\Users\Praise Idowu\Documents\AlsPythonBook
   output folder: C:\Users\Praise Idowu\Documents
   Result: C:\Users\Praise Idowu\Documents\AlsPythonBook\AlsPythonBook_backup\AlsPythonBook_1.zip
   
   NB: If the folder already exists in the path it checks `AlsPythonBook_1.zip` and increments it.