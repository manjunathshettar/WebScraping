import urllib3.request
import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser


#holding each possible value & corresponding search link
engine_dict = {'tenday': "https://weather.com/weather/tenday/l/",
               'hourly': "https://weather.com/weather/hourbyhour/l/",
               'fiveday': "https://weather.com/weather/5day/l/",
               'weekend': "https://weather.com/weather/weekend/l/"}


def pick_engine():
    question = "What type of forecast would you like? Type hourly for hourly, fiveday for five day, weekend for weekend and tenday for ten day"
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
root.title('Get ' + engine_name + ' forecast, made by Manjunath Shettar')

#creates a text-field for the user to enter a sarch
String_Entry = Entry(root)
String_Entry.grid(row=0, column=2)



url =""
def search():
    #gets the value from the text-field and saves it to url
    url = base_url + str(String_Entry.get())
    #forces the web browser to open the url
    webbrowser.open(url)



#creates a button to search the value
Search_Button = Button(root, text='Zip', command=search)
Search_Button.grid(row=0, column=0)
#creates a button to quit out of the program
Quit_Button = Button(root, text='Exit', command=quit)
Quit_Button.grid(row=0, column=1)




#ends the tkinter()
mainloop()
