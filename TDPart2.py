#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def find(df,column,what,view=[], groupby="", sort=""):
    """
        trouve une valeur dans le tableau en fonction de la colonne
        
        groupby : mean, sum, first, last, size
        sort : ascending, descending
    """
    tmp = df[df[column].isin(what)]
    
    if groupby=="mean":
        tmp = tmp.groupby([column]).mean()
    elif groupby=="sum":
        tmp = tmp.groupby([column]).sum()
    elif  groupby=="first":
        tmp = tmp.groupby([column]).first()
    elif  groupby=="last":
        tmp = tmp.groupby([column]).last()
    elif  groupby=="size":
        tmp = tmp.groupby([column]).size()
        if view != []:
            print('\033[93m' + "GROUPBY Warn:"+ '\033[95m' +" pas de VIEW disponible avec l'option size")
            view = []
    
    if sort != "" and groupby != "":
        print('\033[93m' + "SORT Warn:"+ '\033[95m' +" inutile de trier les objets groupé")
        sort=""
    
    if sort=="ascending":
        tmp = tmp.sort_values(by=column, ascending=True)
    elif sort=="descending":
        tmp = tmp.sort_values(by=column, ascending=False)
            
    if view != [] :
       return tmp.loc[:,view]
    return tmp


# In[3]:


def rangeValue(df,column,plage,view=[], groupby="first"):
    """
        regroupe les valeur celon une plage
        
        groupby : mean, sum, first, last, size 
            default -> first
    """
    tmp = df.groupby(pd.cut(csv[column], plage))
    
    if groupby=="mean":
        tmp = tmp.mean()
    elif groupby=="sum":
        tmp = tmp.sum()
    elif  groupby=="first":
        tmp = tmp.first()
    elif  groupby=="last":
        tmp = tmp.last()
    elif  groupby=="size":
        tmp = tmp.size()
        if view != []:
            print('\033[93m' + "GROUPBY Warn:"+ '\033[95m' +" pas de View disponible avec l'option size")
            view = []
            
    if view != [] :
       return tmp.loc[:,view]
    return tmp


# In[7]:


list(range(0,5))


# In[58]:


def changeValue(df, columns, origin, new, condition=[]):
    """
    change la ou les valeurs donnée dans origin par new dans le tableau 
    
    condition (str, object): assigne la valeur new si la condition est respecteer sinon elle garde la valeurs de  base
        origin ne sera pas pris en compte, il peut etre initialisé a ""
    condition ("around", int) : aroundi la valeur selon les colonnes selectionné, int correspond du nombre de chiffre apres la virgule
    """
    for i in range(len(columns)):
        if condition != () and len(condition) == 2:
            mode, form = condition
            if mode == ">":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x > form else x)
            elif mode == "<":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x < form else x)
            elif mode == "!=":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x != form else x)
            elif mode == "==":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x == form else x)
            elif mode == "<=":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x <= form else x)
            elif mode == ">=":
                df[columns[i]] = df[columns[i]].apply(lambda x: new if x >= form else x)
            elif mode == "around":
                df[columns[i]] = df[columns[i]].apply(lambda x: round(x, form) if type(x) is float else x)
        else:
            df[columns[i]] = df[columns[i]].apply(lambda x: new if x == origin else x)
                


# In[56]:


csv = pd.read_csv('mower_market_snapshot.csv',delimiter=";")


# In[10]:


find(csv,"warranty", ["3ans", "2ans"], view=["id"], groupby="size", sort="ascending")


# In[11]:


rangeValue(csv, "price", [0, 200,300,600,float("inf")], groupby="mean")


# In[28]:


find(csv, "product_type", ["electric", "electrique"], groupby="size")


# In[29]:


changeValue(csv, ["product_type"], "electrique", "electric")
find(csv, "product_type", ["electric", "electrique"], groupby="size")


# In[57]:


changeValue(csv, ["price"], "", "", condition=("around", 2))
csv.head()


# In[ ]:




