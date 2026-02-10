import pandas as pd

cpu_file = "data/cpu_metrics.csv"
gpu_file = "data/gpu_metrics.csv"

cpu_df = pd.read_csv(cpu_file)
gpu_df = pd.read_csv(gpu_file)

avg_cpu = cpu_df["cpu_usage_percent"].mean()
avg_gpu = gpu_df["gpu_utilization_percent"].mean()

print(f"Average CPU Usage: {avg_cpu:.2f}%")
print(f"Average GPU Usage: {avg_gpu:.2f}%")

if avg_cpu > 80 and avg_gpu < 30:
    bottleneck = "CPU-bound workload"
elif avg_gpu > 70 and avg_cpu < 50:
    bottleneck = "GPU-bound workload"
elif avg_cpu > 70 and avg_gpu > 70:
    bottleneck = "Balanced CPU-GPU workload"
else:
    bottleneck = "Idle / IO-bound workload"

print("\nDetected Bottleneck:")
print(bottleneck)
