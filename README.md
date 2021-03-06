# CloudComputing
CleanTweetsJsonFile
This document will illustrate how to use the view function of CouchDB with python interface, and how can the CouchDB view function coorperate with sentiment analysis process. 
## Prerequisites
### CouchDB Cluster
You have to have a CouchDB Cluster first. Details refers to ZelongCong's GitHub: 
### Raw tweets data
Tweets crawler refers to ZelongCong's GitHub: 
(Data are saved in couchdb)
### Views established first on the CouchDB server through [Fauxton]
Since the paucity of information on how to write couchdb views with python is obvious. Aftering trying our best to create a view with python, it is showed that creating a view with Fauxton could be much easier.
Details would be illustrated in [How to run](## How to run) part
### Connect to the secure CouchDB server and get the wanted database:
After establishig a CouchDB cluster, three things should be get:
 - Server IP Adress (130.220.212.108)
 - Port number (By default : 5984)
 - authentication credentials (optional)(admin1:password)
We establish a python server class to make the more secure access to the couchdb server (`"couch_server.py"`):


## How to run
The repo can be run from two kinds of files: `"start_remote.py"` and `"start.py"` are used to connect CouchDB server,and `calculate_city.py` is used to calculate final information.
### Step1: Create a view
This view is used to classify the raw tweets data in next step. It is created manually in fauxton.
Map function:
```
function(doc) {
  if (doc.text.match(/(\bfitness\b|\bgym\b|\bdance\b|\byoga\b|\bspinning\b)/gi)){
    emit(doc._id,{indoor: doc});
  } else if (doc.text.match(/(\brun\b|\brunning\b|\bmarathon\b|\bhiking\b)/gi)){
    emit(doc._id,{run: doc});
  } else if (doc.text.match(/(\brugby\b | \bNational Rugby League\b)/gi)){
    emit(doc._id,{rugby: doc});
  }else if (doc.text.match(/(\bfootball\b | \bfooty\b | \bAFL\b | \bAustralian Football League\b | \bARF\b | \bAustralian Rules Football\b | \bAussie Rules or Footy\b | \bbNRL\b)/gi)){
    emit(doc._id,{football: doc});
  } else if (doc.text.match(/(\bsoccer\b)/gi)){
    emit(doc._id,{soccer: doc});
  } else if (doc.text.match(/(\bbasketball\b)/gi)){
    emit(doc._id,{bascketball: doc});
  } else if (doc.text.match(/(\btennis\b)/gi)){
    emit(doc._id,{tennis: doc});
  } else if (doc.text.match(/(\bswim\b | \bswimming\b)/gi)){
    emit(doc._id,{swim: doc});
  } else if (doc.text.match(/(\bcycle\b | \bcycling\b)/gi)){
    emit(doc._id,{cycle: doc});
  } else if (doc.text.match(/(\bcricket\b)/gi)){
    emit(doc._id,{cricket: doc});
  }
}
```
### Step2: Classify 
Classify raw tweets into ten catagories according to the top ten most popular sports in Austrilia.(`sports_tweets/sports_tweets`)
Run the command:
```
$ python3 start_remote.py
```
in terminal to connect couchdb server remotely or run the command:
```
$ ssh -N -L 9000:localhost:5984 -i [yourkey] [usrname]@[IP]
$ python3 start.py
```
`[yourkey]` represents the private key generated by Nectar. A key is always used when connecting to the Nectar VM and in this case we build the couchdb cluster server on Nectar VMs. `[username]` is "ubuntu", because we boot the VM from image `ubuntu 16.04`, `[IP]` represents the VM'a IP address.
### Step3: Create sport views respectively
These views are used to calculate final statistical data in next step. (`view/city`)
Map function:
```
var citylist = ["Melbourne", "Sydney", "Brisbane", "Perth", "Adelaide", "Canberra"]
function(doc) {
  if (citylist.indexOf(doc.place.name)){
    emit(doc.place.name , doc.sentimentType);
  } 
}
```
### Step3: Calculate
In each sport databasea (such as "indoor_tweets"), calculat the number of tweets posted in different cities, as well how many of them are expressing positive mood and how many of them are expressing negative mood.
Run the command:
```
$ python3 calculate_city.py
```
### Step4: Result
Final result is a json file delivered to the website. The format is like:
```
{
  "indoor": {
    "Melbourne": {
      "count": 0,
      "sentiment": {
        "neg": 0,
        "pos": 0
      }
    },
    "Sydney": {
      "count": 9,
      "sentiment": {
        "neg": 2,
        "pos": 7
      }
    },
    ...
}
```

