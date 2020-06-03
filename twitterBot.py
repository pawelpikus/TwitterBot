import tweepy
import time

consumer_key, consumer_secret = 'zfpHpfFvo90yMDzowqwFNxinu', 'QTvstr7ADcUeXTFlqNGMT4pPxTNvLoSicre9AUw3WnKd9Xxezg'
access_token, access_token_secret = '1268207490711326721-gguRdIhZgZ06QhhqzTRhDH9X2cvG1X', 'Vv0WHVYoJwnRMAySPK8UPBvK4XtFjkT72HldRhs7zXOGk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#  get all the tweets from your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()


#  prevent hitting API to many times
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


#  generous bot
followers = tweepy.Cursor(api.followers).items()  # list of followers

for follower in followers:
    if follower:
        follower.follow()
        print(f"Following: "+follower)

    else:
        print("You don't have any followers yet.")

