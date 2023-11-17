import os, sys

# Function to list all files
def list_files(root_dir):
    filenames = []
    # Loop through the directory
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            filenames.append(filename)
        
    return filenames

# Rename files and print a message
def rename_files(old_filename, new_filename):
    os.rename(old_filename, new_filename)
    print(f'{old_filename} has been renamed to {new_filename}')

# Function to rename files with an infinite number of prefix           
def rename_files_with_prefix(root_dir, prefix):
    filenames = list_files(root_dir)
    for filename in filenames:
        old_filename = os.path.join(root_dir, filename)
        new_filename = os.path.join(root_dir, f'{prefix}_{filename}')
        rename_files(old_filename, new_filename)
       
# Function to remove prefix from files    
def remove_prefix_from_files(root_dir):
    filenames = list_files(root_dir)
    for filename in filenames:
        if '_' not in filename:
            print(f'{filename} cannot be renamed because it doesn\'t have a prefix.')
        else:
            splitted_filename = filename.split('_')
            
            if len(splitted_filename) > 1:
                # Remove the last prefix
                old_filename = os.path.join(root_dir, filename)
                new_name = '_'.join(splitted_filename[1:])
                new_filename = os.path.join(root_dir, new_name)
                rename_files(old_filename, new_filename)
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: Python main.py [root_dir] [Optional(for renaming) prefix]')
        sys.exit(1)
    
    root_dir = sys.argv[1]
    
    if len(sys.argv) == 3:
        prefix = sys.argv[2]
        rename_files_with_prefix(root_dir, prefix)
    else:   
         remove_prefix_from_files(root_dir)
    