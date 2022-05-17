#!/usr/bin/env python
# coding: utf-8

# # Can we find the best place to have a squirrel interaction?!?!?
# ### We will be visiting NYC and wish to have an opportunity to see some famously bold squirrels in Central Park.  We can use data to help answer our question.

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# # Initial data preparation

# In[2]:


df = pd.read_csv('nyc_squirrels.csv')
df


# In[3]:


df.isna().sum()


# In[4]:


df.info()


# In[5]:


df.describe().T


# In[6]:


df = df.drop(['zip_codes'], axis = 1)


# In[7]:


df_num = df.select_dtypes(np.number)
df_cat =df.select_dtypes(object)


# In[8]:


df_num


# In[9]:


df_cat
df_cat.isna().sum()


# In[10]:


df['location'].value_counts(dropna=False)


# In[11]:


df['location']=df['location'].fillna('Ground Plane')
df['location'].value_counts(dropna=False)


# In[12]:


df['above_ground_sighter_measurement'].value_counts(dropna=False)
df['above_ground_sighter_measurement']=df['above_ground_sighter_measurement'].fillna('FALSE')


# In[13]:


df['above_ground_sighter_measurement'].value_counts(dropna=False)


# In[14]:


df['other_activities'].value_counts(dropna = False)


# In[15]:


df['other_activities']=df['other_activities'].fillna('No Activity')
df['other_activities'].value_counts(dropna = False)


# In[16]:



df['other_interactions']=df['other_interactions'].fillna('No Interactions')
df['other_interactions'].value_counts(dropna = False)


# In[17]:


df['color_notes'].value_counts(dropna = False)


# In[18]:


df['specific_location'].value_counts(dropna = False)


# In[19]:


#columns to drop, too many NaN values
cols_drop = ['color_notes','specific_location']


# In[20]:


df['age'].value_counts(dropna = False)


# In[21]:


df['age']=df['age'].fillna('Adult')
df.loc[df["age"] == "?", "age"] = "Adult"
df['age'].value_counts(dropna = False)


# In[22]:


df['primary_fur_color'].value_counts(dropna=False)


# In[23]:


df['primary_fur_color']=df['primary_fur_color'].fillna('Gray')
df['primary_fur_color'].value_counts(dropna=False)


# In[24]:


df['combination_of_primary_and_highlight_color'].value_counts()


# In[25]:


df.loc[df["combination_of_primary_and_highlight_color"] == "+", "combination_of_primary_and_highlight_color"] = "Gray+"
df["combination_of_primary_and_highlight_color"].value_counts()


# In[26]:


df['highlight_fur_color'] = df['highlight_fur_color'].fillna('No Highlight')
df['highlight_fur_color'].value_counts(dropna=False)


# In[27]:


df = df.drop(cols_drop,axis=1)
df.isna().sum()


# In[28]:


df_num = df.select_dtypes(np.number)
df_cat =df.select_dtypes(object)


# In[29]:


df['date'].dtypes
df['date']=df['date'].astype(str)


# In[30]:


df['date'] = pd.to_datetime(df['date'],format= '%m%d%Y')


# In[31]:


df.head()


# ## Save our clean dataset to a .csv file

# In[42]:


df.to_csv('squirrelsNYC.csv')


# # EDA (Exploratory Data Analysis)

# In[32]:


df[['running', 'chasing','climbing', 'eating', 'foraging']] = df[['running', 'chasing','climbing', 'eating', 'foraging']].astype(int)


# In[33]:


df[['kuks', 'quaas','moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent','runs_from']] = df[['kuks', 'quaas',
       'moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent',
       'runs_from']].astype(int)


# # Squirrel Sightings in Central Park

# ![Distribution_of_squirrels.png](attachment:Distribution_of_squirrels.png)

# # Age of Squirrels

# In[34]:


fig,ax = plt.subplots()
sns.countplot(data=df, x= 'age')
plt.show()


# # Distribution of Main Colorings

# In[35]:


fig,ax = plt.subplots()
plt.rcParams["figure.figsize"] = (15,8)
sns.countplot(data=df, x= 'primary_fur_color')
plt.show()


# # Where does each color gang hang out?

# ![main_squirrel_color.png](attachment:main_squirrel_color.png)

# # Distribution of Highlight colorings

# In[36]:


fig,ax = plt.subplots()
plt.rcParams["figure.figsize"] = (15,8)
sns.countplot(data=df, x= 'highlight_fur_color')
plt.xticks(rotation = 45)
plt.show()


# # What color combinations am I most likely to see?

# In[37]:


fig,ax = plt.subplots()
plt.rcParams["figure.figsize"] = (15,8)
sns.countplot(data=df, x= 'combination_of_primary_and_highlight_color')
plt.xticks(rotation = 45)
plt.show()


# # What type of tail movements will I see?

# In[55]:


df_group0 = df.groupby('age').agg({'tail_twitches':'mean','tail_flags':'mean'})


# In[56]:


df_group0.plot(kind = 'bar')
plt.xticks(rotation = 360)


# # Should I be focusing more on the ground or in the trees?

# In[38]:


fig,ax = plt.subplots()
sns.countplot(data=df, x = 'location')
plt.show()


# # What activities will they be doing?

# In[39]:


df_group = df.groupby('location').agg({'running':'sum','chasing':'sum','climbing':'sum','eating':'sum','foraging':'sum'})


# In[40]:


df_group


# In[41]:


df_group.plot(kind = 'bar', color='rygbm')
plt.xticks(rotation = 360)


# In[43]:


df_group2 = df.groupby('shift').agg({'running':'sum','chasing':'sum','climbing':'sum','eating':'sum','foraging':'sum'})


# In[44]:


df_group2.plot(kind = 'bar', color='rygbm')
plt.xticks(rotation = 360)


# # Will I be able to hear any vocalizations?

# In[45]:


df_group3 = df.groupby('shift').agg({'kuks':'sum','quaas':'sum','moans':'sum'})


# In[46]:


df_group3.plot(kind = 'bar')
plt.xticks(rotation = 360)


# # Should I focus on listening to Adults or Juveniles?

# In[47]:


df_group4 = df.groupby('age').agg({'kuks':'mean','quaas':'mean','moans':'mean'})


# In[48]:


df_group4.plot(kind = 'bar')
plt.xticks(rotation = 360)


# In[49]:


df_group5 = df.groupby('age').agg({'approaches':'mean','indifferent':'mean','runs_from':'mean',})


# In[50]:


df_group5.plot(kind = 'bar')
plt.xticks(rotation = 360)


# # Will the squirrels actually interact with me?

# ![Interactions_with_people.png](attachment:Interactions_with_people.png)

# ![NYC_Food_Carts.png](attachment:NYC_Food_Carts.png)

# In[ ]:





# # Can we answer our initial question?
# ## Can we find the best place to have a squirrel interaction?!?!?

# ### At this point, we would consider a Machine Learning model to try and predict something that cannot be analyzed using visualizations. 
# ### However, our initial question of finding the best place for squirrel interactions can be gleaned from the visualizations.  So a model is not necessary.  
# ### I would suggest that you purchase some food from a snack truck and enter the park at the South entrance.  Choose a lovely place to set up a picnic and wait for the ensuing squirrel action!

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




