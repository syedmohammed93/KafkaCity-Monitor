from kafka import KafkaProducer
import json, random, time, os

producer = KafkaProducer(bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "air_quality": round(random.uniform(0, 500), 2),
        "timestamp": time.time()
    }

while True:
    data = generate_sensor_data()
    producer.send('iot-sensor-data', value=data)
    print("Sent:", data)
    time.sleep(1)