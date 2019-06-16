#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Textblob
#packaes Neeeded: textblob


# In[8]:


from textblob import TextBlob
import nltk 
nltk.download()


# In[9]:


wiki = TextBlob("Siraj is angry, he never get good match on tinder")
wiki.tags


# In[10]:


wiki.words


# In[ ]:




