from tkinter import ttk
from tkinter import *
import pandas as pd
import csv

###########################
#           GUI CODE      #
###########################
root = Tk()
root.title("Master 2 IAM")
root.configure(bg='#4b5162')
root.geometry('800x800')

# import the csv file
filepath = 'movies.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
# remove the head "title"
del(Data[0])
# append every item parsen into movielist
movielist = []
for x in list(range(0, len(Data))):
    movielist.append(Data[x][1])
# rating list
rating = [1, 2, 3, 4, 5]
# button function to add selected movies
fake_user=[]
def addmovie(movie,rating):
    mov = [movie, rating]
    fake_user.append(mov)
    print(fake_user)

# create rappers to manage the gui
warpper1 = LabelFrame(root, text="Movies Watched")
warpper2 = LabelFrame(root, text="Movies Suggested")
warpper1.pack(padx=10, pady=10, fill="both", expand="yes")
warpper2.pack(padx=10, pady=10, fill="both", expand="yes")
# drop down box with thier label
Label(warpper1, text="Select 3 movies you watched and rate them").grid(row=0, column=0, padx=10, pady=10)
# dropdown menu 1
moviecombo = ttk.Combobox(warpper1, value=movielist).grid(row=1, column=0, padx=10, pady=10)
ratingcombo = ttk.Combobox(warpper1, value=rating).grid(row=1, column=2, padx=10, pady=10)
B1 = Button(warpper1, text="Add Your Movie",
            command=lambda: addmovie(moviecombo, ratingcombo)).grid(row=1, column=3,padx=10, pady=10)
# dropdown menu 1
moviecombo2 = ttk.Combobox(warpper1, value=movielist).grid(row=2, column=0, padx=10, pady=10)
ratingcombo2 = ttk.Combobox(warpper1, value=rating).grid(row=2, column=2, padx=10, pady=10)
B2 = Button(warpper1, text="Add Your Movie",
            command=lambda: addmovie(moviecombo, ratingcombo)).grid(row=2, column=3,padx=10, pady=10)
# dropdown menu 1
moviecombo3 = ttk.Combobox(warpper1, value=movielist).grid(row=3, column=0, padx=10, pady=10)
ratingcombo3 = ttk.Combobox(warpper1, value=rating).grid(row=3, column=2, padx=10, pady=10)
B3 = Button(warpper1, text="Add Your Movie",
            command=lambda: addmovie(moviecombo, ratingcombo)).grid(row=3, column=3,padx=10, pady=10)
# show what user have chosen
Label(warpper1, text="your selected movies").grid(row=4, column=0, padx=10, pady=10)
# list result in a list box
Label(warpper2, text="The Suggested Movies").grid(row=0, column=0, padx=10, pady=10)


root.mainloop()

