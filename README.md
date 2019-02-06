# Twitter-Sentimental-Analysis

Input data contains 2 features:
1) Unprocessed tweet
2) Flag of the tweet(0-positive/1-negative)


Steps followed for building the sentimental analysis model:
- Preprocessing of tweets which incluse removing user handles and non-alphabets using regex, removing unnecessary supportive words using pos_tags and Lemmatization
- Extracting hashtags, finding their Frequency Distribution and creating a word2vec model of hastags.
- Building another word2vec model of tweets, TF-IDF of each word.
- Preparing the data for modelling using the above 2 word2vec models and build a Logistic Regression model.

data_visualisation.ipynb shows the WordCloud and the bar plots of negative and positive hashtags.
