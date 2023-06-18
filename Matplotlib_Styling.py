#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy  as np 
import matplotlib.pyplot as plt


# In[2]:


x=np.linspace(0,11,10)


# In[15]:


image=plt.figure()
ax=image.add_axes([0,0,1,1])
ax.plot(x,x,label='X vs X')
ax.plot(x,x**2,label='X vs X^2')
ax.legend(loc=2)


# In[16]:


image=plt.figure()
ax=image.add_axes([0,0,1,1])
ax.plot(x,x,label='X vs X')
ax.plot(x,x**2,label='X vs X^2')
ax.legend(loc=(1.1,))


# ax=image.add_axes([0,0,1,1])
# line1=ax.plot(x,x**2,color='#69f58e',label='X vs X**2',linewidth=4)
# line2=ax.plot(x,x+7,color='#f272c7',label='X vs X+7',linewidth=1.5)
# line1.set_dashes([5,2,15,5])
# plt.legend()

# In[40]:


ax=image.add_axes([0,0,1,1])
ax.plot(x,x**2,color='#69f58e',label='X vs X**2',linewidth=4,linestyle='--',marker='o',markersize=5)
ax.plot(x,x+7,color='#f272c7',label='X vs X+7',linewidth=1.5,linestyle='-.')
plt.legend()


# In[ ]:




