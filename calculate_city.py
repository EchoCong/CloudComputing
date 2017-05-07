import couchdb
from vaderSentiment import *
import reference_dict


def get_sports_db_list(secure_server):
    sports_db_dict = {}
    couch_dict = reference_dict.couch_dict
    for sport_db in couch_dict.keys():
        try:
            sports_db_dict[sport_db] = secure_server[couch_dict[sport_db]]
        except Exception:
            sports_db_dict[sport_db] = secure_server.create(couch_dict[sport_db])
    return sports_db_dict


def connect_couchDB_server():

    secure_server = couchdb.Server('http://localhost:9000/')
    origin_db = secure_server["viewdatabase"]
    sports_db_dict = get_sports_db_list(secure_server)
    return secure_server, origin_db, sports_db_dict


def calculate_city():
    total_count = 0
    city_list = reference_dict.citylist
    couch_dict = reference_dict.couch_dict
    sports_dict_rv = reference_dict.sports_dict_rv
    final_list = {}
    for db in sports_dbs.keys():
        view = couch_server[couch_dict[db]].view('view/city', reduce=False)
        sport_info = {}
        for city in city_list:
            count = 0
            pos_count = 0
            neg_count = 0
            for doc in view:
                if doc["key"] == city:
                    count = count + 1
                    total_count = total_count +1
                    if (doc["value"] == "positive"):
                        pos_count = pos_count + 1
                    elif (doc["value"] == "negative"):
                        neg_count = neg_count + 1
            city_info = {"count": count, "sentiment": {"neg": neg_count, "pos": pos_count}}
            sport_info[city] = city_info
        final_list[sports_dict_rv[db]] = sport_info
    with open("final_list.json", "w") as Twitter_Output_File:
        json.dump(final_list, Twitter_Output_File, indent=2)


if __name__ == '__main__':

    couch_server, raw_tweets_db, sports_dbs = connect_couchDB_server()
    calculate_city()