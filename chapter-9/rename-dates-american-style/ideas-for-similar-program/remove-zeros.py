import os, sys

# name = '004504Spam00'
# name = 'spam0042'.split('0')
# print(name)
# print('_'.join([name[0], name[-1]]))
# print(name.lstrip('0'))
# print(name.strip('0'))

# It assumes that the zeros is in the middle of the filename beacause according to the program
# we just want to remove the zeros

def remove_zeros(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            splitted_filename = filename.split('0')
            # print(splitted_filename)
            new_filename = ''.join(splitted_filename)
            # print(new_filename)
            new_filepath = os.path.join(directory, new_filename)
            os.rename(file_path, new_filepath)
            print(f'{file_path} was renamed to {new_filepath}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: Python main3.py [path/to/directory]')
        sys.exit(1)

    directory = sys.argv[1]
    remove_zeros(directory)
        
    

