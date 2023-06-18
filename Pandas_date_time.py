#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime


# In[2]:


myyear=2019
mymonth=8
myday=23
myhour=10
mymin=20
mysec=45



# In[3]:


mydate=datetime(myyear,mymonth,myday)


# In[4]:


mydate


# In[5]:


mydate=datetime(myyear,mymonth,myday,myhour,mymin,mysec)


# In[6]:


mydate


# In[7]:


mydate.year


# In[8]:


myser=pd.Series(['Mar 25, 2019','2018-12-12'])


# In[9]:


myser


# In[10]:


myser[0]


# In[11]:


timeser=pd.to_datetime(myser)


# In[12]:


timeser


# In[13]:


timeser[0].year


# In[14]:


d1='15-7-2018'


# In[15]:


pd.to_datetime(d1)


# In[ ]:





# In[16]:


style_date='12--Dec--13'


# In[21]:


pd.to_datetime(style_date,format='%d--%b--%y')


# In[22]:


custom_date='12th of december 2004'


# In[20]:


pd.to_datetime(custom_date)


# In[24]:


sales=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\05-Pandas-and-Finance\\SPY2000_2021.csv')


# In[ ]:





# In[25]:


sales


# In[26]:


sales['Date']


# In[27]:


type(sales['Date'])


# In[28]:


sales['Date']=pd.to_datetime(sales['Date'])


# In[29]:


sales['Date']


# In[31]:


sales=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\05-Pandas-and-Finance\\SPY2000_2021.csv',parse_dates=[0])


# In[33]:


sales['Date']


# In[34]:


sales=sales.set_index("Date")


# In[35]:


sales


# In[36]:


sales.resample(rule='A')


# In[37]:


sales


# In[ ]:




