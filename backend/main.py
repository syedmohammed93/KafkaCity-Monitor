from fastapi import FastAPI
from pymongo import MongoClient
from os import getenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient(getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.iot_data
collection = db.sensor_readings

@app.get("/data")
def get_all_data():
    return list(collection.find({}, {"_id": 0}))

@app.get("/latest")
def get_latest_entry():
    return collection.find_one(sort=[("timestamp", -1)], projection={"_id": 0})