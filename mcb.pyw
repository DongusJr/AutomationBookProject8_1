#! python3
# mcb.pyw - project from the automate the boring stuff with python
# Usage: mcb save <keyword> - Saves clipboard to keyword
#        mcb <keyword> - Loads keyword to clipboard
#        mcb list - Loads all keywords to clipboard
#        mcb getlist - Loads all keywords with newline to clipboard
#        mcb delete <keyword> - deletes a keyword from shelf

import sys, pyperclip, shelve


mcb_shelf = shelve.open("mcb")
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    
    elif sys.argv[1].lower() == "delete":
        if sys.argv[2] in list(mcb_shelf.keys()):
            del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))

    elif sys.argv[1].lower() == "getlist":
        mcb_list = list(mcb_shelf.keys())
        list_string = ""
        for item in mcb_list:
            list_string += item + "\n"
        pyperclip.copy(list_string)

    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()


