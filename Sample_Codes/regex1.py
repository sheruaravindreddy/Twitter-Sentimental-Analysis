import re
import pandas as pd

tweet = "model take all time friday smile user cookie people use cons con personalised booked"

#...replacing old pattern with new pattern
def func(pattern, tweet, replacement):
    r = re.findall(pattern, tweet)
    for i in r:
        tweet = re.sub(i, replacement, tweet)
    return tweet;

#...Removing @Users from the tweet
tweet = func("@[\w]*", tweet, '')

#...Removing non-alphabets from the tweet
r = re.findall("[^A-Za-z]", tweet)
for i in r:
    tweet = tweet.replace(i, " ")    
