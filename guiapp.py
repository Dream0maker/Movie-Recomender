from tkinter import ttk
from tkinter import *
import pandas as pd
import csv

# ############################
# #          backend         #
# ############################
# # movie lens data set import
# ratings = pd.read_csv('ratings.csv')
# movies = pd.read_csv('movies.csv')
#
# # merging the two files to get the movies and ratings in one file + dropping unwanted columns
# ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)
#
# # changing the data structure to ease the work
# user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
# # print(user_ratings.head())
#
# # remove movies who were rated by lesser than 10 user and fill Nan with 0
# user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)
# # print(user_ratings)
# # applying the pearson methode to get the similarities between the movies
# item_similarity_df = user_ratings.corr(method='pearson')
# # print(item_similarity_df.head(50))
#
# def get_similar(movie_name, rating):
#     # get the similarity score and subtracting 2.5 from the rating to fix placement of bad movies in the list
#     similar_score = item_similarity_df[movie_name]*(rating-2.5)
#     similar_score = similar_score.sort_values(ascending=False)
#     # print(type(similar_ratings))
#     return similar_score

###########################
#           GUI CODE      #
###########################
root = Tk()
root.title("Master 2 IAM")
root.configure(bg='#4b5162')
root.geometry('700x800')

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


# create rappers to manage the gui
warpper1 = LabelFrame(root, text="Movies Watched")
warpper2 = LabelFrame(root, text="Movies Suggested")
warpper1.pack(padx=10, pady=10, fill="both", expand="yes")
warpper2.pack(padx=10, pady=10, fill="both", expand="yes")


# drop down box with thier label
Label(warpper1, text="Select 3 movies you watched and rate them").grid(row=0, column=0, padx=10, pady=10)

# dropdown menu 1
moviecombo = ttk.Combobox(warpper1, value=movielist)
ratingcombo = ttk.Combobox(warpper1, value=rating)

# dropdown menu 2
moviecombo2 = ttk.Combobox(warpper1, value=movielist)
ratingcombo2 = ttk.Combobox(warpper1, value=rating)

# dropdown menu 1
moviecombo3 = ttk.Combobox(warpper1, value=movielist)
ratingcombo3 = ttk.Combobox(warpper1, value=rating)

# button function to add selected movies
fake_user=[]
def addmovie(event):
        Label(warpper1, text=moviecombo.get()).grid(row=6, column=0, padx=10, pady=10)
        mov = [moviecombo.get(), int(ratingcombo.get())]
        fake_user.append(mov)
        print(fake_user)


def addmovie2(event):
        Label(warpper1, text=moviecombo2.get()).grid(row=6, column=2, padx=10, pady=10)
        mov = [moviecombo2.get(), int(ratingcombo2.get())]
        fake_user.append(mov)
        print(fake_user)


def addmovie3(event):
        Label(warpper1, text=moviecombo3.get()).grid(row=6, column=3, padx=10, pady=10)
        mov = [moviecombo3.get(), int(ratingcombo3.get())]
        fake_user.append(mov)
        print(fake_user)

# comboSelect bind 1
ratingcombo.current(0)
ratingcombo.bind("<<ComboboxSelected>>", addmovie)
ratingcombo.grid(row=1, column=3, padx=10, pady=10)
moviecombo.current(0)
moviecombo.grid(row=1, column=0, padx=10, pady=10)
# comboSelect bind 2
ratingcombo2.bind("<<ComboboxSelected>>", addmovie2)
ratingcombo2.grid(row=2, column=3, padx=10, pady=10)
moviecombo2.grid(row=2, column=0, padx=10, pady=10)
# comboSelect bind 3
ratingcombo3.bind("<<ComboboxSelected>>", addmovie3)
ratingcombo3.grid(row=3, column=3, padx=10, pady=10)
moviecombo3.grid(row=3, column=0, padx=10, pady=10)


def calculate():
    # collecting similar movies so we can show the result
    similar_movies = pd.DataFrame()
    for movie, rating in fake_user:
        similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)

    # printing the recommended list
    print(similar_movies.sum().sort_values(ascending=False))


B1 = Button(warpper1, text="Add Your Movie", command=calculate).grid(row=4, column=2, padx=10, pady=10)

# show what user have chosen
Label(warpper1, text="your selected movies").grid(row=5, column=0, padx=10, pady=10)
# list result in a list box
Label(warpper2, text="The Suggested Movies").grid(row=0, column=0, padx=10, pady=10)
listbox = Listbox(warpper2)
listbox.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

