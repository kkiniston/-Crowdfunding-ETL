#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# ## Deliverable 1: Extract
# ----
# ### Option 1: Use Python Dictionary Methods
# 
# 1. Import the `backer_info.csv` file into a DataFrame.
# 2. Iterate through the DataFrame and convert each row to a dictionary. 
# 3. Iterate through each dictionary and do the following:
#     * Extract the dictionary values from the keys using Python list comprehension.
#     * Add the values for each row to a new list. 
# 4. Create a new DataFrame with the retrieved data. 
# 5. Export the DataFrame as `backers_data.csv`.

# In[2]:


# Get the backers_info from the crowdfunding_info sheet. 
pd.set_option('max_colwidth', 400)
df = pd.read_csv("backer_info.csv")
backer_data.head (10)


# In[1]:


# Iterate through the backers DataFrame and convert each row to a dictionary.
backer_value = []
    # Iterate through each dictionary (row) and get the values for each row using list comprehension.
    for i, row in backer_data.iterrows()
    data = row ['backer info']
    row_values = [ v for k, v in converted_data.items()]
    # Append the list of values for each row to a list. 
    dict_values.append(row_value)

# Print out the list of values for each row.
print(backer_value)


# In[4]:


# Create a backers_df DataFrame with the following columns: 'backer_id','cf_id', 'name', and 'email' 
# using the list of values lists. 

backers_df = pd.DataFrame(backer_value, columns =['backer_id', 'cf_id', 'name', 'email'])
backers_df.head(10)


# In[5]:


# Export the DataFrame as a CSV file using encoding='utf8'.

backers_df.to_vsc('backer_info.csv', index=False, encoding= 'utf8')


# ## Deliverable 1: Extract
# ----
# ### Option 2: Use regex 
# 
# 1. Import the `backer_info.csv` file into a DataFrame. 
# 2. Extract the "backer_id", "cf_id", "name", and "email using regular expressions."
# 3. Create a new DataFrame with the retrieved data.
# 4. Export the DataFrame as `backers_data.csv`.

# In[6]:


# Get the backers_info from the crowdfunding_info sheet. 
pd.set_option('max_colwidth', 400)


# In[7]:


# Extract the alpha-numeric "backer_id" from the backer_info column using a regex expression 
# and add it as a new column called "backer_id".


# In[8]:


# Extract the two to four-digit "cf_id" number from the backer_info column. 
# and add it as a new column called "cf_id".


# In[9]:


# Extract the name from the backer_info column and add it as a new column called "name".


# In[10]:


# Extract the email from the backer_info column and add it as a new column called "email".


# In[11]:


# Create a new DataFrame with the appropriate columns.


# In[12]:


# Export the DataFrame as a CSV file using encoding='utf8'.


# ## Deliverable 2: Transform and Clean Data
# ----
# 1. Check the data types of the columns and convert the "cf_id" column to an integer, if necessary.
# 2. Split the name in the "name" column into first and last names, and add them to "first_name" and "last_name" columns in the DataFrame. 
# 3. Drop the "name" column in the DataFrame.
# 4. Place the columns in the following order; "backer_id", "cf_id", "first_name", "last_name" and "email".

# In[13]:


# Check data types.

backers_df.info()


# In[14]:


# Convert cf_id to an integer if necessary.
#NA int64 


# In[15]:


# Split the "name" column into "first_name" and "last_name" columns.

backers_df[['first_name', 'last_name']] = backers_df["name"].str.split('', n=1, expand=True)
backers_df.head(10)


# In[16]:


#  Drop the name column
backers_df = backers_df.drop(columns=['name'])

# Reorder the columns
backer_df = backer_df[['backer_id', 'cf_id', 'first_name', 'last_name', 'email']]
backer_df.head(10)


# In[17]:


# Export the DataFrame as a CSV file using encoding='utf8'.

backer_df.to_csv('backers.csv', index=False, encoding='utf8')


# In[ ]:




