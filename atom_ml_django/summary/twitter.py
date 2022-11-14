import os
from urllib import request

# Secured TOKEN storage
os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAMswjQEAAAAApPk1f8zxv1cnZX6kyqubZynecOY%3DcGv3FCegcRUMu0vDtZQCEWhRz7YbE2kJzQ201wM9tqNQ6uYORf'


# auth token feth
def tw_auth():
    return os.getenv('TOKEN')


# CREATH AUTH HEADER

def tw_create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def tw_post_tweet(text, mentions):
    URL = "https://api.twitter.com/2/tweets"
    args = {
        'text': text

    }
    return (URL, args)


def connect_to_endpoint(url, headers, params, next_token=None):
    # params object received from create_url function
    params['next_token'] = next_token
    response = request.Request("GET", url, headers=headers)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


bearer_token = tw_auth()
headers = tw_create_headers(bearer_token)
text = "TestAuthor"

url = tw_post_tweet(text, "test")
# print(url[0])
json_response = connect_to_endpoint(url[0], headers, url[1])
