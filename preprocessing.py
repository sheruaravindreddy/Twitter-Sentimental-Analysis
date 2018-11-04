import pandas as pd
import re

import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

from nltk.corpus import stopwords
stop_words = stopwords.words('english')


#...Function to replace old pattern with new pattern
def pattern_replacement(pattern, tweet, replacement):
    r = re.findall(pattern, tweet)
    for i in r:
        tweet = re.sub(i, replacement, tweet)
    return tweet;

class cleaning:
    df = pd.read_csv('C:/Users/sheruaravindreddy/Downloads/train_E6oV3lV.csv')
    len_df = len(df)
    for index in range(len_df):
        if index % 100 ==0:
            print index
        tweet = df.iloc[index]['tweet']
        
        #...Removing @Users from the tweet
        tweet = pattern_replacement("@[\w]*", tweet, '')
        
        #...Removing non-alphabets from the tweet
        r = re.findall("[^A-Za-z]", tweet)
        for i in r:
            tweet = tweet.replace(i, " ")
            
        #...Removing preposiitons, conjuctions and pronouns from the tweet
        words = nltk.word_tokenize(tweet)
        tags = nltk.pos_tag(words)
        #Tags_list = pd.read_html('http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html')[0][1]
        del_tags = ['PRP','DT','CC', 'IN', 'PRP$', 'VBP', 'NNP', 'VBZ', 'VB', 'MD', 'RB', 'VBD', 'WP', 'CD', 'WRB', 'WDT']
        
        new_tags = []
        for ord_pair in tags:
            if ord_pair[1] not in del_tags and len(ord_pair[0]) >= 3:
#                new_tags.append(stemmer.stem(ord_pair[0]))
                new_tags.append(ord_pair[0])
        
        #...Removing Stopwords from the tweet
        new_tags = [w for w in new_tags if not w in stop_words]
        
        tweet = " ".join(new_tags)
        #...Replacing the tweet in the DataFrame
        df['tweet'][index] = tweet
