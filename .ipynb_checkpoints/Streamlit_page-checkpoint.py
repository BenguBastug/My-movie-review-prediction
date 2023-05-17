import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Prediction of Futeture Movies',
                   page_icon=":movie_camera:")

st.title('Prediction of review for the future Movies')

st.sidebar.header('Predict Your next Movies Selection')

director = st.sidebar.multiselect('Select the Director: ', options=[1,2,3,4,5,6])

actors = st.sidebar.multiselect('Select the Actors: ', options=[1,2,3,4,5,6])

category = st.sidebar.multiselect('Select the category of movie: ', options=[1,2,3,4,5,6])