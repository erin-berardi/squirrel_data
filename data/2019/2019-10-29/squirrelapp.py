import streamlit as st 
from PIL import Image 

import matplotlib.pyplot as plt 
import matplotlib

import seaborn as sns
import pandas as pd 
import numpy as np

DATA_URL = ('squirrelsNYC.csv')


st.markdown('# Introduction to Data Analysis')
st.markdown('### Squirrels of Central Park, NYC')


if st.button("Meet the Squirrels"):
    img=Image.open('Gray_Squirrel.jpeg')
    st.image(img,width=400, caption="Gray Squirrels")
    img=Image.open('Black_Squirrel.jpeg')
    st.image(img,width=400, caption="Black Squirrels")
    img=Image.open('cinnamon_Squirrel.jpeg')
    st.image(img,width=400, caption="Cinnamon Squirrels")
st.markdown(
   "The data was collected and made available by **[NYC open source data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)**.")
    #images=Image.open('images/meet.png')
   # st.image(images,width=600)
    #Ballons
   #st.balloons()




st.sidebar.markdown("## Side Panel")
st.sidebar.markdown('### Use this panel to explore the dataset and create own viz.')
df = pd.read_csv(DATA_URL)
lowercase = lambda x:str(x).lower()
df.rename(lowercase, axis='columns',inplace=True)

st.header('Now, Explore for Yourself the Squirrels of Central Park, NYC')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading squirrelsNYC dataset...')

    # Notify the reader that the data was successfully loaded.
data_load_state.text('Loading squirrelsNYC dataset...Completed!')
images=Image.open('excited_squirrel.jpeg')
st.title('Huzzah!')
st.image(images,width=100)


# Showing the original raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw data')
    st.write(df)
st.title('Quick  Explore')
st.sidebar.subheader(' Quick  Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")
if st.sidebar.checkbox('Basic info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')
        st.write(df.head())
    if st.sidebar.checkbox("Show Columns"):
        st.subheader('Show Columns List')
        all_columns = df.columns.to_list()
        st.write(all_columns)
   
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Descripition')
        st.write(df.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.write(df.isnull().sum())

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Create Own Visualization')
st.markdown("Tick the box on the side panel to create your own Visualization.")
st.sidebar.subheader('Create Own Visualization')
if st.sidebar.checkbox('Graphics'):
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If error, please adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox("Choose a column to plot count. Try Selecting Age ",df.columns)
        hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting primary_fur_color ",df.columns.insert(0,None))
        
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()
            
            
    if st.sidebar.checkbox('Histogram | Distplot'):
        st.subheader('Histogram | Distplot')
        st.info("If error, please adjust column name on side panel.")
        # if st.checkbox('Dist plot'):
        column_dist_plot = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting tail_twitches",df.columns)
        fig = sns.distplot(df[column_dist_plot])
        st.pyplot()
            
            
        
    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If error, please adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column). Try Selecting shift:",df.columns.insert(0,None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical). Try Selecting Any Activity",df.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
        fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
        st.pyplot()




st.sidebar.info("[Data Source](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)")
st.sidebar.info(" [Source Article](https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db)")
st.sidebar.info("Self Exploratory Visualization on palmerpenguins Code - Brought To you By [Mala Deep](https://github.com/maladeep)  ")
st.sidebar.text("Built with  ❤️ Streamlit")










