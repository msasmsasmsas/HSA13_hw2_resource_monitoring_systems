# HSA13_hw2_resource_monitoring_systems

![изображение](https://github.com/user-attachments/assets/f231b6b6-88da-493d-b7b8-3f3a464498f4)



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
```
## 🚀 Getting Started
1. Clone the Repository
```
git clone https://github.com/yourusername/HSA13_hw2_Resource_monitoring_systems.git
cd HSA13_hw2_Resource_monitoring_systems
```
2. Start the Project
```
docker-compose up --build
```
Services available:

    FastAPI: http://localhost:8080

    Grafana: http://localhost:3000

    InfluxDB: http://localhost:8086

    MongoDB: localhost:27017

    Elasticsearch: http://localhost:9200

## 📈 Load Testing

To simulate traffic and monitor system behavior:

# Windows PowerShell
```
.\load_test.ps1
```
This script sends parallel requests to:

    /load_mongo — writes and reads from MongoDB

    /load_elastic — indexes and queries documents in Elasticsearch

    /combined_load — uses both MongoDB and Elasticsearch

You can customize the number of threads and requests inside load_test.ps1.
## 📉 Monitoring Setup

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

## 📸 Screenshots & Reports
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

## 🧪 Endpoints
Method	Endpoint	Description
GET	/	Hello message
GET	/health	Healthcheck endpoint
GET	/load_elastic	Load test for Elasticsearch
GET	/combined_load	Combined Mongo + Elastic
POST	/load_mongo	Load test for MongoDB


## Test results
```
(.venv) PS E:\HSA13\HSA13_hw2_Resource_monitoring_systems> .\load_test.ps1

в–¶ Starting load on /load_mongo

Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
121    Job121          BackgroundJob   Completed     True            localhost            ...
123    Job123          BackgroundJob   Completed     True            localhost            ...
125    Job125          BackgroundJob   Completed     True            localhost            ...
127    Job127          BackgroundJob   Completed     True            localhost            ...
129    Job129          BackgroundJob   Completed     True            localhost            ...
131    Job131          BackgroundJob   Completed     True            localhost            ...
133    Job133          BackgroundJob   Completed     True            localhost            ...
135    Job135          BackgroundJob   Completed     True            localhost            ...
137    Job137          BackgroundJob   Completed     True            localhost            ...
139    Job139          BackgroundJob   Completed     True            localhost            ...
141    Job141          BackgroundJob   Completed     True            localhost            ...
143    Job143          BackgroundJob   Completed     True            localhost            ...
145    Job145          BackgroundJob   Completed     True            localhost            ...
147    Job147          BackgroundJob   Completed     True            localhost            ...
149    Job149          BackgroundJob   Completed     True            localhost            ...
151    Job151          BackgroundJob   Completed     True            localhost            ...
153    Job153          BackgroundJob   Completed     True            localhost            ...
155    Job155          BackgroundJob   Completed     True            localhost            ...
157    Job157          BackgroundJob   Completed     True            localhost            ...
159    Job159          BackgroundJob   Completed     True            localhost            ...
вњ… Completed /load_mongo in 181.8104512 sec

в–¶ Starting load on /load_elastic
161    Job161          BackgroundJob   Completed     True            localhost            ...                      
163    Job163          BackgroundJob   Completed     True            localhost            ...
165    Job165          BackgroundJob   Completed     True            localhost            ...
167    Job167          BackgroundJob   Completed     True            localhost            ...
169    Job169          BackgroundJob   Completed     True            localhost            ...
171    Job171          BackgroundJob   Completed     True            localhost            ...
173    Job173          BackgroundJob   Completed     True            localhost            ...
175    Job175          BackgroundJob   Completed     True            localhost            ...
177    Job177          BackgroundJob   Completed     True            localhost            ...
179    Job179          BackgroundJob   Completed     True            localhost            ...
181    Job181          BackgroundJob   Completed     True            localhost            ...
183    Job183          BackgroundJob   Completed     True            localhost            ...
185    Job185          BackgroundJob   Completed     True            localhost            ...
187    Job187          BackgroundJob   Completed     True            localhost            ...
189    Job189          BackgroundJob   Completed     True            localhost            ...
191    Job191          BackgroundJob   Completed     True            localhost            ...
193    Job193          BackgroundJob   Completed     True            localhost            ...
195    Job195          BackgroundJob   Completed     True            localhost            ...
197    Job197          BackgroundJob   Completed     True            localhost            ...
199    Job199          BackgroundJob   Completed     True            localhost            ...
вњ… Completed /load_elastic in 128.644355 sec

в–¶ Starting load on /combined_load
201    Job201          BackgroundJob   Completed     True            localhost            ...                      
203    Job203          BackgroundJob   Completed     True            localhost            ...
205    Job205          BackgroundJob   Completed     True            localhost            ...
207    Job207          BackgroundJob   Completed     True            localhost            ...
209    Job209          BackgroundJob   Completed     True            localhost            ...
211    Job211          BackgroundJob   Completed     True            localhost            ...
213    Job213          BackgroundJob   Completed     True            localhost            ...
215    Job215          BackgroundJob   Completed     True            localhost            ...
217    Job217          BackgroundJob   Completed     True            localhost            ...
219    Job219          BackgroundJob   Completed     True            localhost            ...
221    Job221          BackgroundJob   Completed     True            localhost            ...
223    Job223          BackgroundJob   Completed     True            localhost            ...
225    Job225          BackgroundJob   Completed     True            localhost            ...
227    Job227          BackgroundJob   Completed     True            localhost            ...
229    Job229          BackgroundJob   Completed     True            localhost            ...
231    Job231          BackgroundJob   Completed     True            localhost            ...
233    Job233          BackgroundJob   Completed     True            localhost            ...
235    Job235          BackgroundJob   Completed     True            localhost            ...
237    Job237          BackgroundJob   Completed     True            localhost            ...
239    Job239          BackgroundJob   Completed     True            localhost            ...
вњ… Completed /combined_load in 281.2246631 sec

рџ•’ Total Execution Time: 591.6946794 seconds

```
![изображение](https://github.com/user-attachments/assets/6347e7dd-f541-49b6-bb9d-36c63a333652)
