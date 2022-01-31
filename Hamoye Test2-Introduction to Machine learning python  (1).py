#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[11]:


food_data = pd.read_csv('FoodBalanceSheets.csv',encoding='latin1')


# In[12]:


print(food_data)


# In[13]:


food_data.head()


# In[14]:


food_data.describe()


# In[41]:


print(type(food_data))


# In[42]:


print(food_data.shape)


# In[44]:


print(food_data.ndim)


# In[15]:


food_data.isnull().sum().


# In[18]:


food_data.duplicated().any()


# In[19]:


food_data.groupby('Area')['Area'].count()


# In[46]:


food_data.groupby('Area').count()


# In[28]:


food_data.groupby('Element')['Element'].count()


# In[52]:


food_data.iloc()


# In[53]:


food_data.loc()


# In[29]:


food_data.groupby('Unit')['Unit'].count()


# In[54]:


food_data.iloc[:]


# In[35]:


food_data.groupby('Y2014')['Y2014'].count()


# In[36]:


food_data.groupby('Y2015')['Y2015'].count()


# In[39]:


food_data.groupby('Y2018')['Y2018'].count()


# In[11]:


y=[(2,4),(7,8),(1,5,9)]
X=y[1][1]
X=y[1][-1]
print(X)


# In[61]:


my_tuppy=(1,2,5,8)
my_tuppy[2]=6


# In[66]:


S=[['him','sell'], [90, 28, 43]]
S[0][1][1]


# In[2]:


#creating pandas Dataframe
import numpy as np
import pandas as pd
array=[[35,'Portugal', 94], [33,'Argentia', 93],[30,'Brazil',92]]
col=['Age', 'Nationality', 'Overall']
var=pd.DataFrame(data=array, index=[1,2,3], columns=col)
print(var)


# In[ ]:




