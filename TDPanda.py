#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


csv = pd.read_csv('mower_market_snapshot.csv',delimiter=";")


# In[4]:


csv.head()


# In[5]:


csv["prod_cost"]


# In[6]:


csv[csv["prod_cost"].isin(["unknown"])]


# In[12]:


csv.isnull().sum()


# In[32]:


csv.groupby(["warranty", "quality"]).first()


# In[9]:


csv["warranty"] = csv["warranty"].apply(lambda x: x[0])


# In[10]:


csv.groupby(["warranty"]).first()


# In[34]:


csv.groupby(pd.cut(csv["price"], [0, 300,500,float("inf")])).mean().loc[:,["capacity", "failure_rate", "margin","market_share", "attractiveness"]]


# In[23]:


csv["product_type"] = csv["product_type"].apply(lambda x: 1 if x=="essence" else 2 if x=="electrique" else 3)


# In[25]:


csv.groupby(["product_type"]).first()


# In[30]:


csv = csv.assign(Essence=csv["product_type"].apply(lambda x: 1 if x==1else 0), Electrique=csv["product_type"].apply(lambda x: 1 if x==2 else 0), Auto_portee=csv["product_type"].apply(lambda x: 1 if x==3 else 0))
csv.groupby(["product_type"]).first()


# In[ ]:




