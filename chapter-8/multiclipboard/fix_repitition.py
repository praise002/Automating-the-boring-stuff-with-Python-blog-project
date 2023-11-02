import pyperclip, shelve, sys

# save_keyword(keyword, content), load_text(keyword), list_keywords()
# Usage: py mcb.py save <keyword> - Saves clipboard to keyword.
# py mcb.py <keyword> - Loads keyword to clipboard.
# py mcb.py list - Loads all keywords to clipboard.
# py mcb.py clear - clears all keywords

prefix = 'mcb'

def save_keyword_with_content(keyword, content, mcb_shelf):
    mcb_shelf[keyword] = content  # fix: it overrides an existing keyword

def list_keywords(mcb_shelf):
    return str(list(mcb_shelf.keys()))

def load_content(keyword, mcb_shelf):
    return mcb_shelf[keyword]
    
def delete_keyword(keyword, mcb_shelf):
    if keyword in mcb_shelf.keys():
        del mcb_shelf[keyword]
    else:
        print(f'{keyword} not found. It must have been deleted.')
        sys.exit()
        
def clear_keywords(mcb_shelf):
    keys = mcb_shelf.keys()
    if len(keys) > 0:
        for key in list(keys):
            del mcb_shelf[key]
    else:
        print('List is empty')
        sys.exit()
    
def run():
    with shelve.open(prefix) as mcb_shelf:  #there is repitition of some variables
        if len(sys.argv) == 3:
            # save clipboard content
            if sys.argv[1].lower() == 'save':
                keyword = sys.argv[2]
                content = pyperclip.paste()
                save_keyword_with_content(keyword, content, mcb_shelf)
            # delete keyword
            elif sys.argv[1].lower() == 'delete':  
                keyword = sys.argv[2]
                delete_keyword(keyword, mcb_shelf)
                print(f'{keyword} deleted with contents.')
                print(list_keywords(mcb_shelf))
            
        elif len(sys.argv) == 2:
            keywords = list_keywords(mcb_shelf)
            # list keywords
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(keywords)
                print(keywords)
            # load contents
            elif sys.argv[1].lower() in keywords: 
                keyword = sys.argv[1]
                content = load_content(keyword, mcb_shelf)
                pyperclip.copy(content)
                print(content)
            # clear all keywords
            elif sys.argv[1].lower() == 'clear':
                clear_keywords(mcb_shelf)
                print('Keywords cleared')
                print(keywords)
                
        else:
            print(f'''Usage: python your_script.py save <keyword>
                    python your_script.py <keyword> 
                    python your_script.py list''')      

if __name__ == '__main__':
    run()