import pandas as pd
import random

# movie lens data set improt
ratings = pd.read_csv('DataSet/ratings.csv')
movies = pd.read_csv('DataSet/movies.csv')

# merging the two files to get the movies and ratings in one file + droping unwanted colmus
ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)

# changing the data structure to ease the work
user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
# print(user_ratings.head())

# remove movies who were rated by lesser than 10 user and fill Nan with 0
user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)
# print(user_ratings)
# applying the pearson methode to get the similarities between the movies
item_similarity_df = user_ratings.corr(method='pearson')
# print(item_similarity_df.head(50))

def get_similar(movie_name,rating):
    # get the similarity score and subtracting 2.5 from the rating to fix placement of bad movies in the list
    similar_score = item_similarity_df[movie_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    # print(type(similar_ratings))
    return similar_score

#####################################################
#                   test                            #
#                   area                            #
#####################################################

fake_user = []
for i in range(5):
    film = random.choice(user_ratings.columns)
    print(film)
    print("please rate it from 0 to 5")
    x=input()
    if x:
      mov = (film), int(x)
      fake_user.append(mov)
    else:
        i += 1
if not fake_user:
    print("please rate at least one movie ! ")
else:
    print(fake_user)

    # collecting similar movies so we can show the result
    similar_movies = pd.DataFrame()
    for movie, rating in fake_user:
        similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)

        # printing the recomended list

    list = [similar_movies.sum().sort_values(ascending=False)]
    print(list)









