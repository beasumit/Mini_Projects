#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
Image.open(r"D:\code\1.jpg")


# In[5]:


from rembg import removemove
from PIL import Image


# In[8]:


input_path = r"D:\code\1.jpg"
output_path = r"D:\code\1.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(r"D:\code\1.png")

