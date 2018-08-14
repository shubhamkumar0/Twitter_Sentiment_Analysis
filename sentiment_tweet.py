import tweepy
from textblob import TextBlob
import pandas as pd

consumer_key='***********'
consumer_secret= '$$$$$$$$$$$$$$$$$$$$$$$$$'

access_token= '%%%%%%%%%%%%%%%%%%'
access_token_secret= '^^^^^^^^^^^^^^^^^^^^^^^'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search('neymar')

df=pd.DataFrame()
print(type(public_tweets))
for tweet in public_tweets:
	#tweet.text
	#label=[]
	
	analysis=TextBlob(tweet.text)
	if (analysis.sentiment>=0):
		label="positive"
	if (analysis.sentiment<0):
		label="negative"
	
	df_temp=pd.DataFrame({'tweet':[tweet.text], 'sentiment':[label]})
	#print(df_temp)
	df=df.append(df_temp)
print(df)
df.to_csv("sentiment.csv",header=True, index=False, encoding='utf-8')





