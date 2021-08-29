import json
import requests
from os import environ as env

ENV=dict(env)

API_ENDPOINT="https://api.twitter.com"

HEADERS = {
    "Authorization": "Bearer %s" % ENV['TWITTER_BEARER_TOKEN']
}

def api_get(uri, parameters=None):
    response = requests.get("%s%s" % (API_ENDPOINT, uri), params=parameters, headers=HEADERS)

    if response.status_code != 200:
        print("aaaaaaaa")
        print(response.status_code)
        return

    return response.json()

def get_users(usernames):
    response = api_get("/2/users/by", {"usernames": ",".join(usernames)})

    return [user['id'] for user in response['data']]

def get_tweets(user):
    response = api_get("/2/users/%s/tweets" % user)

    return response['data']

user_list = [
    "kevinmuir",
    "thegrugq"
]

users = get_users(user_list)

for user in users:
    tweets = get_tweets(user)
    for tweet in tweets:
        print("Tweet:")
        print(tweet['text'])
