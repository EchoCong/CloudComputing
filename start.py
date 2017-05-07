import couch_server
import couchdb
import datetime
from uuid import uuid4
from vaderSentiment import *
from nltk import tokenize
import reference_dict


def connect_couchDB_server():
    database_server = couch_server.db_server('admin1', 'password')
    secure_server = database_server.secure_server
    origin_db = database_server.db
    sports_db_dict = database_server.sports_db_dict
    return secure_server, origin_db, sports_db_dict


def judge_sentiment(tweet_texts):
    sentence_list = tokenize.sent_tokenize(tweet_texts)
    analyzer = SentimentIntensityAnalyzer()
    paragraph_sentiments=0.0
    for sentence in sentence_list:
        vs = analyzer.polarity_scores(sentence)
        paragraph_sentiments += vs["compound"]
    score = round(paragraph_sentiments/len(sentence_list), 4)
    return score


def get_sentiment_type(doc):
    if judge_sentiment(doc["text"]) >= 0:
        sentiment = "positive"
    else:
        sentiment = "negative"
    return sentiment


def view_to_db(dictionary, couch_view):

    sport_dict = reference_dict.sports_dict
    for each_tweet in couch_view:
        for sport in sport_dict.keys():
            if sport in each_tweet["value"]:
                try:
                    doc = each_tweet["value"][sport]
                    sentiment_type = get_sentiment_type(doc)
                    clean_doc = {
                        "id": doc["id"], "text": doc["text"], "coordinates": doc["coordinates"],
                        "user": {"user_id": doc["user"]["id"], "user_id_str": doc["user"]["id_str"],
                                 "user_name": doc["user"]["name"], "user_lang": doc["user"]["lang"],
                                 "user_time_zone": doc["user"]["time_zone"],
                                 "user_description": doc["user"]["description"]},
                        "place": doc["place"],
                        "sportType": sport,
                        "sentimentType": sentiment_type
                    }
                    doc["_id"] = uuid4().hex
                    dictionary[sport_dict[sport]].save(clean_doc)
                except couchdb.http.ResourceConflict as e:
                    with open('database_log', 'a') as f:
                        f.write("[" + datetime.datetime.now().__str__() + "]" + '\n')
                        f.write(str(e) + '\n')
                        f.write((doc['_id'] + '\n'))


if __name__ == '__main__':

    couch_server, raw_tweets_db, sports_dbs = connect_couchDB_server()
    all_sports_view = raw_tweets_db.view('novel_view/all_sports_view', reduce=False)
    view_to_db(sports_dbs, all_sports_view)