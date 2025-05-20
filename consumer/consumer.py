from kafka import KafkaConsumer
import json, os
import pymongo

consumer = KafkaConsumer('iot-sensor-data',
                         bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = mongo_client["iot_data"]
collection = db["sensor_readings"]

for message in consumer:
    data = message.value
    collection.insert_one(data)
    print("Stored:", data)
    if data["temperature"] > 35:
        print("🔥 High temperature alert!")