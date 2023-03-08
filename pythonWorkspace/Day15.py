#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.set_printoptions(precision=5, suppress=True)

# in[5]:

if __name__ == '__main__':
	print('direct call')
else:
	print('imported')


# In[15]:


def read_data():
    d_data = []
    with open('가스공급량_20230217170919.csv') as f:
        for i in f:
            d_data.append(i[:-1].split(','))
    np_data = np.array(d_data[2:])
    np_data = np_data[:,2:].astype(np.int64)
    return np_data

def get_corr(np_data):
    by_year = np.add.reduceat(np_data,np.arange(10,130,12))
    return np.corrcoef(by_year[0:1], by_year[0:3])


# In[20]:


d = read_data()
out = get_corr(d)
print(out)

