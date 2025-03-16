from fastapi import FastAPI
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import random

app = FastAPI()
mongo_client = MongoClient("mongo:27017")
es_client = Elasticsearch("http://elasticsearch:9200")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/load_mongo")
async def load_mongo():
    db = mongo_client.test_db
    collection = db.test_collection
    for _ in range(100):
        collection.insert_one({"value": random.randint(1, 1000)})
    result = collection.find().limit(100)
    return {"inserted": 100, "fetched": len(list(result))}

@app.get("/load_elastic")
async def load_elastic():
    for i in range(100):
        es_client.index(index="test_index", body={"value": random.randint(1, 1000)})
    result = es_client.search(index="test_index", query={"match_all": {}})
    return {"indexed": 100, "found": result["hits"]["total"]["value"]}

@app.get("/combined_load")
async def combined_load():
    mongo_result = await load_mongo()
    elastic_result = await load_elastic()
    return {"mongo": mongo_result, "elastic": elastic_result}