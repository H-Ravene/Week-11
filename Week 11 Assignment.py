#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In this jupyter notebook we will be choosing one of the New York Times APIs, constructing an interface in Python to read in the JSON data, and transforming it into a pandas DataFrame.
import pandas as pd
import json
import urllib.request
from pandas.io.json import json_normalize
#We will be using the Most Viewed Opinion articles in the last 30 days from the Most Popular API and transforming it into a pandas DataFrame.
api_key = '089beac3eb674ecfb1a42ecb5cb7358c'
url = 'https://api.nytimes.com/svc/mostpopular/v2/mostviewed/Opinion/30.json?limit=100'
string = url+'&api-key='+api_key

response = str(urllib.request.urlopen(string).read(), 'utf-8')

df = pd.read_json(response)
df
data = json.loads(response)
most_viewed = json_normalize(data['results'])
most_viewed


# In[ ]:




