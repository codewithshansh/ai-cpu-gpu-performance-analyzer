import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="AMD Performance Analyzer", layout="wide")

st.title("AMD-Style CPU & GPU Performance Analyzer")

# ------------------ Load Data ------------------
cpu_df = pd.read_csv("data/cpu_metrics.csv")
gpu_df = pd.read_csv("data/gpu_metrics.csv")

# ------------------ Rule-Based Analysis ------------------
avg_cpu = cpu_df["cpu_usage_percent"].mean()
avg_gpu = gpu_df["gpu_utilization_percent"].mean()

if avg_cpu > 80 and avg_gpu < 30:
    bottleneck = "CPU-bound workload"
elif avg_gpu > 70 and avg_cpu < 50:
    bottleneck = "GPU-bound workload"
elif avg_cpu > 70 and avg_gpu > 70:
    bottleneck = "Balanced CPU-GPU workload"
else:
    bottleneck = "Idle / IO-bound workload"

# ------------------ Layout ------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("CPU Usage (%)")
    st.line_chart(cpu_df["cpu_usage_percent"])

with col2:
    st.subheader("GPU Usage (%)")
    st.line_chart(gpu_df["gpu_utilization_percent"])

st.subheader("Rule-Based Bottleneck Detection")
st.success(bottleneck)

# ------------------ ML Anomaly Detection ------------------
st.subheader("ML-Based Anomaly Detection (Isolation Forest)")

ml_df = pd.DataFrame()
ml_df["cpu_usage"] = cpu_df["cpu_usage_percent"]
ml_df["memory_usage"] = cpu_df["memory_usage_percent"]
ml_df["gpu_usage"] = gpu_df["gpu_utilization_percent"]

ml_df = ml_df.fillna(0)

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

ml_df["anomaly"] = model.fit_predict(ml_df)

anomalies = ml_df[ml_df["anomaly"] == -1]

st.write(f"Total samples analyzed: {len(ml_df)}")
st.write(f"Anomalies detected: {len(anomalies)}")

if len(anomalies) > 0:
    st.warning("Anomalous performance patterns detected")
    st.dataframe(anomalies.head())
else:
    st.success("No significant anomalies detected")

st.caption(
    "This dashboard combines deterministic performance analysis with "
    "ML-based anomaly detection to identify abnormal system behavior."
)
