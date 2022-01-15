import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["MainDatabase"]
cruise_tweets = database["CruiseTweets"]

#----This block creates a recent_tweet_factory that is used to create recent tweet request based
# on one set of credentials that are stored in the factory
# Each time the loop iterates it produces a new request with the "next_token" from the previous request along with the expected payload

def tweet_reader(iterations: int, query: str):
    recent_tweet_factory = twitter_request_factory("https://api.twitter.com/2/tweets/search/recent", "/Users/at/API Credentials/TwitterCreds.txt","NONE")
    query_params = {'query': query}
    recent_tweet_request = recent_tweet_factory.twitter_request_get_recent_tweets(query_params)
    response = json.dumps(recent_tweet_request.json(),indent=4, sort_keys=True)
    #print(response)
    response_dict = json.loads(response)
    
    next_request_token = response_dict["meta"]
    next_request_token = next_request_token['next_token']
    
    tweet_data = response_dict["data"]
    cruise_tweets.insert_many(tweet_data)
    i = 1
    while i < iterations:
        new_query_params = {'query': query, 'next_token':next_request_token}
        recent_tweet_request = recent_tweet_factory.twitter_request_get_recent_tweets(new_query_params)
        response = json.dumps(recent_tweet_request.json(),indent=4, sort_keys=True)      
        #print(response)
        response_dict = json.loads(response)
        next_request_token = response_dict["meta"]
        next_request_token = next_request_token['next_token']
        tweet_data = response_dict["data"]
        cruise_tweets.insert_many(tweet_data)

        i+=1

for x in cruise_tweets.find():
    print(x)


