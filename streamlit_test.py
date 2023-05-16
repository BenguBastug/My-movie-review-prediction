import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titles=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/movies_noexplode.csv') #Sentiment analysis
#tiltes=titles[titles['tconst', 'primaryTitle', 'genre', 'compound')]]
#getting dir names
dir_names_df = pd.read_csv("https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/pivot_dir.csv")
#getting the dir list
dir_names = dir_names_df.columns.drop('tconst').tolist()
#dir dataframes
directors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/imbdir_rating.csv')
directors1=directors.sort_values(by="dir_rating", ascending=False)
directors1=directors1.reset_index()
directors1=directors1.drop(['index'], axis=1)
directors1= directors1[directors1["dir_rating"] > directors["dir_rating"].mean()]

directorslow = directors.sort_values(by="dir_rating", ascending=True)
directorslow=directorslow.reset_index()
directorslow=directorslow.drop(['index'], axis=1)
directorslow= directorslow[directorslow["dir_rating"] < directors["dir_rating"].mean()]
actors=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/actors_top10.csv')
table_actor_10_top = pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/table_actor_10.csv')
table_actor_10_tail = pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/table_actor_10_tail.csv')

genres_analysis=pd.read_csv('https://raw.githubusercontent.com/RuiVelho/My-movie-review-prediction/main/genres_analysis.csv')


st.set_page_config(page_title='Prediction of Futeture Movies',
                   page_icon=":movie_camera:")

dash = st.sidebar.radio(
    "Prediction of review for the future Movies",
    ('Titles Sentiment Analysis', 'Movies Statistics', 'Actors', 'How good will your movie be?'))

if dash == 'Titles Sentiment Analysis':
    st.title('Titles Sentiment Analysis')
    titles
    

if dash == 'Movies Statistics':
    col1, col2 = st.columns(2)
    with col1:
        st.title('Top Directors')
        directors1
    st.write("Average Director Rating: ", directors["dir_rating"].mean())
    with col2:
        st.title('Worst Directors')
        directorslow
    st.title('Genres Ratings')
    genres_analysis = genres_analysis.sort_values(by="count", ascending=False)
    genres_analysis
    st.write("Average Genre Rating", genres_analysis["Count_Rating"].mean())

if dash == "Actors":
    st.title('Top Actors')
    table_actor_10_top
    
    st.title('Worst Actors')
    table_actor_10_tail

#if dash == 'How good will your movie be?':

    #st.title('Prediction of review for the future Movies')

    #st.sidebar.header('Predict Your next Movies Selection')

    #director = st.sidebar.selectbox('Select the Director: ', options=dir_names + ["others"])

    #actors = st.sidebar.multiselect('Select the Actors: ', options=[1,2,3,4,5,6])
    
    #year= ('Select year: ', options=[2002,2023])

    #category = st.sidebar.selectbox('Select the category of movie: ', options=genres_analysis['genre'])
