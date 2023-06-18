#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


aapl=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\DATA\\AAPL.csv',index_col='Date',parse_dates=True)


# In[3]:


tesla=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\DATA\\TSLA.csv',index_col='Date',parse_dates=True)


# In[4]:


aapl


# In[5]:


tesla


# In[6]:


aapl.info()


# In[7]:


tesla.info()


# In[8]:


aapl['Daily Return']=aapl['Adj Close'].pct_change(1)


# In[9]:


tesla['Daily Return']=tesla['Adj Close'].pct_change(1)


# In[10]:


aapl=aapl.dropna()


# In[11]:


tesla


# In[12]:


tesla=tesla.dropna()


# In[13]:


tesla


# In[14]:


aapl['Daily Return'].std()


# In[23]:


tesla['Daily Return'].std()


# In[ ]:





# In[27]:


def compute_sharp_ratio(df,risk_free_rate=0):
                        mean_return=df['Daily Return'].mean()
                        std=df['Daily Return'].std()
                        sharp_ratio=(mean_return-risk_free_rate)/std
                        return sharp_ratio
#This is for daily sharp ratio


# compute_sharp_ratio(aapl)

# In[28]:


compute_sharp_ratio(aapl)


# In[29]:


compute_sharp_ratio(tesla)


# In[30]:


def compute_sharp_ratio(df,risk_free_rate=0):
                        mean_return=df['Daily Return'].mean()
                        std=df['Daily Return'].std()
                        sharp_ratio=(mean_return-risk_free_rate)/std
                        return sharp_ratio*(252**0.5)
#This is for annual sharp ratio


# In[41]:


sr_aapl=compute_sharp_ratio(aapl)


# In[42]:


sr_tesla=compute_sharp_ratio(tesla)


# In[43]:


sr_aapl

sr_tesla
# In[44]:


sr_tesla


# In[46]:


aapl['Adj Close'].plot()


# In[47]:


tesla['Adj Close'].plot()


# In[ ]:




