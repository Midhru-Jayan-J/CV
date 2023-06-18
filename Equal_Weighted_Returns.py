#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# In[2]:


COST=pd.read_csv('D:\Python for Finance\Python-Finance-QuantConnect\DATA\COST.csv',index_col='Date',parse_dates=True)['Adj Close']


# In[3]:


COST


# In[4]:


WMT=pd.read_csv('D:\Python for Finance\Python-Finance-QuantConnect\DATA\WMT.csv',index_col='Date',parse_dates=True)['Adj Close']


# In[5]:


TGT=pd.read_csv('D:\Python for Finance\Python-Finance-QuantConnect\DATA\TGT.csv',index_col='Date',parse_dates=True)['Adj Close']


# In[6]:


WMT


# In[7]:


TGT


# In[8]:


DG=pd.read_csv('D:\Python for Finance\Python-Finance-QuantConnect\DATA\DG.csv',index_col='Date',parse_dates=True)['Adj Close']


# In[9]:


COST.plot()


# In[10]:


retail=pd.concat([COST,WMT,TGT,DG],axis=1)
retail.columns=['COST','WMT','TGT','DG']


# In[11]:


retail


# In[17]:


retail_return=retail.pct_change(1).dropna()


# In[18]:


retail_return.plot(figsize=(12,3))


# In[19]:


retail_return['COST'].plot(kind='hist',bins=100)


# In[20]:


retail['COST'].plot()


# In[ ]:





# In[25]:


cumul_return=(1+retail_return['COST']).cumprod()-1


# 

# In[26]:


cumul_perc_return=100*cumul_return


# In[29]:


cumul_perc_return.plot()


# In[31]:


np.dot([2,3],[10,20])


# In[32]:


example_return=np.array([1,0.5]) # 100% 50%


# In[36]:


weights=[0.5,0.5] #Cash Go? [100%,0%]


# In[37]:


np.dot(weights,example_return)


# In[39]:


np.dot([1,0,0,0],retail_return.transpose())


# In[40]:


retail_return['COST']


# In[41]:


np.dot([0.5,0,0.25,0.25],retail_return.transpose())


# In[43]:


N=len(retail_return.columns)


# In[44]:


N


# In[45]:


equal_weights=N*[1/N]


# In[46]:


equal_weights


# In[48]:


equal_returns=np.dot(equal_weights,retail_return.transpose())


# In[ ]:





# In[50]:


equal_returns


# In[53]:


cum_equal_weighted_returns=(1+equal_returns).cumprod()-1


# In[56]:


cum_equal_weighted_return_perc=100*cum_equal_weighted_returns


# In[58]:


cewrp=pd.Series(cum_equal_weighted_return_perc,index=retail_return.index)


# In[62]:


plt.figure(figsize=(10,3),dpi=200)
cewrp.plot(label='Equal Weighted Portfolio(CUMUL RETURNS)')
cumul_perc_return.plot(label='COST CUMUL RETURNS')
plt.legend()


# In[ ]:




