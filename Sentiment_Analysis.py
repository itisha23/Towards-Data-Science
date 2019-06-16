#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PACKAGES: Tweepy, nltk,textBlob


# In[5]:


import tweepy
from textblob import TextBlob


# In[ ]:


#written from twitter developer app


# In[10]:


consumer_key = 'Y7iN1HB6yGzR7UE3vr4fS2Vbf'
consumer_secret = 'hwZmrbSm5NxrUyynbkvZhZJTqYPLAJ4x85UtNFNmoQOEJzHjQ1'
access_token = '2570295319-0oqWmJXiOy0LHoByufgAUyn8X2eyYLsFlCNcLhV'
access_token_secret = 'TdQNySL1Y52dxmn3o3v3T9z0VIYhIH8UqUzTsixhy0MNX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)


# In[12]:


api = tweepy.API(auth)


# In[13]:


public_tweets = api.search('Trump')


# In[17]:


for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.polarity)
    
#polarity measures how positive or negative the text is


# In[ ]:




