import os, sys
# loop through a dir 
# find all files with prefix
# check numbering and locates gap in the numbering
# rename all later files to close the gap

def fill_in_gaps(dir_path, file_prefix):
    for filename in os.listdir(dir_path):
        # print(filename)
        if filename.startswith(file_prefix):
            print(filename)
            
            # for alpha in filename.isnumeric():
            #     print(alpha)
        
if __name__ == '__main__':
    dir_path = 'dir1'
    file_prefix = 'spam'
    fill_in_gaps(dir_path, file_prefix)