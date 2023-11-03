import os, re

def regex_search(dir_path, user_supplied_regex):
    # provide abs path
    dir = os.path.abspath(dir_path)
    # print(dir)
    for filename in os.listdir(dir):
        # print(filename)
        if os.path.isfile(os.path.join(dir, filename)):
            # print(filename)
            split_file = os.path.splitext(os.path.join(dir, filename))
            # print(split_file)
            # searches the directory for any .txt files
            if split_file[1] == '.txt':
                print(filename)
                
                # it opens the folder
                with open(os.path.join(dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                # print(content)
                
                # it searches for a line that matches user supplied regex
                user_regex = re.compile(user_supplied_regex, re.VERBOSE)
                for groups in user_regex.findall(content):
                    # it prints the result
                    print(groups)
                    

if __name__ == '__main__':
    dir_path = r'C:\Users\Praise Idowu\Documents\blog-projects\Automating-the-boring-stuff-with-Python-blog-project\chapter-8\regex_search\folder1'
    # user_supplied_regex = r'web | scraping'
    user_supplied_regex = r'''(
        (https?://)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?
        )'''
    regex_search(dir_path, user_supplied_regex)
    