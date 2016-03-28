# coding: utf-8

# In[26]:

import pandas as pd
from collections import defaultdict
import csv

#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

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


# Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor


data.title.values[24] = data.title.values[24].replace(' is ', ' of ')
data.title.value_counts()


#Q3. Search for email addresses and put them in a list. Print the list of email addresses.

email_list = list(data.email.values)

#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

new_list = []
domains = []
for item in email_list:
    new_list.append(item.split('@'))
    
for item in new_list:
    domains.append(item[1])

set(domains)


