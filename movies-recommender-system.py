#!/usr/bin/env python
# coding: utf-8

# #### https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

# In[1]:


import pandas as pd
import numpy as np
import ast


# In[2]:


movies = pd.read_csv("tmdb_5000_movies.csv")
casts = pd.read_csv("tmdb_5000_credits.csv")


# In[3]:


movies.head(1)


# In[4]:


casts.head(1)


# #### merging the two datasets on the basis of title

# In[5]:


movies = movies.merge(casts,on="title")


# In[6]:


## there we dont need all the columns ,so we are choosing the columns that is perfect to create tags

# movie_id
# genres
# keywords
# overview
# title
# cast
# crew


# In[7]:


movies = movies[["movie_id","title","genres","keywords","overview","cast","crew"]]


# In[8]:


movies.info()


# In[9]:


# finding out null values in movies
movies.isnull().sum()


# In[10]:


# since overview has only 3 values missing, we are going to drop the missing rows
movies.dropna(inplace=True)


# In[11]:


movies.isnull().sum()


# In[12]:


# creating a function to extract generes from gener column
def convert(obj):
    lists = []
    for i in ast.literal_eval(obj):
        lists.append(i["name"])
    return lists    


# In[13]:


movies["genres"] = movies["genres"].apply(convert)


# In[14]:


movies.head()


# In[15]:


movies.iloc[0]["keywords"]


# In[16]:


movies["keywords"] = movies["keywords"].apply(convert)


# In[17]:


movies.head()


# In[18]:


movies.iloc[0]["cast"]


# In[19]:


def cast_converter(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter < 3:
            l.append(i["name"])
            counter +=1
        else:
            break
    return l        


# In[20]:


movies["cast"] = movies["cast"].apply(cast_converter)


# In[21]:


movies.head()


# In[22]:


movies.iloc[0]["crew"]


# In[23]:


def crew_convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            l.append(i["name"])
            break
    return l


# In[24]:


movies["crew"]=movies["crew"].apply(crew_convert)


# In[25]:


movies.head()


# In[26]:


movies["overview"] = movies["overview"].apply(lambda x:x.split())


# In[27]:


movies.head()


# In[28]:


# removing spaces between names and geners
movies["cast"] = movies["cast"].apply(lambda x:[i.replace(" ","")for i in x])
movies["crew"] = movies["crew"].apply(lambda x:[i.replace(" ","")for i in x])
movies["genres"] = movies["genres"].apply(lambda x:[i.replace(" ","")for i in x])
movies["keywords"] = movies["keywords"].apply(lambda x:[i.replace(" ","")for i in x])


# In[29]:


movies.head()


# In[30]:


movies["tags"] = movies["genres"] + movies["keywords"] + movies["overview"] + movies["cast"] + movies["crew"]


# In[31]:


new_movies = movies[["movie_id","title","tags"]]


# In[32]:


new_movies


# #### how we have tags with us, now we will perform verterization on this tags

# In[33]:


new_movies['tags'] = new_movies['tags'].apply(lambda x: " ".join(x))


# In[34]:


new_movies


# In[35]:


get_ipython().system('pip install nltk')


# In[36]:


import nltk


# In[37]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[38]:


# lets remove duplicates live love and loved are similar or duplicates
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)    


# In[39]:


new_movies["tags"] = new_movies["tags"].apply(stem)


# In[40]:


new_movies


# In[41]:


print(new_movies.iloc[0,2])


# In[42]:


from sklearn.feature_extraction.text import CountVectorizer


# In[43]:


cv = CountVectorizer(max_features=5000,stop_words="english")


# In[44]:


vectors = cv.fit_transform(new_movies["tags"]).toarray()


# In[45]:


vectors


# In[46]:


cv.get_feature_names()


# In[47]:


# calculating the distance between every movie with every other movie
# we are removing cosine distance of each movie with every other movie


# In[48]:


from sklearn.metrics.pairwise import cosine_similarity


# In[49]:


similarity = cosine_similarity(vectors)


# In[50]:


similarity.shape


# In[51]:


def recommend(movie):
    movie_index = new_movies[new_movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]
    
    for i in movies_list:
        print(new_movies.iloc[i[0]].title)
    


# In[63]:


recommend("Avatar")


# In[57]:


import pickle


# In[59]:


pickle.dump(new_movies.to_dict(),open("movies_dict.pkl",'wb'))


# In[60]:


pickle.dump(similarity,open("similarity.pkl","wb"))


# In[ ]:




