#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


singapore = pd.read_csv('listings (1).csv.gz')


# In[3]:


singaporeDataFrame = pd.DataFrame(singapore)


# In[4]:


singaporeDataFrame.describe()


# In[5]:


print(singaporeDataFrame.isnull().sum())
pd.options.display.max_rows = 4000


# In[6]:


singaporeDataFrame.head()


# In[7]:


print(singaporeDataFrame.columns)


# In[8]:


nonIntSingaporeData = singaporeDataFrame.select_dtypes(exclude = ['int64', 'float64'])
print(nonIntSingaporeData.head())
print("------Singapore host_acceptance_rate-------")
print(nonIntSingaporeData['host_acceptance_rate'])
print("------Singapore host_response_rate-------")
print(nonIntSingaporeData['host_response_rate'])
print("------Singapore host_location-------")
print(nonIntSingaporeData['host_location'])


# In[9]:


intSingaporeData = singaporeDataFrame.select_dtypes(include = ['int64', 'float64'])
intSingaporeData = intSingaporeData.join(singaporeDataFrame['price'])


# In[10]:


#print(intSingaporeData.describe())
print(intSingaporeData.columns)


# In[11]:


intSingaporeData.isnull().sum()


# In[1]:





# In[ ]:





# In[28]:


for col in intSingaporeData.columns:
    if(intSingaporeData[col].isnull().sum()>2000):
        intSingaporeData.drop(col, axis = 1, inplace = True)
        
    


# In[29]:


intSingaporeData.describe()


# In[15]:


smallIntSingaporData = intSingaporeData.sample(n=100, random_state=1)
print(smallIntSingaporData.head())


# In[16]:


smallerIntSingaporeData = smallIntSingaporData
smallerIntSingaporeData = smallerIntSingaporeData.iloc[:, 0:10]
smallerIntSingaporeData = smallerIntSingaporeData.join(smallIntSingaporData[['price']])
print(smallerIntSingaporeData.head())


# In[1]:


smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace('$', '')
smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace(',', '')
smallerIntSingaporeData['price']  = smallerIntSingaporeData['price'].astype('float64')


# In[2]:


print(smallerIntSingaporeData.describe())


# In[3]:


import seaborn as sb
plt.figure(figsize = (10, 10))
sb.pairplot(data = smallerIntSingaporeData)


# In[24]:


smallIntSingaporData = intSingaporeData.sample(n=100, random_state=1)
smallerIntSingaporeData = smallIntSingaporData.iloc[:, 9:20]
smallerIntSingaporeData = smallerIntSingaporeData.join(smallIntSingaporData[['price']])
smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace('$', '')
smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace(',', '')

smallerIntSingaporeData['price']  = smallerIntSingaporeData['price'].astype('float64')
#print(smallerIntSingaporeData.describe())
import seaborn as sb
plt.figure(figsize = (10, 10))
sb.pairplot(data = smallerIntSingaporeData)


# In[25]:


smallIntSingaporData = intSingaporeData.sample(n=100, random_state=1)
smallerIntSingaporeData = smallIntSingaporData.iloc[:, 20:30]
smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace('$', '')
smallerIntSingaporeData['price'] = smallerIntSingaporeData['price'].str.replace(',', '')

smallerIntSingaporeData['price']  = smallerIntSingaporeData['price'].astype('float64')
#print(smallerIntSingaporeData.describe())
import seaborn as sb
plt.figure(figsize = (10, 10))
sb.pairplot(data = smallerIntSingaporeData)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




