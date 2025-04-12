# HSA13_hw2_resource_monitoring_systems

![изображение](https://github.com/user-attachments/assets/f231b6b6-88da-493d-b7b8-3f3a464498f4)

![изображение](https://github.com/user-attachments/assets/ee2313e9-49f2-481c-a864-ae7e220cd21b)

![изображение](https://github.com/user-attachments/assets/85176ecd-4a0b-40be-b840-26d79d5b6c82)


# 🛠️ Resource Monitoring System using TIG Stack (Telegraf + InfluxDB + Grafana)

This project demonstrates real-time monitoring of a microservice-based architecture using the **TIG stack** with metrics collected from:

- MongoDB
- Elasticsearch
- FastAPI application
- Nginx
- Docker containers

## 📌 Project Goals

- Set up containerized services (API, DBs, reverse proxy)
- Route requests through Nginx → App → MongoDB/Elasticsearch
- Monitor system health and performance using Telegraf + InfluxDB + Grafana
- Simulate traffic with load testing tools
- Visualize resource usage via dashboards

---

## 📦 Stack Overview

| Component     | Role                                 |
|---------------|--------------------------------------|
| **FastAPI**   | Application backend                  |
| **MongoDB**   | NoSQL database                       |
| **Elasticsearch** | Search engine backend           |
| **Nginx**     | Reverse proxy                        |
| **Telegraf**  | Metrics collector                    |
| **InfluxDB**  | Time-series metrics database         |
| **Grafana**   | Metrics visualization dashboard      |
| **Docker Compose** | Container orchestration        |

---

## 📊 Architecture

```plaintext
Client
  ↓
Nginx (8080)
  ↓
FastAPI (8000)
  ↙       ↘
MongoDB   Elasticsearch

Monitoring:
Telegraf → InfluxDB → Grafana

🚀 Getting Started
1. Clone the Repository

git clone https://github.com/yourusername/HSA13_hw2_Resource_monitoring_systems.git
cd HSA13_hw2_Resource_monitoring_systems

2. Start the Project

docker-compose up --build

Services available:

    FastAPI: http://localhost:8080

    Grafana: http://localhost:3000

    InfluxDB: http://localhost:8086

    MongoDB: localhost:27017

    Elasticsearch: http://localhost:9200

📈 Load Testing

To simulate traffic and monitor system behavior:

# Windows PowerShell
.\load_test.ps1

This script sends parallel requests to:

    /load_mongo — writes and reads from MongoDB

    /load_elastic — indexes and queries documents in Elasticsearch

    /combined_load — uses both MongoDB and Elasticsearch

You can customize the number of threads and requests inside load_test.ps1.
📉 Monitoring Setup

    Grafana Access

        Visit: http://localhost:3000

        Default login: admin / admin

    Data Source

        Type: InfluxDB

        URL: http://influxdb:8086

        Bucket: telegraf

        Token/Org: Set via .env or docker-compose.yml

    Dashboards

        Import pre-configured JSON dashboards from /grafana-dashboards/

        Dashboards include:

            MongoDB operations

            Elasticsearch heap/index/query stats

            Nginx connections

            Docker container CPU, memory, network usage

📸 Screenshots & Reports
Load Testing Proof

    Screenshots of Grafana during active load (CPU, query rates, memory)

    Logs saved in:

        mongo_test.log

        elastic_test.log

        combined_test.log

Report Export

You can export Grafana panels as:

    PNG via panel menu → Share → Export

    PDF via Grafana report tools

🧪 Endpoints
Method	Endpoint	Description
GET	/	Hello message
GET	/health	Healthcheck endpoint
GET	/load_elastic	Load test for Elasticsearch
GET	/combined_load	Combined Mongo + Elastic
POST	/load_mongo	Load test for MongoDB
