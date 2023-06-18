#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\DATA\\FB.csv')


# In[3]:


df


# In[4]:


df.plot()


# In[5]:


df[['Open','Close']].plot(kind='bar')


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


plt.figure(dpi=300)
df['Volume'].plot(kind='line',c='red',figsize=(7,10))


# In[8]:


df['Volume'].plot(kind='kde')


# In[9]:


new_df=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\DATA\\TGT.csv')


# In[10]:


new_df


# In[11]:


new_df['Open'].plot(label='TGT')
df[['Open','Low']].plot(label='FB')
plt.legend(loc=(0.5,1.005))


# In[12]:


f=new_df['Open'].plot(label='TGT')
df[['Open','Low']].plot(ax=f)
plt.legend(loc=(0.5,1.005))


# In[20]:


cost1=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\DATA\\COST.csv',index_col='Date',parse_dates=True)


# In[25]:


cost1


# In[26]:


cost1.index


# In[28]:


cost1.plot()


# In[29]:


cost1['Open'].plot()


# In[32]:


cost1['Open']['2019-01-01':'2021-12-31'].plot()


# In[44]:


cost1['Close'].plot()
from matplotlib import dates
    


# In[49]:


f=plt.figure(dpi=150)
line=cost1['Close']['2019-04-14':'2021-03-06'].plot()
line.xaxis.set_major_locator(dates.MonthLocator())


# In[53]:


f=plt.figure(dpi=150)
line=cost1['Close']['2019-04-14':'2021-03-06'].plot()
line.xaxis.set_major_locator(dates.MonthLocator(7))
line.xaxis.set_major_formatter(dates.DateFormatter('%Y-%B'))


# In[54]:


cost1.plot()


# In[85]:


m=plt.figure(figsize=(50,10),dpi=175)
m2=cost1['Volume']['2018-01-10':'2020-12-31'].plot()
m2.xaxis.set_major_locator(dates.YearLocator())
m2.xaxis.set_major_formatter(dates.DateFormatter('%Y'))
m2.xaxis.set_minor_locator(dates.MonthLocator())
m2.xaxis.set_minor_formatter(dates.DateFormatter('%b-%y'))
plt.savefig('D:\\Python for Finance\\firstliked graph.pdf',bbox_inches='tight')


# In[98]:


m=plt.figure(figsize=(20,10),dpi=175)
m2=cost1['Volume']['2018-01-10':'2020-12-31'].plot()
m2.xaxis.set_major_locator(dates.YearLocator())
m2.xaxis.set_major_formatter(dates.DateFormatter('%Y  %b'))
m2.xaxis.set_minor_locator(dates.MonthLocator())
m2.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
m2.tick_params(axis='x',which='major',rotation=90)
m2.tick_params(axis='x',which='minor',rotation=90)
plt.xticks(ha='center');
m2.yaxis.grid(True)


# In[ ]:




