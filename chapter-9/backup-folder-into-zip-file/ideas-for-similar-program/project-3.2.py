import os, sys

def get_greatest_num_files(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    
    # Check if the provided path is a directory
    if not os.path.isdir(folder):
        print(f'The path "{folder}" you have provided is not a directory')
        return  # used to exit the function

    folder_lengths = {}
    
    # Walk through the directory tree
    for folder_name, _, filenames in os.walk(folder):
        length = len(filenames)
        folder_lengths[folder_name] = length
    
    max_length = 0
    # max_folder = None
    max_folders = []
    
    for folder_name, length in folder_lengths.items():
        if length > max_length:
            # max_folder = folder_name
            # max_length = length
            max_folders = [folder_name]
            max_length = length
        elif length == max_length:
            max_folders.append(folder_name)
    
    if len(max_folders) == 1:
        print(f"The folder with the maximum length is '{max_folders[0]}' with {max_length} files.")
    else:
        print(f"The folders with the maximum length ({max_length} files) are: {', '.join(max_folders)}")
              
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
    
    
# TODO: Split into functions, use debugging, write comments