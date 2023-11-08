
# backupToZip_advanced.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
# the user specifies a source and output folder
# "C:\Users\Praise Idowu\Documents\test-automate\AlsPythonBook"
# C:\Users\Praise Idowu\Documents\project\AlsPythonBook

import zipfile, os, sys


def backup_to_zip(source_folder, output_folder):
    # get the absolute path of the source and output folder
    source_folder = os.path.abspath(source_folder)
    output_folder = os.path.abspath(output_folder)
    print(f'Source folder: {source_folder}')
    print(f'Output folder: {output_folder}')
    
    # get the basename
    base_filename = os.path.basename(source_folder)
    # print(base_filename)
    
    # We initialize the backup folder to be the ouput folder so it can be a global variable
    backup_folder = output_folder
    
    # We check if the output folder and the source folder are the same
    if source_folder != output_folder:
        # if not the same that means the user specified an output folder 
        # so it creates a backup folder using the 'basename_backup' in this case 'AlsPython_backup'
        backup_folder = os.path.join(output_folder, f'{base_filename}_backup')
        
    # if checks for the existence of the folder in the absolute path, if it doesn't exist it creates it
    # if it does exists it skips it
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
    
    # Initialize number
    number = 1
    
    # Check if the current base_filename and number exists
    while True:
        zip_filename = f'{base_filename}_{number}.zip'
        full_zip_path = os.path.join(backup_folder, zip_filename)
        print(f'Full zip path: {full_zip_path}')
        # print(f'Initial: {number}')
        number += 1
        # print(f'Final: {number}') 
        
        # Check if the zip file already exists
        if not os.path.exists(full_zip_path):
            break  # If the path does not exist a Unique filename found, exit the loop
        
   
    print(f'Creating {full_zip_path}...')
    
    # Create the zip file
    with zipfile.ZipFile(full_zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip_file:
        for folder_name, _, filenames in os.walk(source_folder):
            print(f'Adding files in {folder_name}')
            backup_zip_file.write(folder_name, os.path.relpath(folder_name, source_folder))
            
            for filename in filenames:
                # Check if a backup source_folder with the basename exists inside the current source_folder
                if not (filename.startswith(f'{base_filename}_') and filename.endswith('.zip')):
                    backup_zip_file.write(os.path.join(folder_name, filename), os.path.relpath(os.path.join(folder_name, filename), source_folder))
    
    # Print final message
    print('Done.')
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: Python backupToZip.py [folder_absolute_path e.g C:\\Users\\Praise Idowu\\Documents...]')
        sys.exit(1)
    
    source_folder = sys.argv[1]
    
    # Check if the specified folder exists
    if not os.path.exists(source_folder):
        print(f"The folder '{source_folder}' does not exist.")
        sys.exit(1)
    
    # We assume the user wants to save it to the source folder
    if len(sys.argv) == 2:
        print(f'You did not specify an output folder. Added to {source_folder}')
        backup_to_zip(source_folder, output_folder=source_folder)
        
    # the user specifies an output folder
    if len(sys.argv) == 3:
        output_folder = sys.argv[2]
        if not os.path.exists(output_folder):
            print(f"The folder '{output_folder}' does not exist.") 
            sys.exit(1)
            
        print(f'You specified an output folder. Created a backup folder in {output_folder}')
        backup_to_zip(source_folder, output_folder)
        
    