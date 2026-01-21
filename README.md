# DevSecOps Monitoring Dashboard

![Dashboard Preview](docs/images/dashboard_preview.png)

A full **DevSecOps monitoring stack** built with **Prometheus**, **Grafana**, **Node Exporter**, **FastAPI**, and **Falco**.
This stack provides **real-time system metrics, application monitoring, and security alerting** for containerized environments.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics & Dashboards](#metrics--dashboards)
- [Falco Security Alerts](#falco-security-alerts)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This project provides a **centralized monitoring solution** for DevSecOps environments. It collects metrics from:

- Linux nodes using **Node Exporter**
- Containerized applications (FastAPI app)
- Security events via **Falco**

All metrics are visualized in **Grafana dashboards**, enabling developers and DevOps engineers to **track system performance, app health, and security alerts** in real-time.

---

## Architecture

      +------------------+
      |  FastAPI App     |
      |  /metrics        |
      +------------------+
               |
               v
      +------------------+
      |   Prometheus     |
      |   Scrapes metrics|
      +------------------+
               |
               v
      +------------------+
      |    Grafana       |
      |  Visualize Data  |
      +------------------+
               ^
               |
      +------------------+
      |   Node Exporter  |
      |   (CPU, RAM, Disk)|
      +------------------+
               ^
               |
      +------------------+
      |      Falco       |
      |  Security Alerts |
      +------------------+


---

## Features

- **System Monitoring:** CPU, Memory, Disk, and Network usage
- **Application Monitoring:** FastAPI request rates per endpoint
- **Security Monitoring:** Falco alerts for suspicious container activity
- **Real-Time Visualization:** Grafana dashboards with 10s refresh rate
- **Alerting Ready:** Panels can trigger alerts in Grafana

---

## Installation

### Prerequisites

- Ubuntu 22.04 LTS (Generic Kernel recommended for Falco eBPF)
- Docker & Docker Compose
- Access to AWS / any cloud VM (optional)

### Steps

```bash
# Clone repository
git clone https://github.com/Festiveokagbare/dvesecop-dashboard.git
cd dvesecop-dashboard

# Start services
docker-compose up -d

Services
* Prometheus: http://localhost:9090
* Grafana: http://localhost:3000 (default login: admin/admin)
* FastAPI App: http://localhost:8000/metrics
* Falco: Logs and alerts in container or via Prometheus sidecar

# Usage
1. Access Grafana → import the JSON dashboard:
    * File: grafana/dashboards/devsecops-dashboard.json

2. Monitor metrics for:
    * CPU / Memory / Disk
    * Network traffic
    * FastAPI requests

3. Watch Falco security alerts for suspicious container activity
```

Metrics & Dashboards
CPU Usage (%)
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

Memory Usage (%)
(node_memory_Active_bytes / node_memory_MemTotal_bytes) * 100
```

Memory Usage (%)
(node_memory_Active_bytes / node_memory_MemTotal_bytes) * 100
```

Network Traffic
* Rx:
rate(node_network_receive_bytes_total{device="eth0"}[10s])
```

* Tx:
rate(node_network_transmit_bytes_total{device="eth0"}[10s])
```

FastAPI Requests
rate(http_requests_total[1m])
```

Falco Security Alerts
Falco monitors container activity in real-time. Examples:
* Unexpected curl inside container
* Writing to sensitive directories
* Privilege escalation attempts
```

Contributing
* Fork the repository
* Create a feature branch
* Commit your changes
* Open a pull request
```

License
MIT License © 2026 Festus Okagbare
```


