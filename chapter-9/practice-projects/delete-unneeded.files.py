import os
# send2trash
# walk through the dir
# select files or folders that are more than 100MB
# print these files with their abs path
# "C:\Users\Praise Idowu\Downloads"
# "C:\Users\Praise Idowu\Documents\programmingbooks"

def delete_large_files(folder_path, size_limit):
    folder_path = os.path.abspath(folder_path)
    # Walk through the folder tree
    for folder_name, _, filenames in os.walk(folder_path):
        
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            # Get the size of the file in bytes
            file_size = os.path.getsize(file_path)
            
            # Check if the file size exceeds the specified limit
            if file_size > size_limit:
                print(f'File: {file_path} | Size: {file_size} bytes')
       
        
if __name__ == '__main__':
    folder_path = r"C:\Users\Praise Idowu\Documents\programmingbooks"
    size_limit = 18151908  # in bytes 
    # Call the function to find and print large files
    delete_large_files(folder_path, size_limit)