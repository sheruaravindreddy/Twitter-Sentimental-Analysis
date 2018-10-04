import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt

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

#...Removing preposiitons, conjuctions and pronouns from the tweet
words = nltk.word_tokenize(tweet)
tags = nltk.pos_tag(words)
print tags
#Tags_list = pd.read_html('http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html')[0][1]
del_tags = ['PRP','DT','CC', 'IN', 'PRP$', 'VBP', 'NNP', 'VBZ', 'VB', 'MD', 'RB', 'VBD', 'WP', 'CD', 'WRB', 'WDT']

new_tags = []
for i in tags:
    if i[1] not in del_tags:
        new_tags.append(i[0])

tweet = " ".join(new_tags)
print tweet

# =============================================================================
# from wordcloud import WordCloud
# wordcloud = WordCloud(width = 800, height = 500, random_state = 21, max_font_size = 110).generate(tweet)
# 
# plt.figure(figsize = (10,7))
# plt.imshow(wordcloud, interpolation = 'bilinear')
# plt.axis('off')
# plt.show()
# =============================================================================
