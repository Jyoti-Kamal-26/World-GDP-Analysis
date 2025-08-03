#!/usr/bin/env python
# coding: utf-8

# In[16]:


# In[17]:


import pandas as pd

import plotly.express as ex
import plotly.offline as pyo

df = pd.read_csv('gdp.csv')
df.head()


# In[18]:


df.shape


# ##### check for Null values

# In[19]:


df.isna().sum()


# ### Check Discription of each column

# In[20]:


df['Country Name'].describe()


# In[21]:


df['Country Code'].describe()


# In[22]:


print('min year: ',df['Year'].min())
print('max year: ',df['Year'].max())


# ### Analysing Arab World

# In[23]:


df_pr = df[df['Country Name']=='Arab World']


# In[24]:


df_pr.plot(kind='line',x='Year',y='Value',
           figsize=(8,3),
           grid = True,
           ylabel='GDP',
           xlabel='YEARS')


# ### Finding GDP growth at a country

# In[25]:


df_pr = df[df['Country Name']=='India']
data = df_pr.values
gdp_change=[0]

for i in range(1,len(data)):
    prev=data[i-1][3]
    cur=data[i][3]

    gdp_change.append(round(((cur-prev)/prev)*100,2))
df_pr.assign(GDP=gdp_change)


# ### Finding GDP Growth for every country

# In[26]:


final_data=[]
for country_name in df['Country Name'].unique():
    df_pr = df[df['Country Name']==country_name]
    
    data = df_pr.values
    gdp_change=[0]

    for i in range(1,len(data)):
        prev=data[i-1][3]
        cur=data[i][3]

        gdp_change.append(round(((cur-prev)/prev)*100,2))
    df_pr=df_pr.assign(GDP=gdp_change)
    final_data.append(df_pr)


# In[27]:


df = pd.concat(final_data, axis=0)


# In[28]:


df.sample(10)


# In[29]:


df.groupby('Country Name')['GDP'].mean().sort_values(ascending=False)


# In[30]:


df.groupby('Country Name')['Value'].max().sort_values(ascending=False).head(50)


# In[31]:


df_pr = df[df['Country Name']=='World']
fig=ex.line(df_pr,x='Year',y='Value', title='World GDP analysis')
fig
pyo.plot(fig, filename='World GDP.html')


# In[32]:


df_pr = df[df['Country Name']=='India']
fig=ex.line(df_pr,x='Year',y='Value', title='Indian GDP analysis')

pyo.plot(fig, filename='Indian GDP.html')


# In[ ]:




