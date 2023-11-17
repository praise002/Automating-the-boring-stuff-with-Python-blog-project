
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
# output folder is same as source folder
# Usage: py .\backupToZip.py "C:\Users\Praise Idowu\Desktop\python-book"

import zipfile, os, sys

def backup_to_zip(folder):
    # get the absolute path of the folder
    folder = os.path.abspath(folder)
    # get the basename
    base_filename = os.path.basename(folder)
    print(base_filename)  # output: python-book
    
    # Initialize number
    number = 1
    
    # Check if the current base_filename and number exists
    while True:
        zip_filename = f'{base_filename}_{number}.zip'  # python-book_1.zip
        full_zip_path = os.path.join(folder, zip_filename)
        print(f'Initial: {number}')
        number += 1
        print(f'Final: {number}') 
        
        # Check if the zip file already exists
        if not os.path.exists(full_zip_path):
            break  # If the path does not exist a Unique filename found, exit the loop
        
   
    print(f'Creating {full_zip_path}...')
    
    # Create the zip file
    with zipfile.ZipFile(full_zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip_file:
        # Walk the entire folder tree and compress the files in each folder
        # for folder_name, subfolders, filenames in os.walk(folder):
        for folder_name, _, filenames in os.walk(folder):
            print(f'Adding files in {folder_name}')
            # Add the current folder to the ZIP file
            backup_zip_file.write(folder_name)

            # Add all the files in this folder to the ZIP file
            for filename in filenames:
                # skip previously made backup ZIPs
                if not (filename.startswith(f'{base_filename}_') and filename.endswith('.zip')):
                    backup_zip_file.write(os.path.join(folder_name, filename))
    
    # Print final message
    print('Done.')
    
def main():   
    if len(sys.argv) != 2:
        print('Usage: Python backupToZip.py [absolute_path]')
        sys.exit(1)
        
    folder = sys.argv[1]
    
    # Check if the specified folder exists
    if not os.path.exists(folder):
        print(f"The folder '{folder}' does not exist.")  
        sys.exit(1)
    
    backup_to_zip(folder)
    
if __name__ == '__main__':
    main()
    