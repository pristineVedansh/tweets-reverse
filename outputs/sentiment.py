#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os

os.chdir("AITMC")

# read CSVs
riots = pd.read_csv("AITMC.csv")
#trump_visit = pd.read_csv("trump_visit.csv")
#during_election = pd.read_csv("during_election.csv")
riots = riots[['date', 'username', 'tweet', 'replies_count', 'retweets_count', 'likes_count', 'hashtags']]
riots.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)


riots.head(5)


print(riots.shape)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


scores_riots = []
sentences_riots = riots['tweet'].tolist()

for sentence in sentences_riots:
    score = analyser.polarity_scores(sentence)
    print("Score for {} is {}".format(sentence, score))
    scores_riots.append(score)
    
#Converting List of Dictionaries into Dataframe
dataFrame_riots = pd.DataFrame(scores_riots)

dataFrame_riots.to_csv("AITMC_sentiment.csv", index=False)
print("Overall Sentiment Score for the multiple sentences :- ", dataFrame_riots.mean())