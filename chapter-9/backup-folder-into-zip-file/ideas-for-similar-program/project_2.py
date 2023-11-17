import os, sys, zipfile

def archive_files(folder):
    # Get the absolute path of the folder
    folder = os.path.abspath(folder)
    
    # Extract the base name of the folder
    base_name = os.path.basename(folder)
    
    # Check if the provided path is a directory
    if not os.path.isdir(folder):
        print(f'The path "{folder}" you have provided is not a directory')
        return  # used to exit the function
    
    # Initialize number for creating unique zip file names
    number = 1
    
    # Check if the current base_filename and number exists
    while True:
    
        zip_filename = f'{base_name}_backup_{number}.zip'
        full_zip_path = os.path.join(folder, zip_filename)
        
        number += 1
        
        # Check if the zip file already exists
        if not os.path.exists(full_zip_path):
            break  # If the path does not exist, a Unique filename found, exit the loop
        
   
    print(f'Creating {full_zip_path}...')
    
    
    # Create a new ZIP file
    with zipfile.ZipFile(full_zip_path, 'w', zipfile.ZIP_DEFLATED) as archive_zip_file:
        # Walk through the directory tree
        for folder_name, _, filenames in os.walk(folder):
            
            for filename in filenames:
                # Exclude certain file types and the current zip file
                if not (filename.endswith('.txt') or filename.endswith('.py')\
                    or filename.startswith(f'{base_name}_') and filename.endswith('.zip')):
                    print(f'{filename}')
                    file_path = os.path.join(folder_name, filename)
                    archive_path = os.path.relpath(file_path, folder_name)
                    archive_zip_file.write(file_path, archive_path)
    
    # Print final message
    print('Done.')           

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
    
    # Call the function to archive the files  
    archive_files(folder)
    
if __name__ == '__main__':
    main()
    
   