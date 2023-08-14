import pickle
import pandas as pd
import streamlit as st
import requests

st.title("MOVIE RECOMMENDER SYSTEM")

# enter your own API key here
api_key = "YOUR API KEY HERE"

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

TMDB_BASE_URL = 'https://api.themoviedb.org/3'
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def fetch_poster_url(movie_title):
    # Make an API request to search for the movie by title
    response = requests.get(
        f'{TMDB_BASE_URL}/search/movie',
        params={'api_key':api_key ,'query': movie_title}
    )
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        return f'{POSTER_BASE_URL}{poster_path}'
    else:
        return None

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]
    
    recommend_list = []
    for movie in movies_list:
        
        recommend_list.append(movies.iloc[movie[0]].title)
        
    return recommend_list    

movies = pd.DataFrame(movies_dict)

selected_movie = st.selectbox('Chose a Movie', movies["title"].values)



# Create a button
if st.button('Recommend'):
    
    recommended_movies = recommend(selected_movie)
    movies_url = []
    for movie in recommended_movies:
        movies_url.append(fetch_poster_url(movie))
        
        
    
    col1, col2, col3 ,col4, col5= st.columns(5)
    
#    for movie in recommended_movies:
#        st.write(movie)
#        movie_url = fetch_poster_url(movie)
#        if movie_url:
#            st.image(movie_url, use_column_width=True)
#        else:
#            st.write("Poster not available")
         

    
    with col1:
         st.header(recommended_movies[0])   
         st.image(movies_url[0],use_column_width=True)
        
    with col2:
        st.header(recommended_movies[1])   
        st.image(movies_url[1],use_column_width=True)  
        
    with col3:
        st.header(recommended_movies[2])   
        st.image(movies_url[2],use_column_width=True)  

    with col4:
        st.header(recommended_movies[3])   
        st.image(movies_url[3],use_column_width=True)  
        
    with col5:
        st.header(recommended_movies[4])   
        st.image(movies_url[4],use_column_width=True)          
