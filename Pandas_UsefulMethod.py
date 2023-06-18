#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("D:\\Python for Finance\\Python-Finance-QuantConnect\\03-Core-Pandas\\tips.csv")


# In[4]:


df


# In[5]:


def last_four(num):
    return str(num)[-4:]


# In[6]:


df['CC Number'].apply(last_four)


# In[7]:


df['total_bill'].mean()


# In[8]:


def yelp(price):
    if price<10:
        return '$'
    elif price<30:
        return '$$'
    else:
        return '$$$'
    


# In[9]:


df['Yelp']=df['total_bill'].apply(yelp)


# In[10]:


df['Yelp']


# In[11]:


df[df['Yelp']=='$']


# In[12]:


lambda bill:bill*2


# In[13]:


df['total_bill'].apply(lambda bill:bill*2)


# In[20]:


def quality(billamount,tipsgiven):
    if tipsgiven/billamount>0.25:
        return("Generous")
    else:
        return("Other")


# In[15]:


df['Quality']=df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)


# In[16]:


df


# In[17]:


df[df['Quality']=='Generous']


# In[21]:


df['Quality']=np.vectorize(quality)(df['total_bill'],df['tip'])


# In[22]:


df


# In[23]:


df=pd.read_csv("D:\\Python for Finance\\Python-Finance-QuantConnect\\03-Core-Pandas\\tips.csv")


# In[24]:


df.describe()


# In[25]:


df.describe().transpose()


# In[27]:


df.sort_values('tip')


# In[30]:


df.sort_values('total_bill',ascending=False)


# In[31]:


df.sort_values(['total_bill','tip'])


# In[32]:


df['tip'].max()


# In[33]:


df['tip'].idxmax()


# In[34]:


df.corr()


# In[36]:


df['sex'].value_counts()


# In[37]:


df['day'].unique()


# In[38]:


df['day'].nunique()


# In[40]:


df['day'].value_counts()


# In[41]:


df.replace('Female','F')


# In[42]:


df.replace(['Female','Male'],['F','M'])


# In[43]:


mymap={'Male':'M','Female':'F'}


# In[45]:


df['sex'].map(mymap)


# In[50]:


simpledf=pd.DataFrame([1,2,2],['a','b','c'])


# In[51]:


simpledf


# In[54]:


simpledf.drop_duplicates()


# In[56]:


df[df['total_bill'].between(10,20,inclusive=True)]


# In[57]:


df.nlargest(10,'tip')


# In[58]:


df.nlargest(15,'total_bill')


# In[62]:


df.sort_values('total_bill',ascending=False).iloc[0:15]


# In[64]:


df.nsmallest(10,'total_bill')


# 

# In[65]:


df.sample(5)


# In[66]:


df.sample(5)


# In[ ]:




