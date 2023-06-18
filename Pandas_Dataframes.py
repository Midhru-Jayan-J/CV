#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


mydata=np.random.randint(0,101,(4,3))


# In[4]:


mydata


# In[5]:


myindex=['India','China','NZ','Australia']


# In[6]:


mycoloums=['ageexp','growth','rank']


# In[7]:


df=pd.DataFrame(mydata,myindex,mycoloums)


# In[8]:


df


# In[9]:


df.info()


# In[10]:


pwd


# In[11]:


df=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\03-Core-Pandas\\tips.csv')


# In[12]:


df


# In[13]:


df.columns


# In[14]:


df.index


# In[15]:


df.head()


# In[16]:


df.head(10)


# In[17]:


df.tail()


# In[18]:


df.tail(10)


# In[19]:


df.info()


# In[20]:


df.describe()


# In[21]:


df.describe().transpose()


# In[22]:


df['total_bill']


# In[23]:


mycols=['tip','size']
df[mycols]


# In[25]:


df['tips_percent']=100*df['tip']/df['total_bill']


# In[26]:


df['tips_percent']


# In[27]:


df


# In[28]:


df['price_per_person']=df['total_bill']/df['size']


# In[29]:


df


# In[30]:


df['price_per_person']=np.round(df['total_bill']/df['size'],2)


# In[31]:


df


# In[34]:


df.drop('tips_percent',axis=1)


# In[35]:


df


# In[36]:


df=df.drop('tips_percent',axis=1)


# In[37]:


df


# In[39]:


df=df.set_index('Payment ID')


# In[40]:


df


# In[47]:


df=df.reset_index()


# In[48]:


df


# In[49]:


df=df.set_index('Payment ID')


# In[50]:


df


# In[52]:


df.iloc[0]


# In[53]:


df.loc['Sun2959']


# In[54]:


df.iloc[0:4]


# In[56]:


df.loc[['Sun2959','Sun5260']]


# In[57]:


df.drop('Sun2959')


# In[58]:


df=pd.read_csv('D:\\Python for Finance\\Python-Finance-QuantConnect\\03-Core-Pandas\\tips.csv')


# In[59]:


df


# In[66]:


df[df['total_bill']>45]


# In[64]:





# In[68]:


df[df['sex']=='Male']


# In[75]:


df[(df['total_bill']>40) | (df['sex']!='Male')]


# In[76]:


options=['Sat','Sun']


# In[78]:


df[df['day'].isin(options)]


# In[ ]:




