import re

# sports_dict for "test.py"
sports_dict = {"run": "run_db", "indoor": "indoor_db", "rugby": "rugby_db", "football": "football_db",
               "soccer": "soccer_db", "basketball": "basketball_db", "tennis": "tennis_db", "swim": "swim_db",
               "cycle": "cycle_db", "cricket": "cricket_db"}

# regrex_dict for "testSmallTweets.py"
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

re_dict = {"run": run, "indoor": indoor, "rugby": rugby, "football": football, "soccer": soccer,
           "basketball": basketball, "tennis": tennis, "swim": swim, "cycle": cycle, "cricket": cricket}

# couch_dict for "connect_couchdb.py"
couch_dict = {"indoor_db": "indoor_tweets", "run_db": "run_tweets", "rugby_db": "rugby_tweets",
              "football_db": "football_tweets", "soccer_db": "soccer_tweets",
              "basketball_db": "basketball_tweets", "tennis_db": "tennis_tweets",
              "swim_db": "swim_tweets", "cycle_db": "cycle_tweets", "cricket_db": "cricket_tweets"}