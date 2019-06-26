# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:39:00 2019

@author: hehehe
"""

from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

#Buat API Twitter di link berikut https://developer.twitter.com/en/apps
consumer_key = "masukkan consumer_key"
consumer_secret = "masukkan consumer_secret"
access_token = "masukkan access_token"
access_token_secret = "masukkan access_token_secret"

class AkangStream(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    
    #def on_data(self, data):
    #    print(data)
    #    return True
    
    def on_status(self, status):
        print(status.text)

if __name__ == '__main__':
    l = AkangStream()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

query=input("Masukkan Keyword : ")
stream = Stream(auth, l)
stream.filter(track=[query])
