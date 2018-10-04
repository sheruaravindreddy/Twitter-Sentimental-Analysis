import pandas as pd
import re
from wordcloud import WordCloud
import nltk
import seaborn as sns
import matplotlib.pyplot as plt


import timeit
t1 = timeit.default_timer()

#from preprocessing import cleaning
#df = cleaning.df
#df.to_csv('Cleaned_Data.csv')

cleaned_df = pd.read_csv('Cleaned_Data.csv')
cleaned_df = cleaned_df.dropna()
cleaned_df = cleaned_df.reset_index()

def plot_words(df):
    all_words = " ".join(df['tweet'])
    wordcloud = WordCloud(width = 800, height = 600, random_state = 20, max_font_size = 100).generate(all_words)
    plt.figure(figsize = (10,7))
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.show()

df_pos = cleaned_df[cleaned_df['label'] == 0]
#plot_words(df_pos)

df_neg = cleaned_df[cleaned_df['label'] == 1]
#plot_words(df_neg)


def extract_hashtags(tweets):
    hashtags_list = []
    for i in tweets:
        ht = re.findall(r"#(\w+)", i)
        hashtags_list.append(ht)
    return hashtags_list;


def plot_hashtag(dataframe):
    b = nltk.FreqDist(dataframe)
    tweet_count = pd.DataFrame({'Hashtag': list(b.keys()), 'Count': list(b.values())})
    few_hashtags = tweet_count.nlargest(columns="Count", n = 15)
    plt.figure(figsize=(16,5))
    ax = sns.barplot(data=few_hashtags, x= "Hashtag", y = "Count")
    ax.set(ylabel = 'Count')
    plt.show()
    return tweet_count;


df = pd.read_csv("C:/Users/sheruaravindreddy/Downloads/train_E6oV3lV.csv")

normal_ht = sum(extract_hashtags(df['tweet'][df['label'] == 0]),[])
neg_ht = sum(extract_hashtags(df['tweet'][df['label'] == 1]),[])

pos_count = plot_hashtag(normal_ht)
neg_count = plot_hashtag(neg_ht)

t2 = timeit.default_timer()
print (t2 - t1)