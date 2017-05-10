#!/usr/bin/python
import json

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

sport_dict = {"Dancing": dance, "Netball": netball, "Rugby": rugby, "Football": football, "Soccer": soccer,
              "Basketball": basketball, "Tennis": tennis, "Swimming": swim, "Cycling": cycle, "Cricket": cricket}

file_path="aurin_coor_list.geojson"

def read_file(file_name):
    # open file from the current dirctory
    fileobject = open(file_name, 'r', encoding='utf-8')
    sport_dict = read_lines(fileobject)
    fileobject.close()
    return  sport_dict


def read_lines(tinyTwitter_File):
    data = json.load(tinyTwitter_File)
    for each in data["features"]:
        if each["properties"]["sportsplayed"] in sport_dict.keys():
            sport_dict[each["properties"]["sportsplayed"]].append(each["geometry"]["coordinates"])
        else:
            break
    return sport_dict


if __name__ == '__main__':
    sports_list = read_file(file_path)

    with open("aurin_coor_list.json", "w") as Twitter_Output_File:
        json.dump(sports_list, Twitter_Output_File, indent=4)