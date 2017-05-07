from vaderSentiment import *
from nltk import tokenize
import reference_dict

# get coordinate information from tweets and save into a list
indoor_tweets = []
run_tweets = []
rugby_tweets = []
football_tweets = []
soccer_tweets = []
basketball_tweets = []
tennis_tweets = []
swim_tweets = []
cycle_tweets = []
cricket_tweets = []
sydney_tweets = []
melbourne_tweets = []
perth_tweets = []
adelaide_tweets = []
canberra_tweets = []
brisbane_tweets = []
non_sydney_tweets = []
non_melbourne_tweets = []
non_perth_tweets = []
non_adelaide_tweets = []
non_canberra_tweets = []
non_brisbane_tweets = []
nonsport_tweets = []
sportType = " "
sentimentType = " "


def search_city(twitter_object):
    city_name = twitter_object["place"]["name"]
    if city_name == "Sydney":
        sydney_tweets.append(twitter_object)
    elif city_name == "Melbourne":
        melbourne_tweets.append(twitter_object)
    elif city_name == "Brisbane":
        brisbane_tweets.append(twitter_object)
    elif city_name == "Perth":
        perth_tweets.append(twitter_object)
    elif city_name == "Adelaide":
        adelaide_tweets.append(twitter_object)
    elif city_name == "Canberra":
        canberra_tweets.append(twitter_object)


def non_city(twitter_object):
    if twitter_object["place"]:
       city_names = twitter_object["place"]["name"]
       if city_names == "Sydney":
          non_sydney_tweets.append(twitter_object)
       elif city_names == "Melbourne":
          non_melbourne_tweets.append(twitter_object)
       elif city_names == "Brisbane":
          non_brisbane_tweets.append(twitter_object)
       elif city_names == "Perth":
          non_perth_tweets.append(twitter_object)
       elif city_names == "Adelaide":
          non_adelaide_tweets.append(twitter_object)
       elif city_names == "Canberra":
        non_canberra_tweets.append(twitter_object)




