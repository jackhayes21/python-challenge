#!/usr/bin/env python
# coding: utf-8

# # Python-Challenge

# In[98]:


import csv


# In[99]:


import pandas as pd


# In[100]:


import os


# In[101]:


csvpath = os.path.join("/Users/PrincessAimee/Downloads/budget_data.csv")
csvoutput = os.path.join("output.txt")


# In[102]:


# Variables 
total_months = 0
net_total_amount = 0
average_change = 0
net_change_list = []
months = []


# In[103]:


greatest_increase = ["", -1000]
greatest_decrease = ["",999999]


# In[123]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)
#     print(csv_headers)
#     print(next(csvreader))
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    total_months += 1
    first_row = next(csvreader)
    prev = int(first_row[1])
    net_total_amount += int(first_row[1])
    for x in csvreader:
        months.append(x[0])
        total_months += 1
        net_total_amount += int(x[1])
        net_change = int(x[1]) - prev
        net_change_list.append(net_change)
        prev = int(x[1])
        if net_change > greatest_increase[1]:
            greatest_increase[0]=x[0]
            greatest_increase[1]=net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=x[0]
            greatest_decrease[1]=net_change
    average_change = sum(net_change_list) / len(net_change_list)
    print("Financial Analysis")
    print(f"-"*20)
    print(f"total number of months is : {total_months}")
    print(f"net total amount is : ${net_total_amount}")
    print(f"average change is {str(average_change)}")
    print(f"greatest increase in profit : {greatest_increase[0]} {greatest_increase[1]}")
    print(f"greates decrease in profit : {greatest_decrease[0]} {greatest_decrease[1]}")
#     print(f"greatest increase in profit : {months[net_change_list.index(max(net_change_list))]} {max(net_change_list)}")
#     print(f"greates decrease in profit : {months[net_change_list.index(min(net_change_list))]} {min(net_change_list)}")
