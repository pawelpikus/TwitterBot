import tweepy
import time

consumer_key, consumer_secret = 'zfpHpfFvo90yMDzowqwFNxinu', 'QTvstr7ADcUeXTFlqNGMT4pPxTNvLoSicre9AUw3WnKd9Xxezg'
access_token, access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get all the tweets from your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()


#  prevent hitting API to many times
def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
        except StopIteration:
            print("Breaking the iteration...")
            break


#  generous bot
followers = tweepy.Cursor(api.followers).items()  # list of followers

for follower in limit_handler(followers):
    follower.follow()
    print(f"Following: "+follower)


#  search bot
search_string = 'developer'
numOfTweets = 3

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numOfTweets)):
    try:
        tweet.favorite()
        print("Tweet liked.")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break




