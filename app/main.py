from fastapi import FastAPI
from pymongo import MongoClient
import requests

app = FastAPI()
client = MongoClient("mongodb://mongodb:27017")
db = client.test

@app.get("/health")
def health_check():
    return {"status": "ok"}

#@app.get("/data")
#def fetch_data():
#    response = requests.get("http://elasticsearch:9200")
#    return {"elasticsearch": response.json(), "mongo_collections": db.list_collection_names()}
@app.get("/data")
def fetch_data():
    try:
        response = requests.get("http://elasticsearch:9200", timeout=5)
        return {"elasticsearch": response.json(), "mongo_collections": db.list_collection_names()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
