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
