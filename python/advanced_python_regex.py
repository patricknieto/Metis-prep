# coding: utf-8

# In[26]:

import pandas as pd
from collections import defaultdict


# In[36]:

#before reading in the data, we need to make sure there are no whitespaces
#leading or trailing the text. 

#Coverters: Dict of functions for converting values in certain columns. Keys can 
#either be integers or column labels 


def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text
    
def stripReplace(text):
    try:
        return text.strip().replace('.','').replace('0', 'none')
    except AttributeError:
        return text    

data = pd.read_csv('faculty.csv', sep =',',
                    names = ["name", "degree", "title", "email"],
                    header = 0,
                    converters = {'name' : strip,
                                  'degree' : stripReplace,
                                  'title' : strip,
                                  'email' : strip})
data.head()


# In[37]:

degrees = list(data.degree)
Alldegrees = []
for item in degrees:
    Alldegrees.extend(item.split())
    
degree_count = defaultdict(int)
for degree in Alldegrees:
    degree_count[degree] += 1
    
degree_count


# In[38]:

freqs = pd.DataFrame.from_dict(degree_count, orient='index')
freqs


# In[ ]:



