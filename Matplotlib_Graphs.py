#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[3]:


x=np.arange(0,10)


# In[4]:


y=2*x


# In[5]:


plt.plot(x,y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xlim(0,10)
plt.ylim(0,22)
plt.title('Chart')
plt.show()
plt.savefig('D:\\Python for Finance\\Firstplot.png')


# In[6]:


fig=plt.figure()
axes=fig.add_axes([5,5,1,1])
axes.plot(x,y)


# In[7]:


a=np.linspace(0,10,11)


# In[8]:


b=a**4


# In[9]:


x=np.arange(0,10)


# In[10]:


y=2*x


# In[11]:


a


# In[12]:


b


# In[13]:


x


# In[14]:


y


# In[30]:


fig=plt.figure()
axes1=fig.add_axes([0,0,1,1])
axes1.plot(a,b)
axes1.set_xlim(0,10)
axes1.set_ylim(0,10000)
axes2.set_title('power of 4')


axes2=fig.add_axes([0.2,0.5,0.25,0.25])
axes2.plot(x,y)
axes2.set_xlim(0,12)
axes2.set_ylim(0,20)
axes2.set_title('multiples of 2')
plt.show()


# In[41]:


fig=plt.figure(dpi=200,figsize=(10,2))
axes1=fig.add_axes([0,0,1,1])
axes1.plot(a,b)
fig.savefig('D:\\Python for Finance\\first figsize.jpg',bbox_inches='tight')
    


# In[61]:


fig,s=plt.subplots(nrows=2,ncols=2)
s[0,0].plot(a,b)
s[0,1].plot(x,y)
s[1,0].plot(a,b)
s[1,1].plot(x,y)
plt.tight_layout


# In[53]:





# In[52]:


s.shape


# In[72]:


fig,s=plt.subplots(nrows=2,ncols=2,figsize=(10,5))
s[0,0].plot(a,b)
s[0,1].plot(x,y)
s[1,0].plot(a,b)
s[1,1].plot(x,y)
fig.subplots_adjust(wspace=0.9,hspace=0.5)
fig.suptitle('title')
fig.savefig('D:\\Python for Finance\\first subplot.pdf',bbox_inches='tight')


# In[ ]:




