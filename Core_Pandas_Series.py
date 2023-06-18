#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


import pandas as pd


# In[4]:


help(pd.Series)


# In[5]:


myindex=['India','China','Japan']


# In[6]:


mydata=[77,65,54]


# In[11]:


myset=pd.Series(mydata,myindex)


# In[12]:


myset


# In[14]:


ages={'Sam':7,'Ananya':12,'Veer':9}


# In[15]:


pd.Series(ages)


# In[19]:


q1={'Japan':80,'China':450,'India':200,'USA':250}
q2={'Brazil':100,'China':500,'India':210,'USA':260}


# In[20]:


sales_q1=pd.Series(q1)


# In[21]:


sales_q2=pd.Series(q2)


# In[22]:


sales_q1


# In[23]:


sales_q2


# In[9]:


[1,2]*2


# In[24]:


np.array([1,2])*2


# In[25]:


sales_q1*2


# In[26]:


sales_q1.add(sales_q2,fill_value=0)


# In[27]:


sales_q1+sales_q2


# In[16]:


sales_q1*sales_q2-


# In[18]:


sales_q1.mul(sales_q2,fill_value=0)


# In[ ]:




