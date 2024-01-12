#!/usr/bin/env python
# coding: utf-8

# ## Assignment -  1

# ###  Import the necessary libraries

# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO


# ###  Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). <br>
# Use sep= "|" while reading the data

# In[53]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|')
users


# ### Assign it to a variable called users and use the 'user_id' as index

# In[61]:


users = pd.read_csv(url,sep='|', index_col='user_id')
users


# ### See the first 10 and last 10 entries 

# In[62]:


print("--------First 10 entries -------\n", users.head(10), "\n--------Last 10 entries -------\n", users.tail(10))


# ### What is the number of observations in the dataset?

# In[18]:


num_observations = users.shape[0]
print("Number of observations :", num_observations)


# ### What is the number of columns in the dataset?

# In[63]:


num_columns = users.shape[1]
print("Number of columns :",num_columns)


# ### Print the name of all the columns.

# In[64]:


column_names = users.columns
print(column_names)


# ### How is the dataset indexed?

# In[65]:


index_info = users.index
print(index_info)


# ### What is the data type of each column?

# In[28]:


users.info()


# ### Print only the occupation column

# In[66]:


occupation_column = users['occupation']
print(occupation_column)


# ### How many different occupations are in this dataset?

# In[30]:


num_occupations = users['occupation'].nunique()
num_occupations


# ### What is the most frequent occupation?

# In[52]:


most_frequent_occupation = users['occupation'].value_counts().idxmax()

print(f"0 {most_frequent_occupation}\ndtype: object")


# ###  DataFrame Info.

# In[45]:


users.info()


# ### Describe all the columns

# In[47]:


all_columns_description = users.describe(include='all')
print("Descriptive the all columns:")
print(all_columns_description)


# ### Summarize only the occupation column

# In[49]:


occupation_summary = users['occupation'].value_counts()
print("Summary for the 'occupation' column:")
print(occupation_summary)


# ###  What is the mean age of users?

# In[50]:


mean_age = users['age'].mean()

print(mean_age)


# ###  What is the age with least occurrence?

# In[51]:


least_occurred_age=users['age'].value_counts().idxmin()
print(least_occurred_age)


# In[ ]:




