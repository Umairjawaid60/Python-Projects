#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


# In[3]:


a = sorted(dataset)
display(a)


# In[4]:


q1,q3 = np.percentile(dataset,[25,75])
display(q1,q3)


# In[5]:


iqr = q3 - q1
display(iqr)


# In[6]:


lower_bound = q1 - (1.5*iqr)
upper_bound = q3 + (1.5*iqr)

display(lower_bound, upper_bound)


# In[8]:


outliers = (x for x in a if x < lower_bound or x > upper_bound)
detected = (x for x in a if lower_bound <= x <= upper_bound)

# To print the values, convert the generator expressions to lists
print("Outliers:", list(outliers))  # Print the list of outliers
print("Values within the range:", list(detected))


# In[ ]:




