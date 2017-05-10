#!/usr/bin/python

import couchdb
import os
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("-f","--file_path",required=True,help="file_path")
args = vars(ap.parse_args())


file_path=args["file_path"]

secure_server = couchdb.Server('http://admin1:password@localhost:5984')
db = secure_server["bigtweet"]


def insert(data):
    try:
        doc_id,doc_rev=db.save(data)
    except Exception as e:
        with open('dabatase_log', 'a') as f:
            f.write(str(e)+'\n')
            f.write((data['_id']+'\n'))

def read_file(file_name):
    # open file from the current dirctory
    fileobject = open(file_name, 'r', encoding='utf-8')
    read_lines(fileobject)
    fileobject.close()


def read_lines(tinyTwitter_File):
    while 1:
        line = tinyTwitter_File.readline()
        if line:
            if line.startswith("{"):
                file_data = line.strip().strip(",")
                data_json = json.loads(file_data)
                data_json["_id"]=data_json["id_str"]
                insert(data_json)


if __name__ == '__main__':
    read_file(file_path)
