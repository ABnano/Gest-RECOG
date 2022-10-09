#!/usr/bin/env python
# coding: utf-8

# # STEP #1: IMPORTING LIBRARIES

# In[ ]:


# import libraries 
import pandas as pd # Import Pandas for data manipulation using dataframes
import numpy as np # Import Numpy for data statistical analysis 
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import seaborn as sns # Statistical data visualization


# # STEP #2: LOADING DATA

# In[ ]:


df = pd.read_csv('')
df.head()
df.tail()


# # STEP #3: VISUALIZING THE DATA

# In[ ]:


sns.pairplot(bank_df, hue = '', vars = ['', ''] 


# In[ ]:


sns.countplot(bank_df[''], label = "") 


# In[ ]:


plt.figure(figsize=[6,12])
plt.subplot(211)
sns.countplot(x = '', data = training_set)
plt.subplot(212)
sns.countplot(x = '', hue = '', data=training_set)


# In[ ]:


plt.figure(figsize=(40,30))
sns.countplot(x = '', hue = '', data=training_set)


# In[ ]:


plt.figure(figsize=(10,10)) 
sns.heatmap(Kyphosis_df.corr(), annot=True) 

