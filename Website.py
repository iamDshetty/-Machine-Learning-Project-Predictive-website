#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.impute import  SimpleImputer
imp = SimpleImputer(strategy='mean',missing_values=np.nan)


csv_path ='C:/Users/lenovo/Predictive Website/Stack Over Flow developer_survey_2019/survey_results_public.csv'

df = pd.read_csv(csv_path)


# In[7]:


class data_set():
    
    def __init__ (self):
        #self.link = link
        #self.df = pd.read_csv(link)  
        self.cols = df.columns
        pass
    
    #def _1vs1 (self,a,b,filt_col,filt_val):
        
        #filt = df[filt_col]==filt_val
        #fig,ax = plt.subplots()
        #ax.scatter(df.loc[filt,a],df.loc[filt,b],label=f'{a} v/s {b}')
        #ax.legend()
        #ax.set(xlabel = a,ylabel=b)
        #pass
    
    def analysis(self,filt_col,filt_val,y,*args):  
        filt = df[filt_col]==filt_val
        for x in args:
            fig,ax1 = plt.subplots()
        
            ax1.scatter(df.loc[filt,x],df.loc[filt,y],label=f'{x} v/s {y}')
            ax1.legend()
            ax1.set(xlabel = x,ylabel=y)
            pass
        pass
    pass


    

