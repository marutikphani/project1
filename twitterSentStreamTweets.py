from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json	
import sentimentMod as s

#consumer key, consumer secret, access token, access secret.
ckey="ypKbW2x72jI3BEscXGI2HWgUY"
csecret="sHYMr8quVKYYOo1xWzVJP8Mbzdp7mqNxphedmlboHgvC9GBP08"
atoken="1295313636-xiqgxJn6bAMYLf5pgoDdjZpI6SdNAXCoIGBTM3W"
asecret="lPN6tNWt2dMF4HuFVfg6gxivNXTwYnquITFY5I8Fr1rDq"

class listener(StreamListener):

    def on_data(self, data):
    	all_data = json.loads(data)
    	saveFile = open('tweetStore.txt','a')
        saveFile.write(str(all_data))
        saveFile.write('\n')
        saveFile.close()
    	#print("all_data"+str(all_data))
    	if 'text' not in all_data:
    		return(True)
    	tweet = all_data["text"]
    	sentiment_value, confidence = s.sentiment(tweet)
    	print(tweet, sentiment_value, confidence)

    	if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()
       	return(True)

    def on_error(self, status):
        print status
        return(True)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
def start_stream(text):
	while True:
		try:
			twitterStream = Stream(auth, listener())
			twitterStream.filter(track=[text])
		except:
			continue
start_stream("happy")
