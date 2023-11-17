import os, shutil, sys

def select_files(src, extensions):
    """
    Select files with specified extensions from the source directory.

    Parameters:
    - src (str): Source directory path.
    - extensions (list): List of file extensions to select.

    Returns:
    - list: List of selected file paths.
    """
    src = os.path.abspath(src)
    selected_files = []
    # walk the dir tree
    for folder_name, _, filenames in os.walk(src):
        for filename in filenames:
            if any(filename.endswith(extension) for extension in extensions):
                selected_files.append(os.path.join(folder_name, filename))
                    
    return selected_files

def copy_files(selected_files, dest):
    """
    Copy selected files to the destination directory.

    Parameters:
    - selected_files (list): List of file paths to copy.
    - dest (str): Destination directory path.
    """
    # check if the dest exists
    if not os.path.exists(dest):
        os.mkdir(dest)
    
    for file_path in selected_files:
        # print(file_path)
        shutil.copy(file_path, dest)
        print(f'Copied: "{file_path}" to "{dest}"')
        
        
def select_copy(src, dest, extensions):
    """
    Select files with specified extensions from the source directory
    and copy them to the destination directory.

    Parameters:
    - src (str): Source directory path.
    - dest (str): Destination directory path.
    - extensions (list): List of file extensions to select.
    """
    src = os.path.abspath(src)
    dest = os.path.abspath(dest)
    
    # Check if the specified folder exists
    if not os.path.isdir(src):
        print(f'The path "{src}" you have provided is not a directory')
        return  # used to exit the function
    
    selected_files = select_files(src, extensions)
    copy_files(selected_files, dest)            

if __name__ == '__main__':
    # src = r"C:\Users\Praise Idowu\Desktop\test2"
    # dest = r"C:\Users\Praise Idowu\Desktop\test4"
    
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print('Usage: python filename.py [src] [dest]')
        sys.exit(1)
    
    # Get the folder path from the command-line argument
    src = sys.argv[1]
    dest = sys.argv[2]  
    extensions = ['.pdf', '.jpg', '.png']
    select_copy(src, dest, extensions)