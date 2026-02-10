# AI CPU-GPU Performance Analyzer

## Overview
- Software-only system performance analyzer built in Python
- Monitors CPU and GPU usage on a local machine
- Uses machine learning to detect abnormal performance behavior
- Designed for system performance analysis use cases

## Features
- Collects real-time CPU metrics (usage, frequency, load)
- Collects GPU metrics (utilization, memory usage)
- Stores system metrics for analysis
- Machine learning model detects anomalies in performance data
- Streamlit dashboard for visualization and reporting

## Machine Learning Usage
- Unsupervised learning model used for anomaly detection
- Model learns normal system behavior from collected metrics
- Flags unusual CPU or GPU behavior automatically
- Helps identify performance bottlenecks and abnormal workloads

## Tech Stack
- Python 3.12
- Pandas, NumPy
- Scikit-learn
- Streamlit
- System monitoring libraries

## Project Structure
- scripts/ : system metric collection scripts
- data/ : stored performance data
- models/ : trained machine learning models
- dashboard/ : Streamlit dashboard application

## How to Run
- Install dependencies using requirements.txt
- Run data collection scripts
- Start the dashboard using Streamlit

## Use Case
- Performance monitoring on developer machines
- Detect abnormal CPU/GPU behavior
- Useful for system optimization and analysis tasks
