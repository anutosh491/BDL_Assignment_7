# Health Monitoring of FastAPI

## Overview
This project provides health monitoring for a FastAPI application using Prometheus for metrics collection and Grafana for metrics visualization. 

## Installation
Install Docker and WSL to your local computer.

Run the command `docker-compose up --build` to start the FastAPI application and host the Grafana UI

## Walkthrough of Code
The `main.py` file resides in the `root/src/app/` directory and contains the FastAPI application code, including the necessary updates for Prometheus metrics.
The `prometheus.yml` configuration file is located inside the `root/prometheus_data` directory.
Place the Dockerfile and `requirements.txt` file in the src directory.
Lastly, place the `docker-compose.yml` file in the `root/` directory.

* The main.py file contains the following metrics posted to Prometheus
    1. API Usage Counters: Tracks the number of hits from different client IP addresses.
    2. API Run Time: Records the total time taken by the API to process requests.
    3. API Processing Time (T/L): Measures the effective processing time per character.
    4. CPU Utilization: Monitors the CPU usage rate by the FastAPI application.
    5. Memory Utilization: Tracks the memory usage by the FastAPI application.
    6. Network I/O: Measures the bytes sent and received by the application.
    7. Network I/O Rate: Tracks the rate of bytes sent and received by the application.

    These can be queried in Grafana and visualized

## Additional Information
In case you add some code on top of this, you may have to add the libraries that you use in the `requirements.txt` file in the. Repeat the command and `docker-compose up --build` command as done earlier.

Once the usage is over, ensure to run the command `docker-compose down` to shutdown the local host.
In case your system consumes a lot of memory and disk usage, then open the command promt with administrator access and run `wsl --shutdown` after this.