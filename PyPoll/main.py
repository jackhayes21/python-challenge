#!/usr/bin/env python
# coding: utf-8

# In[67]:


import csv


# In[68]:


import pandas as pd


# In[69]:


import os


# In[90]:


csvpath = os.path.join("/Users/PrincessAimee/Downloads/election_data.csv")
csvoutput = os.path.join("output.txt")


# In[89]:


#Variables 
total_number_of_votes = 0
complete_list_of_candidates =[]
vote_count = {}
individual_votes = []


# In[91]:


csvpath = os.path.join('/Users/PrincessAimee/Downloads/election_data.csv')
# csvoutput = os.path.join('output.txt')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader) # exhausting the first row will leave me with the rest of the data
    for x in csvreader:
        # print(x)
        # ["123455", "Jeffeson", "Charles Casper ...."]
        # ["987654", "Jeffeson", "Charles Casper ...."]
        total_number_of_votes += 1
        name = x[2]
        if name not in complete_list_of_candidates:
            complete_list_of_candidates.append(name)
            vote_count[name] = 1
        else: # if the candidate already exist, just increment the value for the name by 1
            vote_count[name] += 1
    for k, v in vote_count.items():
        print(f"Percentage for {k} is %{round(v/total_number_of_votes*100,2)}")
    for k, v in vote_count.items():
        print(f"Total Number of Votes Each Candidate Won is: Name {k} and # of Votes {v}")
    max_votes = 0
    name = ""
    for k,v in vote_count.items():
        if max_votes < v: # 0 < 85213 , 85213 < 272892
            max_votes = v
            name = k
        else:
            continue
    print(f"name {name} and popular vote {max_votes}")


# In[ ]:

