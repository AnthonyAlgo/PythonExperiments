import pandas
import requests
import io
import zipfile
import json

#--Twitter Auth and Request
# Twitter request Factory creates a factory that creates twitter api requests
# The factory is in charge of handling the credentials by retrieving the credentials (bearer token)
# from file and determining the url of the endpoint for the request.
# The actual request just requires a query
# Create a new factory for each request type
# I guess this is way to not have to retrieve credentials everytime you need to send a request

class twitter_request_factory:
       
    bearer_token : str
    url : str
    request_type : str
    
    def __init__(self, url: str, credential_path, request_type):
        self.url = url
        self.request_type = request_type
        self.bearer_token = get_credentials(credential_path)

    def get_credentials(path: str) -> str:
        file = open(path, "r")
        token = file.readline()
        bearer_token = "Bearer " + token
        return bearer_token
    
    def bearer_oauth(self,r):
        """
        Method required by bearer token authentication.
        """
        token = bearer_oauth
        r.headers["Authorization"] = f"Bearer {token}"
        r.headers["User-Agent"] = self.request_type
        return r
            
    def twitter_request_all(self, query_params):
        response = requests.request("GET", self.url, auth=self.bearer_oauth, params=query_params)
        #print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
   
    def twitter_request_get_recent_tweets(self, query_params):
        headers = {"Authorization" : self.bearer_token}
        response = requests.request("GET", self.url, params = query_params, headers=headers)
        #print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response
    
#twit_factory = twitter_request_factory("https://api.twitter.com/2/tweets/search/all", "/Users/at/API Credentials/TwitterCreds.txt","v2FullArchiveSearchPython")

#print(twit_factory.twitter_request_all({'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}))