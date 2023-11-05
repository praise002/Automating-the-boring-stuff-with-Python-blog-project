import os, shutil, re, sys

# let us assume all files are in the American Style dates and we want files in the 19's and 20's

def rename_files(root_dir):
    # Create a regex pattern for American-style dates (MM-DD-YYYY)
    # date_pattern = re.compile(
    #     r'''
    #     ^(.*?) # all text before the date
    #     (0[1-9]|1[0-2])-  # matches 01-09 or 10-12 for month with a '-' character
    #     (0[1-9]|[12]\d|3[01])- # matches 01-31 for days
    #     ((19|20)\d{2})  # matches the 19's and 20's for year
    #     (.*?)$ # all text after the date
    #     ''', re.VERBOSE
    # )  # can you determine how many groups is here
    
    date_pattern = re.compile(
        r'''
        (0[1-9]|1[0-2])-  # matches 01-09 or 10-12 for month with a '-' character
        (0[1-9]|[12]\d|3[01])- # matches 01-31 for days
        ((19|20)\d{2})  # matches the 19's and 20's for year
        ''', re.VERBOSE
    ) 
   
    # Loop through all files in the current directory
    for filename in os.listdir(root_dir):
        # Check if the filename contains a date in American style
        match = date_pattern.search(filename)

        if match:  # not None
            # Extract the date components
            month, day, year, _ = match.groups()  # returns a tuple
            # Rename the file with European-style date (DD-MM-YYYY)
            new_filename = f'{filename[:match.start()]}{day}-{month}-{year}{filename[match.end():]}'
            # print(new_filename)
            
            old_filepath = os.path.join(root_dir, filename)
            new_filepath = os.path.join(root_dir, new_filename)
            
            # Rename the file using shutil.move()
            # shutil.move(old_filepath, new_filepath)
            os.rename()
            print(f'Renamed: {filename} -> {new_filename}')
            print()
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py [root_dir]')
        exit(1)
    
    try:
        root_dir = sys.argv[1]  
        rename_files(root_dir)
    except FileNotFoundError as e:
        print(e)
    