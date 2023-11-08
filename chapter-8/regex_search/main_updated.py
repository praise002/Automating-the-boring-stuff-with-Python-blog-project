import os, re

def regex_search(dir_path, user_supplied_regex):
    # Provide an absolute path
    dir = os.path.abspath(dir_path)
    
    # Create a regex pattern from the user-supplied regex
    user_regex = re.compile(user_supplied_regex, re.VERBOSE)
    
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        
        # Check if the file is a .txt file
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            print(filename)
                
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Search for matches in the content
            matches = user_regex.findall(content)
            
            # Print the matched line
            for match in matches:
                # Extract and print all groups in the match
                # print(type(match))
                if isinstance(match, tuple):
                    print(match[0])
                elif isinstance(match, list):
                    pass
                else:
                    print(match)
                    

if __name__ == '__main__':
    dir_path = r'C:\Users\Praise Idowu\Documents\blog-projects\Automating-the-boring-stuff-with-Python-blog-project\chapter-8\regex_search\folder1'
    # user_supplied_regex = r'web | scraping'
    user_supplied_regex = r'''(
        (https?://)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?
        )'''
    regex_search(dir_path, user_supplied_regex)