#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Open the file that contains the allow list
file_path = "allow_list.txt"

# Read the file contents
with open(file_path, "r") as file:
    allow_list_content = file.read()

# Convert the string into a list
allow_list = allow_list_content.split()

# List of IP addresses to be removed
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Iterate through the remove list
for ip_address in remove_list:
    # Remove IP addresses that are on the remove list
    if ip_address in allow_list:
        allow_list.remove(ip_address)

# Update the file with the revised list of IP addresses
updated_allow_list = " ".join(allow_list)

with open(file_path, "w") as file:
    file.write(updated_allow_list)

# Summary: File has been updated with the removed IP addresses
print("File has been updated with the removed IP addresses.")







## Summary:

##This algorithm provides a systematic approach to updating a file that manages IP addresses for restricted content access
##By checking and removing IP addresses from the allow list based on the remove list,
##it ensures that the file remains up-to-date with the current access permissions.
##The use of Python's file handling methods and list operations makes the process efficient and straightforward.


# In[ ]:




