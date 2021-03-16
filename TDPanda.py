#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


# In[22]:


import numpy as np


# In[2]:


csv = pd.read_csv('mower_market_snapshot.csv',delimiter=";")


# In[3]:


csv.head()


# In[28]:


csv["prod_cost"]


# In[26]:


csv[csv["prod_cost"].isin(["unknown"])]


# In[32]:


csv.groupby(["warranty"]).first()


# In[49]:


csv["warranty"] = csv["warranty"].apply(lambda x: x[0])


# In[51]:


csv.groupby(["warranty"]).first()


# In[ ]:




