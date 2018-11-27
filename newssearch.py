from tkinter import *
import webbrowser
#holding each possible value & corresponding search link
engine_dict = {'cnn': "https://www.cnn.com/search/?size=10&q=",
               'fox': "https://www.foxnews.com/search-results/search?q=",
               'bbc': "https://www.bbc.co.uk/search?q=",
               'abc': "https://abcnews.go.com/search?searchtext="}


def pick_engine():
    question = "Pick your favorite news channel between CNN, Fox, ABC, and BBC. "
    print(question)
    #while the user has entered a valid news channel
    while True:
        search_engine = input('> ').lower()
        #if the search engine is a valid entry
        if search_engine in engine_dict:
            engine_name = search_engine.capitalize()
            #gets the base url of the entered channel
            base_url = engine_dict[search_engine]
        else:
            print('Wrong answer! Try again.\n')
            print(question)
            #continues the operation
            continue
        #returns the news channel and the news channel's search link
        return engine_name, base_url


engine_name, base_url = pick_engine()
#creates the gui
root = Tk()
root.title('Search in ' + engine_name + ' made by Manjunath Shettar')

#creates a text-field for the user to enter a sarch
String_Entry = Entry(root)
String_Entry.grid(row=0, column=0)

def search():
    #gets the value from the text-field and saves it to url
    url = base_url + str(String_Entry.get())
    #forces the web browser to open the url
    webbrowser.open(url)

#creates a button to search the value
Search_Button = Button(root, text='Go', command=search)
Search_Button.grid(row=0, column=1)
#creates a button to quit out of the program
Quit_Button = Button(root, text='Exit', command=quit)
Quit_Button.grid(row=0, column=2)
#ends the tkinter()
mainloop()
