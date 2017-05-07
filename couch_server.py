#!/usr/bin/python
import reference_dict
import couchdb


class db_server(object):
    def __init__(self, username, login):
        self.secure_server = couchdb.Server('http://%s:%s@130.220.212.108:5984/' % (username, login))
        self.db = self.secure_server["viewdatabase"]
        self.sports_db_dict = self.get_sports_db_list()

    def get_sports_db_list(self):
        sports_db_dict = {}
        couch_dict = reference_dict.couch_dict
        for sport_db in couch_dict.keys():
            try:
                sports_db_dict[sport_db] = self.secure_server[couch_dict[sport_db]]
            except Exception:
                sports_db_dict[sport_db] = self.secure_server.create(couch_dict[sport_db])
        return sports_db_dict
