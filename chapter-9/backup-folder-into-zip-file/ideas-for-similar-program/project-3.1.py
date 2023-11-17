# sum stat_size
# for filename in os.listdir(data):
    # print(os.path.splitext(filename)[1]) # File extension
    # print(os.stat(f"{file_dir}/{filename}").st_size) # File Size
    # print(os.path.getmtime(path)) # File Creation Time
    
# greatest number of files, walk the tree and count it
# most disk space: get the statistics of all the sizes in that directory
# try using send2trash
# os.path.getsize()

import os, sys

def get_greatest_num_files(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    
    # Check if the provided path is a directory
    if not os.path.isdir(folder):
        print(f'The path "{folder}" you have provided is not a directory')
        return  # used to exit the function

    # list = []
    folder_lengths = {}
    
    # Walk through the directory tree
    for folder_name, subfolders, filenames in os.walk(folder):
        print(f'Folder name: {folder_name}')
        print(f'Subfolders: {subfolders}')
        print(len(filenames))
        # print(filenames)
        
        length = len(filenames)
        # list.append(length)
        folder_lengths[folder_name] = length
        
    print(folder_lengths)
    
    max_length = 0
    max_folder = None
    for folder_name, length in folder_lengths.items():
        if length > max_length:
            max_folder = folder_name
            max_length = length
            
    print(max_folder)
            
def main():   
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: python filename.py [absolute_path]')
        sys.exit(1)
    
    # folder = r"C:\Users\Praise Idowu\Desktop\test2\cats\catnames.txt" 
    # Get the folder path from the command-line argument
    folder = sys.argv[1]  
    
    # Check if the specified folder exists
    if not os.path.exists(folder):
        print(f"The folder '{folder}' does not exist.")
        sys.exit(1) 
    
    # Call the function to get max num files  
    get_greatest_num_files(folder)
    
if __name__ == '__main__':
    main()
    
   