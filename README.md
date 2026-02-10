<<<<<<< HEAD
\# AI CPU–GPU Performance Analyzer



An AI-driven system performance analysis tool that monitors CPU and GPU utilization,

detects performance bottlenecks using rule-based logic, and identifies abnormal

performance behavior using machine learning.



---



\## Problem Statement



Modern computing workloads rely on efficient coordination between CPU and GPU resources.

However, performance issues such as CPU bottlenecks, GPU underutilization, or abnormal

workload behavior are difficult to detect using static thresholds alone.



Traditional monitoring tools provide raw metrics but do not automatically identify

unexpected or anomalous performance patterns.



This project bridges that gap by combining deterministic performance analysis with

machine learning–based anomaly detection.



---



\## Project Overview



This system:

\- Collects real-time CPU, memory, and GPU performance metrics

\- Visualizes performance trends through an interactive dashboard

\- Detects CPU–GPU bottlenecks using explainable rule-based logic

\- Identifies abnormal performance behavior using machine learning

\- Assists engineers in investigating performance issues efficiently



---



\## Machine Learning Component



The project uses an unsupervised Isolation Forest model for anomaly detection.



\### Rationale

\- Does not require labeled training data

\- Learns normal system performance behavior automatically

\- Detects deviations that indicate potential performance anomalies



\### ML Functionality

\- Learns baseline CPU, memory, and GPU usage patterns

\- Flags anomalous metric combinations such as high CPU usage with low GPU utilization

\- Supports performance investigation rather than automated optimization



The ML component is designed to complement deterministic analysis and support

human decision-making.



---



\## Dashboard Features



The Streamlit-based dashboard provides:

\- Time-series visualization of CPU usage

\- Time-series visualization of GPU utilization

\- Rule-based bottleneck classification

\- Machine learning–detected anomalous performance samples



All analysis outputs are presented in a unified interface.



---



\## System Architecture



1\. Performance metrics are collected using Python-based monitoring scripts

2\. Collected data is stored and preprocessed for analysis

3\. Rule-based logic identifies known performance bottlenecks

4\. Machine learning detects abnormal performance patterns

5\. Results are visualized through an interactive dashboard



---



\## Technology Stack



\- Python 3.12

\- psutil for CPU and memory metrics

\- GPUtil for GPU utilization metrics

\- Streamlit for dashboard visualization

\- scikit-learn for machine learning

\- Pandas and Matplotlib for data processing and visualization



---



\## How to Run



\### Install dependencies

```bash

pip install -r requirements.txt



=======
# AI CPU–GPU Performance Analyzer

An AI-driven system performance analysis tool that monitors CPU and GPU utilization,
detects performance bottlenecks using rule-based logic, and identifies abnormal
performance behavior using machine learning.

---

## 📌 Problem Statement

Modern computing workloads rely on efficient coordination between CPU and GPU resources.
However, performance issues such as CPU bottlenecks, GPU underutilization, or abnormal
workload behavior are difficult to detect using static thresholds alone.

Traditional monitoring tools provide raw metrics, but they do not help engineers
automatically identify **unexpected or abnormal performance patterns**.

This project addresses that gap by combining deterministic performance analysis with
ML-based anomaly detection.

---

## 🚀 What This Project Does

- Collects real system metrics (CPU, memory, GPU utilization)
- Visualizes performance trends using an interactive dashboard
- Detects CPU–GPU bottlenecks using explainable rule-based logic
- Uses machine learning to automatically detect abnormal performance behavior
- Assists engineers in identifying where further investigation is needed

---

## 🧠 Machine Learning Component

This project uses an **unsupervised Isolation Forest model** for anomaly detection.

### Why Isolation Forest?
- Does not require labeled data
- Learns normal system behavior automatically
- Flags performance patterns that significantly deviate from typical behavior

### What the ML Model Does
- Learns normal CPU, memory, and GPU usage patterns
- Identifies anomalous performance snapshots (e.g., high CPU usage with idle GPU)
- Acts as an early warning system for unexpected system behavior

⚠️ The model does **not** optimize performance automatically.
It supports **human investigation and decision-making**, which aligns with real-world
performance engineering workflows.

---

## 📊 Dashboard Overview

The Streamlit dashboard provides:
- CPU usage trends over time
- GPU utilization trends over time
- Rule-based bottleneck classification
- ML-detected anomalous performance samples

The dashboard integrates deterministic logic and ML results in a single view to improve
performance analysis and debugging.

---

## 🏗️ Project Architecture

1. System metrics are collected using Python scripts
2. Metrics are stored and preprocessed for analysis
3. Rule-based logic detects known performance bottlenecks
4. Machine learning identifies abnormal performance patterns
5. Results are visualized in an interactive dashboard

---

## 🛠️ Tech Stack

- **Python 3.12**
- **psutil** – CPU & memory metrics
- **GPUtil** – GPU utilization metrics
- **Streamlit** – Interactive dashboard
- **scikit-learn** – Machine learning (Isolation Forest)
- **Pandas & Matplotlib** – Data processing and visualization

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
>>>>>>> 1f8aee05a77ec442812150bf7f9e9f33337e6a96
