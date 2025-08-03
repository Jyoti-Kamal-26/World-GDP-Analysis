#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

import plotly.express as px
import plotly.offline as pyo

df = pd.read_csv('gdp.csv')

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
df = pd.concat(final_data, axis=0)
df.head()


# ### GDP of each country

# In[7]:


os.mkdir('GDP Indivisual')
for country_name in df['Country Name'].unique():
    df_pr = df[df['Country Name']==country_name]
    fig=px.line(df_pr,x='Year',y='Value', title=country_name+'GDP analysis')
    pyo.plot(fig, filename='GDP Indivisual/'+country_name+'.html',auto_open=False)


# In[8]:


os.mkdir('GDP Indivisual WRT World')
for country_name in df['Country Name'].unique():
    df_pr = df[df['Country Name']==country_name]
    fig=px.line(df_pr,x='Year',y='Value', title=country_name+'GDP analysis', range_y=(0,80000000000000))
    pyo.plot(fig, filename='GDP Indivisual WRT World/'+country_name+'.html',auto_open=False)


# ### GDP analysis of all countries

# In[9]:


fig=px.line(df,x='Year',y='Value', title='GDP analysis of all countries',color='Country Name')
pyo.plot(fig, filename='countries GDP.html')


# ### GDP comparision between specific countries

# In[10]:


fig=px.line(df_pr,x='Year',y='Value', title='GDP comparision between india|China|Pakistan|World',color='Country Name')
pyo.plot(fig, filename='CHN_IND_PKS_WLD.html')


# In[11]:


# c1=df[df['Country Name']=='India']
# c2=df[df['Country Name']=='World']
# c3=df[df['Country Name']=='China']
# c4=df[df['Country Name']=='Pakistan']
# df_pr=pd.concat([c1,c2,c3,c4],axis=0)

##------------- OR---------------

lst=['IND','ITA','USA','CHN']
dfs = []
for i in lst:
    dfs.append(df[df['Country Code']==i])
    df_pr=pd.concat(dfs,axis=0)


# In[12]:


fig=px.line(df_pr,x='Year',y='Value', title='GDP comparision between'+'|'.join(lst),color='Country Name')
pyo.plot(fig, filename='_'.join(lst)+'.html')


# In[13]:


def compare_gdp(lst, isOpen):
    dfs=[]
    for i in lst:
        dfs.append(df[df['Country Code']==i])
        df_pr=pd.concat(dfs,axis=0)

    fig=px.line(df_pr,x='Year',y='Value', title='GDP comparision- '+'|'.join(lst),color='Country Name')
    pyo.plot(fig, filename='_'.join(lst)+'.html',auto_open=isOpen)


# In[14]:


compare_gdp(['IND','CHN'],True)


# In[15]:


def compare_gdp(lst, isOpen):
    dfs=[]
    for i in lst:
        dfs.append(df[df['Country Code']==i])
        df_pr=pd.concat(dfs,axis=0)

    fig=px.line(df_pr,x='Year',y='GDP', title='GDP comparision- '+'|'.join(lst),color='Country Name')
    pyo.plot(fig, filename='GDP'+'_'.join(lst)+'.html',auto_open=isOpen)


# In[16]:


compare_gdp(['IND','CHN'],True)


# ### GDP Comparision between all countries

# In[17]:


fig=px.line(df,x='Year',y='GDP', title='GDP comparision',color='Country Name')
pyo.plot(fig, filename='GDP Growth'+'.html',auto_open=True)


# ### GDP Growth of all countries graph indivisual

# In[ ]:


os.mkdir('GDP Growth indivisual country')
for country_name in df['Country Code'].unique():
    df_pr=df[df['Country Code']==country_name]
    fig=px.line(df_pr,x='Year',y='GDP',title=country_name)
    pyo.plot(fig, filename='GDP Growth indivisual country/'+country_name+'.html', auto_open= False)


# ### GDP Growth between 1960-1916

# In[ ]:


dfs=[]
for country_name in df['Country Name'].unique():
    df_pr=df[df['Country Name']==country_name]
    # print(country_name, len(df_pr))
    if (len(df_pr)==57):
        dfs.append(df_pr)
df_pr=pd.concat(dfs,axis=0)


# In[ ]:


fig=px.line(df_pr,x='Year',y='GDP',title='GDP Growth', color='Country Name')
pyo.plot(fig, filename='GDP growth.html', auto_open= True)


# In[ ]:




