import tweepy
from textblob import TextBlob
import pandas as pd

consumer_key='UTx1m8vLBNjGqfygeF5KO3o8V'
consumer_secret= 'x8b3TCToIP0UUNt2NRcn8FqxsoRH5cn6oHCnLAjsyL6HDQgzzD'

access_token= '64656251-bqE7PXIA6TrTLj6LtXdMb3BufFgcW7jhmnrTz0HPB'
access_token_secret= 'sklcJ0Bhm7qr5pXRTC6ew39sZj1iMdlkJbxNJprIv34u9'

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





