import os, sys

def get_folder_sizes(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    
    # Check if the provided path is a directory
    if not os.path.isdir(folder):
        print(f'The path "{folder}" you have provided is not a directory')
        return  # used to exit the function

    folder_lengths = {}
    
    # Walk through the directory tree
    for folder_name, _, filenames in os.walk(folder):
        # print(folder_name)
        
        # folder_size = sum(os.path.getsize(os.path.join(folder_name, filename)) for filename in filenames)
        folder_size = sum(os.stat(os.path.join(folder_name, filename)).st_size for filename in filenames)
        # print(folder_size)  # in bytes
        
        if folder_size > 0:
            folder_lengths[folder_name] = folder_size
            
    # print(folder_lengths)
    return folder_lengths
    
# Function to find the folder with the maximum size
def get_max_folder(folder_lengths):
    max_size = 0
    max_folder = []
    
    # loop through the dictionary
    for folder_name, size in folder_lengths.items():
        if size > max_size:
            max_folder = folder_name
            max_size = size
            
    return max_folder, max_size
              
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
    
    # Call the function to get folder size s   
    folder_lengths = get_folder_sizes(folder)
    
    # Call the function to get max folder
    max_folder, max_size = get_max_folder(folder_lengths)
    
    #  Print the result
    print(f"The folder that uses the most disk space is '{max_folder}' with {max_size} bytes.")
    
if __name__ == '__main__':
    main()
    # folder = r"C:\Users\Praise Idowu\Desktop\test2" 
    # folder_lengths = get_folder_sizes(folder)
    # max_folder = get_max_folder(folder_lengths)
    # print(max_folder)
    

