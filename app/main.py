from fastapi import FastAPI
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import requests



app = FastAPI()
client = MongoClient("mongodb://mongodb:27017")
db = client.test

@app.get("/health")
def health_check():
    return {"status": "ok"}


es = Elasticsearch(
    ["https://elasticsearch:9200"],
    verify_certs=False,  # Отключает проверку сертификатов
    basic_auth=('elastic', 'password')  # Укажите правильные учетные данные, если есть
)

@app.get("/data")
def get_data():
    try:
        mongo_status = db.command("ping")
    except Exception as e:
        mongo_status = {"error": str(e)}

    try:
        es_status = es.ping()
    except Exception as e:
        es_status = False

    return {"mongo": mongo_status, "elasticsearch": es_status}