#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[5]:


train = pd.read_csv('titanic_train.csv')


# In[ ]:


train.head()


# In[7]:


train.isnull()


# In[8]:


sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[9]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train)


# In[10]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')


# In[14]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')


# In[15]:


sns.countplot(x='SibSp',data=train)


# In[19]:


train['Fare'].hist(color='blue',bins=40,figsize=(8,4))


# In[20]:


sns.boxplot(x='Pclass',y='Age',data=train)


# In[21]:


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age


# In[22]:


train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)


# In[23]:


sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[24]:


train.drop('Cabin',axis=1,inplace=True)


# In[25]:


train.head()


# In[26]:


train.info()


# In[ ]:




