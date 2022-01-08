#!/usr/bin/env python
# coding: utf-8

# In[59]:


pip install bsedata


# In[42]:


pip install pandasql


# In[60]:


pip install nsepy


# In[61]:


pip install quandl


# In[62]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import os
from pandasql import *
from IPython.display import clear_output


# In[63]:


#LIBRARIES
from nsepy import get_history
from datetime import date,timedelta,datetime
import quandl
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# import numpy as np


# In[64]:


from bsedata.bse import BSE


# In[65]:


# os. chdir(r'C:\karanDirectories\Fundamental_analysis\twenty_pct_tradingStr')


# In[66]:


master_data=pd.read_csv('equity.csv')


# In[67]:


master_data.head()


# In[68]:


# #####LAST ONE MONTH DIFFERENCE####
# quandl.ApiConfig.api_key = 'bpiTuJQDVqfgdZeX_tVu'
# old_day=date.today()-timedelta(30)
# if(old_day.weekday()==5):
#     old_day=date.today()-timedelta(31)
# elif(old_day.weekday()==6):
#     old_day=date.today()-timedelta(29)
# else:
#     old_day=old_day
# historical_price=pd.DataFrame(columns=['code','name','close_price'])

# for i in range(len(master_data)):
#     code='BSE/BOM'+str(master_data['Security Code'][i])
#     print(code)
#     print(i)
#     df=quandl.get(code, start_date=old_day, end_date=old_day)
#     cd=master_data['Security Code'][i]
#     name=master_data['Security Name'][i]
#     close_price=df['Close'][0]
#     print(close_price)
#     data={'code':cd,'name':name,'close_price':close_price}
#     historical_price=historical_price.append(data,ignore_index=True)
    


# In[69]:


#####LAST ONE WEEK DIFFERENCE####
quandl.ApiConfig.api_key = 'bpiTuJQDVqfgdZeX_tVu'
old_day=date.today()-timedelta(7)
if(old_day.weekday()==5):
    old_day=date.today()-timedelta(8)
elif(old_day.weekday()==6):
    old_day=date.today()-timedelta(6)
else:
    old_day=old_day
historical_price=pd.DataFrame(columns=['code','name','close_price'])

for i in range(len(master_data)):
    code='BSE/BOM'+str(master_data['Security Code'][i])
    print(code)
    print(i)
    df=quandl.get(code, start_date=old_day, end_date=old_day)
    cd=master_data['Security Code'][i]
    name=master_data['Security Name'][i]
    close_price=df['Close'][0]
    print(close_price)
    data={'code':cd,'name':name,'close_price':close_price}
    historical_price=historical_price.append(data,ignore_index=True)
    


# In[70]:


historical_price


# In[71]:


b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)


# In[72]:

log=pd.DataFrame(columns=['timestamp','code''name','old_price','current_price','drop_pct','grow_pct'])
clear_output(wait=True)
print('Running Again')
for i in range(10):
    code=master_data['Security Code'][i]
    q=b.getQuote(str(code))
    current=float(q['currentValue'])
    old=float(historical_price[historical_price['code']==int(code)]['close_price'])
    drop_pct=((old-current)/old)*100
    grow_pct=((current-old)/old)*100
    if(grow_pct>=5):
        data={'timestamp':q['updatedOn'],'code': q['scripCode'],'name':q['securityID'],'old_price':old,'current_price':current,'drop_pct':drop_pct,'grow_pct':grow_pct}
        log=log.append(data,ignore_index=True)
if(len(log)==0):   
    clear_output(wait=True)
    print('No Records')
else:
    clear_output(wait=True)
    print(log)
       

