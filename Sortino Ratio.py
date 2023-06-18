#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


aapl=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\06-Financial-Concepts-with-Python\\apple.csv')


# In[3]:


wal=pd.read_csv("D:\\Python for Finance\\Python-Finance-QuantConnect\\06-Financial-Concepts-with-Python\\WMT.csv")


# In[4]:


aapl.info()


# In[5]:


wal.info()


# In[7]:


aapl.describe()


# In[8]:


wal.describe()


# In[9]:


aapl['Daily_Return']=aapl['Adj Close'].pct_change(1)


# In[10]:


aapl['Daily_Return']


# In[11]:


wal['Daily_Return']=wal['Adj Close'].pct_change(1)


# In[13]:


wal['Daily_Return']


# In[17]:


def compute_sortino_ratio(df,risk_free_rate=0,threshold=0):
    mean_return=df['Daily_Return'].mean()
    std_df=(df[df['Daily_Return']<threshold]['Daily_Return']).std()
    sortino_ratio=(mean_return-risk_free_rate)/std_df
    return sortino_ratio

#This is daily Sortino Ratio
    
    


# In[18]:


compute_sortino_ratio(aapl)


# In[19]:


compute_sortino_ratio(wal)


# In[20]:


def compute_sortino_ratio(df,risk_free_rate=0,threshold=0):
    mean_return=df['Daily_Return'].mean()
    std_df=(df[df['Daily_Return']<threshold]['Daily_Return']).std()
    sortino_ratio=(mean_return-risk_free_rate)/std_df
    return sortino_ratio*(252**0.5)

#This is annual Sortino Ratio


# In[21]:


compute_sortino_ratio(aapl)


# In[22]:


compute_sortino_ratio(wal)


# In[23]:


aapl['Adj Close'].plot()


# In[ ]:




