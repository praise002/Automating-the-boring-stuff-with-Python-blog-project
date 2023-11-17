import os, shutil, sys

# walk through a dir tree
# create a list of file extensions to copy
# copy it to a new folder

def select_copy(src, dest):
    src = os.path.abspath(src)
    dest = os.path.abspath(dest)
    # base_name
    extensions = ['.pdf', '.jpg', '.png']
    
    # Check if the provided path is a directory
    if not os.path.isdir(src):
        print(f'The path "{src}" you have provided is not a directory')
        return  # used to exit the function
    
    # walk the dir tree
    for folder_name, subfolders, filenames in os.walk(src):
        for filename in filenames:
            # print(filename)
            # if any(filename.endswith(extension) for extension in extensions):
            for extension in extensions:
                if filename.endswith(extension):
                    print(filename)
                    
                    # check if the dest exists
                    if not os.path.exists(dest):
                        os.mkdir(dest)
                        
                    # copy it to a new folder
                    shutil.copy(os.path.join(folder_name, filename), dest)
                    

if __name__ == '__main__':
    src = r"C:\Users\Praise Idowu\Desktop\test2"
    dest = r"C:\Users\Praise Idowu\Desktop\test4"
    select_copy(src, dest)