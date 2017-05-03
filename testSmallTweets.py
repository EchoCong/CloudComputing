import json
import re

search_for = ["fitness", "gym", "dance", "yoga", "spinning",
              "run", "running", "marathon",
              "rugby", "NRL", "National Rugby League",
              "football", "footy", "AFL", "Australian Football League", "ARF",
              "Australian Rules Football", "Aussie Rules or Footy",
              "soccer", "basketball", "tennis", "swim", "swimming",
              "cycle", "cycling", "cricket"]
indoor = re.compile(r"\bfitness\b | \bgym\b | \bdance\b | \byoga\b | \bspinning\b", flags=re.I | re.X)
run = re.compile(r"\brun\b | \brunning\b | \bmarathon\b")
rugby = re.compile(r"\brugby\b")
football = re.compile(r"\bfootball\b | \bfooty\b | \bAFL\b | \bAustralian Football League\b "
                   r"| \bARF\b | \bAustralian Rules Football\b | \bAussie Rules or Footy\bbNRL\b "
                   r"| \bNational Rugby League\b")
soccer = re.compile(r"\bsoccer\b")
basketball = re.compile(r"\bbasketball\b")
tennis = re.compile(r"\btennis\b")
swim = re.compile(r"\bswim\b | \bswimming\b")
cycle = re.compile(r"\bcycle\b | \bcycling\b")
cricket = re.compile(r"\bcricket\b")

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


def read_file(file_name):
    # open file from the current directory
    fileobject = open(file_name, 'r', encoding='utf-8')
    return fileobject


def get_clean_tweet(data):
    tweet_id = data["meta"]["id"]
    text = data["json"]["text"]

    coordinates = data["json"]["coordinates"]["coordinates"]
    user_id = data["json"]["user"]["id"]
    user_id_str = data["json"]["user"]["id_str"]
    user_name = data["json"]["user"]["name"]
    user_lang = data["json"]["user"]["lang"]
    user_time_zone = data["json"]["user"]["time_zone"]
    user_description = data["json"]["user"]["description"]
    place = data["json"]["place"]

    clean_tweet = {
        "id": tweet_id, "text": text, "coordinates": coordinates,
        "user": {"user_id": user_id, "user_id_str": user_id_str,
                 "user_name": user_name, "user_lang": user_lang,
                 "user_time_zone": user_time_zone, "user_description": user_description},
        "place": place
    }
    return clean_tweet


def get_tweet_info(twitter_file):

    while 1:
        line = twitter_file.readline()
        if line:
            if line.startswith("{"):
                file_data = line.strip().strip(",")
                data_json = json.loads(file_data)
                text = data_json["json"]["text"]
                description = data_json["json"]["user"]["description"]
                if re.search(indoor, text) or re.search(indoor, description):
                    clean_tweet = get_clean_tweet(data_json)
                    indoor_tweets.append(clean_tweet)
                elif re.search(run, text) or re.search(run, description):
                    clean_tweet = get_clean_tweet(data_json)
                    run_tweets.append(clean_tweet)
                elif re.search(rugby, text) or re.search(rugby, description):
                    clean_tweet = get_clean_tweet(data_json)
                    rugby_tweets.append(clean_tweet)
                elif re.search(football, text) or re.search(football, description):
                    clean_tweet = get_clean_tweet(data_json)
                    football_tweets.append(clean_tweet)
                elif re.search(soccer, text) or re.search(soccer, description):
                    clean_tweet = get_clean_tweet(data_json)
                    soccer_tweets.append(clean_tweet)
                elif re.search(basketball, text) or re.search(basketball, description):
                    clean_tweet = get_clean_tweet(data_json)
                    basketball_tweets.append(clean_tweet)
                elif re.search(tennis, text) or re.search(tennis, description):
                    clean_tweet = get_clean_tweet(data_json)
                    tennis_tweets.append(clean_tweet)
                elif re.search(swim, text) or re.search(swim, description):
                    clean_tweet = get_clean_tweet(data_json)
                    swim_tweets.append(clean_tweet)
                elif re.search(cycle, text) or re.search(cycle, description):
                    clean_tweet = get_clean_tweet(data_json)
                    cycle_tweets.append(clean_tweet)
                elif re.search(cricket, text) or re.search(cricket, description):
                    clean_tweet = get_clean_tweet(data_json)
                    cricket_tweets.append(clean_tweet)
        else:
            break


def write_tweet_info():
    with open("indoorTwitter.json", "w") as Twitter_Output_File:
        print("indoor count : ", len(indoor_tweets))
        json.dump(indoor_tweets, Twitter_Output_File, indent=4)
    with open("runTwitter.json", "w") as Twitter_Output_File:
        print("run count : ", len(run_tweets))
        json.dump(run_tweets, Twitter_Output_File, indent=4)
    with open("rugbyTwitter.json", "w") as Twitter_Output_File:
        print("rugby count : ", len(rugby_tweets))
        json.dump(rugby_tweets, Twitter_Output_File, indent=4)
    with open("footballTwitter.json", "w") as Twitter_Output_File:
        print("football count : ", len(football_tweets))
        json.dump(football_tweets, Twitter_Output_File, indent=4)
    with open("soccerTwitter.json", "w") as Twitter_Output_File:
        print("soccer count : ", len(soccer_tweets))
        json.dump(soccer_tweets, Twitter_Output_File, indent=4)
    with open("basketballTwitter.json", "w") as Twitter_Output_File:
        print("basketball count : ", len(basketball_tweets))
        json.dump(basketball_tweets, Twitter_Output_File, indent=4)
    with open("tennisTwitter.json", "w") as Twitter_Output_File:
        print("tennis count : ", len(tennis_tweets))
        json.dump(tennis_tweets, Twitter_Output_File, indent=4)
    with open("swimTwitter.json", "w") as Twitter_Output_File:
        print("swim count : ", len(swim_tweets))
        json.dump(swim_tweets, Twitter_Output_File, indent=4)
    with open("cycleTwitter.json", "w") as Twitter_Output_File:
        print("cycle count : ", len(cycle_tweets))
        json.dump(cycle_tweets, Twitter_Output_File, indent=4)
    with open("cricketTwitter.json", "w") as Twitter_Output_File:
        print("cricket count : ", len(cricket_tweets))
        json.dump(cricket_tweets, Twitter_Output_File, indent=4)


if __name__ == '__main__':

    Twitter_Input_File = read_file("smallTwitter.json")
    # read tweets file
    get_tweet_info(Twitter_Input_File)
    # writ tweets file
    write_tweet_info()
