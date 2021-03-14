import pandas as pd

# movie lens data set import
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# merging the two files to get the movies and ratings in one file + dropping unwanted columns
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

def get_similar(movie_name, rating):
    # get the similarity score and subtracting 2.5 from the rating to fix placement of bad movies in the list
    similar_score = item_similarity_df[movie_name]*(rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)
    # print(type(similar_ratings))
    return similar_score

#####################################################
#                   test                            #
#                   area                            #
#####################################################
# get user input
fake_user = []
for i in range(0,3):
    mov = (input("movie you already watched: "), int(input("your rating :")))
    fake_user.append(mov)
# some option for testting 17 Again (2009)/21 Jump Street (2012)/2012 (2009)




# collecting similar movies so we can show the result
similar_movies = pd.DataFrame()
for movie, rating in fake_user:
    similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)

# printing the recommended list
print(similar_movies.sum().sort_values(ascending=False))