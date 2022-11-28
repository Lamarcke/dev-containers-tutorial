import os
from pymongo.mongo_client import MongoClient
import redis


def mongodb_connect():
    mongo_url = os.environ.get("MONGODB_URL")
    mongo = MongoClient(mongo_url)
    db = mongo.get_database("test")
    return db.get_collection("test")


def redis_connect():

    redis_url = os.environ.get("REDIS_URL")
    redis_client = redis.from_url(redis_url)  # type: ignore
    return redis_client
