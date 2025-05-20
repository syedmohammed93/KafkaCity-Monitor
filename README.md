# Smart City IoT Monitoring System

This project simulates IoT devices streaming sensor data through Apache Kafka. The system uses Zookeeper for Kafka coordination, MongoDB for data storage, FastAPI for accessing data via a web API, and Docker for orchestration.

## Components
-->Producer : Simulates IoT sensors
-->Kafka    : Real-time messaging
-->Zookeeper: Kafka broker coordination
-->Consumer : Processes and stores data
-->MongoDB  : Stores sensor data
-->FastAPI  : Exposes REST API for sensor data access

## Run the project
```bash
docker-compose up --build
```

## Features
- Real-time data streaming
- Kafka topics for sensor types
- Alerting for high temperatures
- MongoDB storage
- REST API to access sensor data

## Future Improvements
- Integrate Grafana for visualization
- Simulate multiple sensor types
- Add authentication and authorization to API
