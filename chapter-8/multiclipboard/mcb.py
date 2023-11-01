import pyperclip, shelve, sys

# save_keyword(keyword, content), load_text(keyword), list_keywords()
# Usage: py mcb.py save <keyword> - Saves clipboard to keyword.
# py mcb.py <keyword> - Loads keyword to clipboard.
# py mcb.py list - Loads all keywords to clipboard.
# py mcb.py clear - clears all keywords

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
    with shelve.open(prefix) as mcb_shelf:  #modify: remove mcb_shelf
        if keyword in mcb_shelf.keys():
            del mcb_shelf[keyword]
        else:
            print(f'{keyword} not found. It must have been deleted.')
            sys.exit()
    
def run():
    if len(sys.argv) == 3:
        # save clipboard content
        if sys.argv[1].lower() == 'save':
            keyword = sys.argv[2]
            content = pyperclip.paste()
            save_keyword_with_content(keyword, content)
        # delete keyword
        elif sys.argv[1].lower() == 'delete':  
            keyword = sys.argv[2]
            delete_keyword(keyword)
            print(f'{keyword} deleted with contents.')
            print(list_keywords())
        
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