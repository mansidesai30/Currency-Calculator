#!/usr/bin/env python
# coding: utf-8

# In[89]:


# loading the packages
# requests provides us with the capabilities of sending an HTTP request to a server
import requests
import json # A useful library for JSON manipulation and pretty print


# In[90]:


# Define the web URL
# web URL: the part of the URL common to all requests, not containing the parameters
web_url = "https://api.exchangeratesapi.io/latest"


# In[91]:


# We can make a GET request to this web url for API endpoint with requests.get
response = requests.get(web_url)

# This method returns the response from the server
# We store this response in a variable for future data processing


# In[92]:


# Checking if the request went through ok whether it is true or false i.e true = Success False = Not Success
response.ok
# Checking the status code of the response i.e 200 = Success or 400 = Error
response.status_code


# In[93]:


# Printing the content body of the response in regular format
response.text
# printing the content of the response in bytes format
response.content
# Requests has in-build method to directly convert the response to JSON format
response.json()


# In[94]:


#.dumps() has options to make the string more readable
# We can choose the number of spaces to be used as indentation
# In order to visualize these changes, we need to print the string
print(json.dumps(response.json(), indent=4))


# In[95]:


print(json.dumps(response.json(), indent=4))


# In[98]:


response.json().keys()


# In[99]:


# Request parameters are added to the URL after a question mark '?'
# In this case, we request for the exchange rates of the US Dollar (USD) and indian Rupees only
param_url = web_url + "?symbols=USD&base=INR"
param_url


# In[100]:


# Making a request to the server with the new URL, containing the parameters
response = requests.get(param_url)
response.status_code


# In[101]:


# Saving the response data
data = response.json()
data


# In[102]:


# 'data' is a dictionary
data['base']


# In[103]:


data['date']


# In[82]:


data['rates']


# In[104]:


param_url = web_url + "?symbols=GBP&base=USD"


# In[105]:


data = requests.get(param_url).json()
data


# In[106]:


# Pretty printing the data
data = response.json()
print(json.dumps(data, indent=4))


# In[107]:


web_url = "https://api.exchangeratesapi.io"


# In[108]:


# Pretty printing the data
data = response.json()
print(json.dumps(data, indent=4))


# In[114]:


# CURRENCY CALCULATOR
date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input("How much {} do you want to convert: ".format(base)))

# Constructing the URL based on the user parameters and sending a request to the server
url = web_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url)

# Displaying the error message, if something went wrong
if(response.ok is False):
    print("\nError {}:".format(response.status_code))
    print(response.json()['error'])

else:
    data = response.json()
    rate = data['rates'][curr]
    
    result = quan*rate
    
    print("\n{0} {1} is equal to {2} {3}, based upon exchange rates on {4}".format(quan,base,result,curr,data['date']))


# In[ ]:




