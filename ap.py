import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    TITLE = movies[movies.title.str.contains(movie)].iloc[0]["title"]

    INDEX = movies[movies.title.str.contains(movie)].iloc[0].movie_id

    print(TITLE)
    print(INDEX)

    return movies[movies.movie_id.isin(correlated_movie_matrix[INDEX].sort_values(ascending=False).head(10).index.to_list())]["title"]


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

correlated_movie_matrix_dict = pickle.load(open('correlated_movie_matrix.pkl','rb'))
correlated_movie_matrix = pd.DataFrame(correlated_movie_matrix_dict)


st.title('Movie Recommender System')


titles_dict = pickle.load(open('titles_.pkl','rb'))
titles = pd.DataFrame(titles_dict)
titles = pd.DataFrame(pd.Series(titles['title']).drop_duplicates())
# titles = list(set(titles))

select_movie_name = st.selectbox('How would you like to be contacted?',
                      (titles['title'].values))


# recommend('Gladiator')

if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)

# print(recommend('Thomas Crown Affair, The'))
