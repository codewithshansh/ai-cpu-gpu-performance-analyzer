import subprocess
import pandas as pd
import time
from datetime import datetime

OUTPUT_FILE = "data/gpu_metrics.csv"
DURATION_SECONDS = 30
INTERVAL_SECONDS = 1

data = []

def get_nvidia_gpu_metrics():
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=utilization.gpu,memory.used,temperature.gpu",
                "--format=csv,noheader,nounits"
            ],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return None

print("Starting GPU metric collection...")

for _ in range(DURATION_SECONDS):
    timestamp = datetime.now().strftime("%H:%M:%S")
    output = get_nvidia_gpu_metrics()

    if output is None or output == "":
        data.append({
            "timestamp": timestamp,
            "gpu_vendor": "Unknown / AMD / Not Available",
            "gpu_utilization_percent": 0,
            "gpu_memory_used_mb": 0,
            "gpu_temperature": None
        })
    else:
        util, mem, temp = output.split(", ")
        data.append({
            "timestamp": timestamp,
            "gpu_vendor": "NVIDIA",
            "gpu_utilization_percent": float(util),
            "gpu_memory_used_mb": float(mem),
            "gpu_temperature": float(temp)
        })

    time.sleep(INTERVAL_SECONDS)

df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)

print(f"GPU metrics saved to {OUTPUT_FILE}")
