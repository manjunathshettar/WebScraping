import webbrowser
from tkinter import *

form = {
    'dictionary': "https://www.dictionary.com/browse/",
    'thesaurus': "https://www.thesaurus.com/browse/"
}


def choose_source():
    question = "Would like you to visit the dictionary or the thesaurus?"
    print(question)
    while True:
        source = input('> ').lower()
        # if the search engine is a valid entry
        if source in form:
            engine_name = source.capitalize()
            # gets the base url of the entered channel
            base_url = form[source]
        else:
            print('Wrong answer! Try again.\n')
            print(question)
            # continues the operation
            continue
        # returns the news channel and the news channel's search link
        return engine_name, base_url

s, base_url = choose_source()


#creates the gui
root = Tk()
root.title('Fast Forward')

#creates a text-field for the user to enter a sarch
String_Entry = Entry(root)
String_Entry.grid(row=0, column=2)

def search():
    #gets the value from the text-field and saves it to url
    url = base_url + str(String_Entry.get())
    #forces the web browser to open the url
    webbrowser.open(url)

    text_file = open("Out.txt", "w")


#creates a button to search the value
Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=0)
#creates a button to quit out of the program
Quit_Button = Button(root, text='Exit', command=quit)
Quit_Button.grid(row=0, column=1)




#ends the tkinter()
mainloop()
