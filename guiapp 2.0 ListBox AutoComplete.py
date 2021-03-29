from tkinter import ttk
from tkinter import *
import pandas as pd

####################################################################################################################
#                                           backend                                                               ##
####################################################################################################################
# movie lens data set import
ratings = pd.read_csv('DataSet/ratings.csv')
movies = pd.read_csv('DataSet/movies.csv')

# merging the two files to get the movies and ratings in one file + dropping unwanted columns
ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)

# changing the data structure to ease the work
user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')

# remove movies who were rated by lesser than 10 user and fill Nan with 0
user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)

# movie list shown in dropdown menu
movie_list = []
for i in range(0, len(user_ratings.columns)):
    movie_list.append(user_ratings.columns[i])

# applying the pearson methode to get the similarities between the movies
item_similarity_df = user_ratings.corr(method='pearson')


def get_similar(movie_name, rating):
    # get the similarity score and subtracting 2.5 from the rating to fix placement of bad movies in the list
    similar_score = item_similarity_df[movie_name] * (rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score


def checkkey(event):
    value = event.widget.get()

    # get data from movie list
    if value == '':
        data = movie_list
    else:
        data = []
        for item in movie_list:
            if value.lower() in item.lower():
                data.append(item)

                # update data in listbox
    update(data)


def update(data):
    # clear previous data
    lb.delete(0, 'end')

    # put new data
    for item in data:
        lb.insert('end', item)


################################################################################################################
#                                                  GUI CODE                                                    #
################################################################################################################

root = Tk()
root.title("Master 2 IAM")
root.configure(bg='#4b5162')
root.geometry('700x800')
root.resizable(False, False)

# create rappers to manage the gui
wrapper1 = Frame(root, bg='#383c4a')
wrapper2 = Frame(root, bg='#4b5162')
wrapper3 = Frame(root, bg='#4b5162')
wrapper1.pack(padx=0, pady=0, fill="both")
wrapper2.pack(padx=30, pady=10, fill="both", expand="yes")
wrapper3.pack(padx=30, pady=10, fill="both", expand="yes")

#########################
#         header        #
#########################
Label(wrapper1, text="MOVIE RECOMMENDER", bg='#383c4a', fg='white', font=("Chango", 33)).pack(pady=10)

#########################
#     main content      #
#########################
# drop down box with their label
Label(wrapper2, text="Select at least ONE movie", fg='white', bg='#4b5162', font=("Chango", 10)).grid(
    row=0, column=0, padx=10, pady=10)
# dropdown menu 1
movie_combo = Entry(wrapper2, width=63)
rating_combo = ttk.Combobox(wrapper2, value=[0, 1, 2, 3, 4, 5], width=32)
# creating list box
lb = Listbox(wrapper2, width=95)

# grid element to the screen
rating_combo.grid(row=1, column=3, padx=10, pady=10)
movie_combo.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
lb.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# call for the keystrock function
update(movie_list)
# button function to add selected movies
fake_user = []


def add_movie(event):
    mov = [movie_combo.get(), int(rating_combo.get())]
    fake_user.append(mov)
    global labeltest
    labeltest = Label(wrapper2, text=fake_user)
    labeltest.grid(row=4, column=0,columnspan=4 , padx=10, pady=10)


def fill(event):
    movie_combo.delete(0, END)
    movie_combo.insert(0, lb.get(ACTIVE))


# comboSelect bind
rating_combo.bind("<<ComboboxSelected>>", add_movie)
# key release bind
movie_combo.bind('<KeyRelease>', checkkey)
# list box bind to print selected item in entry box
lb.bind("<<ListboxSelect>>", fill)

# label for wrapper 3
Label(wrapper3, text="Our Recommendation", bg='#4b5162', fg='white', font=("Chango", 10)).pack(pady=20)
# show the movie recommended with their ratings
tree = ttk.Treeview(wrapper3)  # Treeview instead of listbox
# define columns
tree['columns'] = ("ID", "Movie Name")
# format Treeview
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=W, width=25)
tree.column("Movie Name", width=600, anchor=W)
# headings
tree.heading("#0", text="", anchor=W)
tree.heading("ID", text="#", anchor=W)
tree.heading("Movie Name", text="Movie Name", anchor=W)
# pack
tree.pack(padx=10, pady=10)
# # create error message when movies not selected
error_message = StringVar()


# button to suggest movie
def calculate():
    # collecting similar movies so we can show the result
    if not any(movie_combo.get()):
        error_message = ['please enter at least one movie !']
        tree.insert(parent='', index='end', iid=0, text='', values=(1, error_message))
    else:
        # error_message.config(text="                         ")
        similar_movies = pd.DataFrame()
        for movie, rating in fake_user:
            similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)
        # printing the top 20 recommended movie
        s = similar_movies.sum().sort_values(ascending=False)
        i = 0
        j = 1
        for i in range(20):
            tree.insert(parent='', index='end', iid=i, text='', values=(j, s.iloc[i:j].to_string()))
            # tree.insert(END, s.iloc[i:j].to_string())
            j = j + 1


# clear button function
def clear():
    fake_user.clear()
    movie_combo.delete(0, END)
    rating_combo.delete(0, END)
    lb.delete(0, END)
    for item in movie_list:
        lb.insert(END, item)
    for record in tree.get_children():
        tree.delete(record)
    labeltest.destroy()


# create buttons
B1 = Button(wrapper2, text="Get Recommendation", bg='#7c818c', fg='white', padx=10, pady=10, borderwidth=2,
            command=calculate).grid(row=8, column=0, padx=20, pady=10)
B2 = Button(wrapper2, text="     clear    ", bg='#7c818c', fg='white', padx=24, pady=10, borderwidth=2,
            command=clear).grid(row=8, column=3)

root.resizable(width=False, height=True)
root.mainloop()
