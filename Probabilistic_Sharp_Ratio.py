#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


aapl=pd.read_csv('D:\Python for Finance\\Python-Finance-QuantConnect\\06-Financial-Concepts-with-Python\\apple.csv',index_col='Date',parse_dates=True)


# In[30]:


wal=pd.read_csv('D:\Python for Finance\\Python-Finance-QuantConnect\\06-Financial-Concepts-with-Python\\WMT.csv',index_col='Date',parse_dates=True)
aapl['Daily Return']=aapl['Adj Close'].pct_change(1)
wal['Daily Return']=wal['Adj Close'].pct_change(1)
aapl=aapl.dropna()
wal=wal.dropna()


# In[31]:


def compute_sharp_ratio(df,risk_free_rate=0):
                        mean_return=df['Daily Return'].mean()
                        std=df['Daily Return'].std()
                        sharp_ratio=(mean_return-risk_free_rate)/std
                        return sharp_ratio
#This is for daily sharp ratio


# In[32]:


import scipy.stats


# In[51]:


def compute_psr(df,benchmark=0):
    sr=compute_sharp_ratio(df)
    skew=scipy.stats.skew(df['Daily Return'])
    kurtosis=scipy.stats.kurtosis(df['Daily Return'],fisher=True)
    n=len(df)
    sigma_sr=( (1/(n-1)) * (1 + 0.5*sr**2 - skew*sr+ (kurtosis/4)*sr**2 ))**0.5
    ratio=(sr-benchmark)/sigma_sr
    psr=scipy.stats.norm.cdf(ratio)
    return psr


# In[37]:


aapl_sr=compute_sharp_ratio(aapl)


# In[38]:


aapl_sr


# In[52]:


aapl_psr=compute_psr(aapl)


# In[53]:


aapl_psr


# In[54]:


wal_sr=compute_sharp_ratio(wal)


# In[55]:


wal_sr


# In[56]:


wal_psr=compute_psr(wal)


# In[57]:


wal_psr


# In[49]:


wal


# In[ ]:




