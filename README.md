# Log Monitoring System

This project implements a comprehensive log monitoring system using containers. It generates application logs, ships them to Elasticsearch, and monitors log ingestion with Prometheus alerts.

## Components

- **App Server**: Python application that generates random logs every 5 seconds
- **Log Shipper (Filebeat)**: Collects logs and sends them to Elasticsearch
- **Elasticsearch**: Storage for log data
- **Kibana**: UI for visualizing logs
- **Prometheus**: Monitoring system to track log metrics
- **AlertManager**: Sends alerts to Slack when issues are detected
- **Log Exporter**: Custom service exposing Elasticsearch document counts as Prometheus metrics

## Architecture

```
App Server → Logs → Filebeat → Elasticsearch ← Kibana
                                    ↑
                                Log Exporter → Prometheus → AlertManager → Slack
```
## Alerting
The system is configured to trigger alerts when:
- No new logs are detected in Elasticsearch for 5 minute

## Setup and Usage
1. Clone this repository
2. Update the Slack webhook URL in `alertmanager.yml`
3. Start the services:

```bash
docker-compose up -d
```
4. Access the services:
   - Kibana: http://localhost:5601
   - Prometheus: http://localhost:9090
   - AlertManager: http://localhost:9093
   - Log Exporter: http://localhost:8080

## Configuration
- `docker-compose.yaml`: Service definitions and configurations
- `prometheus.yml`: Prometheus configuration
- `alertmanager.yml`: Alert routing configuration
- `filebeat.yml`: Log shipping configuration
- `prometheus-alert.yml`: Alert rules for log monitoring
