import psutil
import pandas as pd
import time
from datetime import datetime

OUTPUT_FILE = "data/cpu_metrics.csv"
DURATION_SECONDS = 30      # total collection time
INTERVAL_SECONDS = 1       # sampling interval

data = []

print("Starting CPU metric collection...")

for _ in range(DURATION_SECONDS):
    cpu_usage = psutil.cpu_percent(interval=INTERVAL_SECONDS)
    memory_usage = psutil.virtual_memory().percent
    ctx_switches = psutil.cpu_stats().ctx_switches
    cores = psutil.cpu_count(logical=True)

    data.append({
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage,
        "context_switches": ctx_switches,
        "logical_cores": cores
    })

print("Metric collection completed.")

df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Metrics saved to {OUTPUT_FILE}")
