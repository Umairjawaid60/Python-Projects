#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


# In[9]:


a = sorted(dataset)
display(a)


# In[10]:


q1,q3 = np.percentile(dataset,[25,75])
display(q1,q3)


# In[11]:


iqr = q3 - q1
display(iqr)


# In[12]:


lower_bound = q1 - (1.5*iqr)
upper_bound = q3 + (1.5*iqr)

display(lower_bound, upper_bound)


# In[17]:


outliers = (x for x in a if x < lower_bound or x > upper_bound)
detected = (x for x in a if lower_bound <= x <= upper_bound)

print("Outliers:", list(outliers))  
print("Values within the range:", list(detected))


# In[19]:


import matplotlib.pyplot as plt

outliers = [102, 107, 108]
values_within_range = [10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 17, 19]

plt.scatter(range(len(values_within_range)), values_within_range, label='Values within the range')
plt.scatter([outliers.index(x) for x in outliers], outliers, color='red', label='Outliers')

plt.title('Outliers and Values within Range')
plt.xlabel('Data Point Index')
plt.ylabel('Value')
plt.legend()

plt.show()


# In[ ]:




