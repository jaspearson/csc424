#import statements
import tkinter
from tkinter import *
from bs4 import BeautifulSoup
import requests


#Define the scrape function
def webScrapper():

    #Assing the URL to be scaped
    url = 'http://books.toscrape.com/'

    #Set the response to the URL
    response = requests.get(url, timeout=5)

    #Define the content
    content = BeautifulSoup(response.content, "html.parser")


    # Scrape all the titles on the page and display them into the left box
    titleResult.insert(INSERT, "TITLES:\n")

    # Loop through the content on the page and print the titles in to the text area.
    for title in content.findAll("h3"):
        titleResult.insert(INSERT, title.text)
        titleResult.insert(INSERT, "\n")

    #end the print in to the text field
    titleResult.insert(END, "")

    # Scape all the prices on the page and display them in the right box
    priceResult.insert(INSERT, "PRICES:\n")

    #loop through the content on the page and print the prices into the text area.
    for price in content.findAll('p', attrs={"class": "price_color"}):
        priceResult.insert(INSERT, price.text)
        priceResult.insert(INSERT, "\n")

    # end the printint to the text field
    priceResult.insert(END, "")


# ******************************** CREATE THE GUI********************
#Create GUI top bar
class mainWindow(Frame):
    def _init_(self, master=None):
        Frame._init_(self, master)
        self.pack()

#define the root window
root = Tk()
root.geometry("750x450")
app = mainWindow(master = root)
app.master.title("Webscraper")


#Create a spacer frame
topSpace = Frame(master = root, height = "5")
topSpace.pack()

#Define the scrape button
scrapeButton = Button(master = root, text = "Scrape books.toscrape.com", width = "100", command = webScrapper)
scrapeButton.pack()

#create a spacer frame
afterButtonSpace = Frame(master = root, height = "5")
afterButtonSpace.pack()

#Create a container for the text boxes
textFrame = Frame(master = root, height = "400")
textFrame.pack()

#Create a text widget to display titles
titleResult = Text(master = textFrame, width = "43")
titleResult.pack(side = "left")

#Create a space frame between text fields
textSpace = Frame(master = textFrame, width = "8")
textSpace.pack(side = "left")

#create a text widget to display prices
priceResult = Text(master = textFrame, width = "43")
priceResult.pack(side = "left")


#enter main loop of the application
app.mainloop()
