import json
import re

dance = []
netball = []
rugby = []
football = []
soccer = []
basketball = []
tennis = []
swim = []
cycle = []
cricket = []

sport_dict = {"dance": dance, "netball": netball, "rugby": rugby, "football": football, "soccer": soccer,
              "basketball": basketball, "tennis": tennis, "swim": swim, "cycle": cycle, "cricket": cricket}

# regrex_dict for "testSmallTweets.py"
dance_re = re.compile(r"dance\b|\bdancing\b|\bdisco\b|\bsamba\b|\btango\b|\bwalts\b", flags=re.I | re.X)
netball_re = re.compile(r"\bnetball\b")
rugby_re = re.compile(r"\brugby\b")
football_re = re.compile(r"\bfootball\b | \bfooty\b | \bAFL\b | \bAustralian Football League\b "
                   r"| \bARF\b | \bAustralian Rules Football\b | \bAussie Rules or Footy\bbNRL\b "
                   r"| \bNational Rugby League\b")
soccer_re = re.compile(r"\bsoccer\b")
basketball_re = re.compile(r"\bbasketball\b")
tennis_re = re.compile(r"\btennis\b")
swim_re = re.compile(r"\bswim\b | \bswimming\b")
cycle_re = re.compile(r"\bcycle\b | \bcycling\b")
cricket_re = re.compile(r"\bcricket\b")

re_dict = {"dance": dance_re, "netball": netball_re, "rugby": rugby_re, "football": football_re, "soccer": soccer_re,
           "basketball": basketball_re, "tennis": tennis_re, "swim": swim_re, "cycle": cycle_re, "cricket": cricket_re}


def read_file(file_name):
    # open file from the current dirctory
    fileobject = open(file_name, 'r', encoding='utf-8')
    return fileobject


def get_coordinates(tinyTwitter_File):
    # get coordinate information from tweets and save into a list
    while 1:
        line = tinyTwitter_File.readline()
        if line:
            if line.startswith("{"):
                file_data = line.strip().strip(",")
                data_json = json.loads(file_data)
                for sport in sport_dict.keys():
                    if re.search(re_dict[sport], data_json["json"]["text"]):
                        sport_dict[sport].append(data_json["json"]["coordinates"]["coordinates"])
        else:
            break
    return sport_dict


if __name__ == '__main__':

        Twitter_File = read_file("/mnt/bigTwitter.json")
        # read tweets file
        coordinates_Data = get_coordinates(Twitter_File)
        # get coordinate info
        with open("big_coor_list.json", "w") as Twitter_Output_File:
            json.dump(coordinates_Data, Twitter_Output_File, indent=4)





