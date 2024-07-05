import requests
import json
import logging

def get_meme():
    try:
        url = "https://meme-api.com/gimme"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        meme_large = data["preview"][-2]
        subreddit = data["subreddit"]
        return meme_large, subreddit
    except requests.RequestException as e:
        logging.error("Request failed: %s", e)
        raise
    except (KeyError, IndexError) as e:
        logging.error("Error parsing response: %s", e)
        raise

































#import requests
#import json

#def get_meme():
 ##   response = json.loads(requests.get(url).text)
  #  meme_large = response["preview"][-2]
  #  subreddit = response["subreddit"]
  #  return meme_large, subreddit