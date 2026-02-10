import multiprocessing
import math
import time

def cpu_intensive_task():
    while True:
        # Heavy mathematical computation
        math.sqrt(12345.6789) ** 100

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting CPU workload on {num_cores} cores")

    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_intensive_task)
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("\nStopping CPU workload...")
