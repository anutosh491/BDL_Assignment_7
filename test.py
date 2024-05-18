import psutil
import numpy as np

# Record the initial CPU usage percentage
cpu_percent = psutil.cpu_percent(interval=1)

# Capture the initial memory usage in KB
memory_usage_start = psutil.virtual_memory().used / 1024

# Initialize a variable
a = 3

# Perform a computation to simulate CPU and memory usage
for i in range(1_000_000):
    a += 1

# Capture the final memory usage in KB
memory_usage_end = psutil.virtual_memory().used / 1024

# Calculate the absolute difference in memory usage
memory_usage = np.abs(memory_usage_end - memory_usage_start)

# Print the results
print(f"CPU Percent: {cpu_percent}%")
print(f"Initial Memory Usage: {memory_usage_start} KB")
print(f"Memory Usage Difference: {memory_usage} KB")
print(f"Random Integer: {np.random.randint(10)}")
