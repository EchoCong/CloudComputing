# CloudComputing
CleanTweetsJsonFile
This document will illustrate how to use the view function of CouchDB with python interface, and how can the CouchDB view function coorperate with sentiment analysis process. 
## Prerequisites
### CouchDB Cluster
You have to have a CouchDB Cluster first. Details refers to ZelongCong's GitHub: 
### Views established first on the CouchDB server through [Fauxton]
Since the paucity of information on how to write couchdb views with python is obvious. Aftering trying our best to create a view with python, it is showed that creating a view with Fauxton could be much easier.
## Connect to the secure CouchDB server and get the wanted database:
After establishig a CouchDB cluster, three things should be get:
 - Server IP Adress
 - Port number (By default : 5984)
 - authentication credentials (optional)
We establish a python server class to make the more secure access to the couchdb server (`"connect_couchdb.py"`):
```
from couchdb import Server
class db_server(object):

    def __init__(self, username, login):
        self.secure_server = Server('http://%s:%s@130.220.212.108:5984' % (username, login))
        self.db = self.secure_server["viewdatabase"]
```
