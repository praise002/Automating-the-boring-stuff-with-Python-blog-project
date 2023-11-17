import os, sys

# Function to get the lengths of files in each folder
def get_folder_lengths(folder):
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
        
    return folder_lengths

# Function to find the folder(s) with the maximum length
def find_max_folder(folder_lengths):
    max_length = 0
    max_folders = []
    
    # loop through the dictionary
    for folder_name, length in folder_lengths.items():
        if length > max_length:
            max_folders = [folder_name]
            max_length = length
        elif length == max_length:
            max_folders.append(folder_name)
            
    return max_folders, max_length
              
def main():   
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: python filename.py [absolute_path]')
        sys.exit(1)
    
    # Get the folder path from the command-line argument
    folder = sys.argv[1]  
    
    # Check if the specified folder exists
    if not os.path.exists(folder):
        print(f"The folder '{folder}' does not exist.")
        sys.exit(1) 
    
    # Call the function to get folder lengths    
    folder_lengths = get_folder_lengths(folder)
    
    # Call the function to get max folder
    max_folders, max_length = find_max_folder(folder_lengths)
    
    #  Print the result
    if len(max_folders) == 1:
        print(f"The folder with the maximum length is '{max_folders[0]}' with {max_length} files.")
    else:
        print(f"The folders with the maximum length ({max_length} files) are: {', '.join(max_folders)}")
    
if __name__ == '__main__':
    main()
    
    
# TODO: use debugging