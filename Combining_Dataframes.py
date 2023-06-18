#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


data_one={'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']}


# In[4]:


data_two={'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']}


# In[5]:


one=pd.DataFrame(data_one)


# In[6]:


two=pd.DataFrame(data_two)


# In[7]:


one


# In[8]:


two


# In[9]:


pd.concat([one,two],axis=1)


# In[10]:


pd.concat([one,two])


# In[11]:


pd.concat([one,two],axis=0)


# In[12]:


pd.concat([two,one],axis=0)


# In[13]:


registrations=pd.DataFrame({'regid':[1,2,3,4],'name':['Andrew','Bob','Charlie','David']})
logins=pd.DataFrame({'loginid':[1,2,3,4],'name':['Xavier','Andrew','Yelana','Bob']})


# In[14]:


registrations


# In[15]:


pd.merge(registrations,logins,how='inner',on='name')


# In[16]:


pd.merge(left=registrations,right=logins,how='left',on='name')


# In[17]:


pd.merge(left=registrations,right=logins,how='right',on='name')


# In[18]:


pd.merge(registrations,logins,how='outer',on='name')


# In[19]:


registrations=registrations.set_index('name')


# In[20]:


registrations


# In[21]:


logins


# In[22]:


pd.merge(registrations,logins,left_index=True,right_on='name',how='inner')


# In[23]:


registrations.columns=['regid','reg_name']


# In[ ]:


registrations


# In[ ]:


pd.merge(left=registrations,right=logins,left_on='reg_name',right_on='name',how='outer')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




