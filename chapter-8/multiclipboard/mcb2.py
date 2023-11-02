import pyperclip, shelve, sys

# save_keyword(keyword, content), load_text(keyword), list_keywords()
# copy, paste, list_keywords, clear
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

#TODO: Fix repitition in shelve and keywords

prefix = 'mcb'
def save_keyword_with_content(keyword, content):
    with shelve.open(prefix) as mcb_shelf:
        mcb_shelf[keyword] = content

def list_keywords():
    with shelve.open(prefix) as mcb_shelf:
        return str(list(mcb_shelf.keys()))

def load_content(keyword):
    with shelve.open(prefix) as mcb_shelf:
        return mcb_shelf[keyword]
    
def delete_keyword(keyword):
    with shelve.open(prefix) as mcb_shelf:
        if keyword in mcb_shelf.keys():
            del mcb_shelf[keyword]
        else:
            print(f'{keyword} not found. It must have been deleted.')
            sys.exit()
        
def clear_keywords():  #TODO:
    with shelve.open(prefix) as mcb_shelf:
        pass
    
    
def run():
    if len(sys.argv) == 3:
        # save clipboard content
        if sys.argv[1].lower() == 'save':
            keyword = sys.argv[2]
            content = pyperclip.paste()
            save_keyword_with_content(keyword, content)
        # delete keyword
        elif sys.argv[1].lower() == 'delete':  #TODO: CTA: Are you sure you want to
            keyword = sys.argv[2]
            while True:
                user_input = input(f'Are you sure you want to delete {keyword}: ').lower()
                if user_input == 'yes' or 'y':  # fix this issue not working
                # if user_input == 'yes' or user_input == 'y':
                    delete_keyword(keyword)
                    print(f'{keyword} deleted with contents.')
                    print(list_keywords())
                    sys.exit()
                elif user_input == 'no' or 'n':  #fix:not working
                # elif user_input == 'no' or user_input == 'n':
                    print('Deletion abolished')
                    sys.exit()
        
    # list keywords and load content
    elif len(sys.argv) == 2:
        keywords = list_keywords()
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(keywords)
            print(keywords)
        elif sys.argv[1] in keywords: 
            keyword = sys.argv[1]
            content = load_content(keyword)
            pyperclip.copy(content)
            print(content)
            
    else:
        print(f'''Usage: python your_script.py save <keyword>
                python your_script.py <keyword> 
                python your_script.py list''')      

if __name__ == '__main__':
    run()
    
# TODO: Ask the user to add that functionality and fix the bug: cta