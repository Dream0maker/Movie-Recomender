from tkinter import ttk
from tkinter import *
import pandas as pd

#########################
# application code      #
#########################
# movie lens data set import
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
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
#
#
# # print(item_similarity_df.head(50))
#
# def get_similar(movie_name, rating):
#     # get the similarity score and subtracting 2.5 from the rating to fix placement of bad movies in the list
#     similar_score = item_similarity_df[movie_name] * (rating - 2.5)
#     similar_score = similar_score.sort_values(ascending=False)
#     # print(type(similar_ratings))
#     return similar_score
#

###########################
#           GUI CODE      #
###########################
root = Tk()
root.title("Master 2 IAM")
root.configure(bg='#4b5162')
root.geometry('800x800')

header = Frame(root, bg='#383c4a')
content = Frame(root, bg='#4b5162')

# root.columnconfigure(0, weight=1)    # 100%
# root.rowconfigure(0, weight=1)   # 10%
# # root.rowconfigure(1, weight=9)   # 80%
# header.grid(row=0, columnspan=2, sticky=W)
# content.grid(row=1, sticky='news')

label_header = Label(root, text='Movie Recommender', bg='#383c4a', font="AkayaTelivigala 30 bold").pack()
# end of header
moviesL = pd.read_csv('movies.csv',index_col=1).drop(['genres', 'movieId'], axis=1)
rating = [1, 2, 3, 4, 5]
# drop down box
moviecombo = ttk.Combobox(root, value=moviesL).pack(pady=20)
ratingcombo = ttk.Combobox(root, value=rating).pack()


# add button and thier function
def addmovie():
    print("hello")


B = Button(root, text="Add Your Movie", command=addmovie()).pack()

root.mainloop()

