# Write a Python program to find out the number of CPUs used.

import multiprocessing
import os

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()
os_cpu_count = os.cpu_count()

# Print the number of CPU cores available on the system.
print("Multiprocessing ",cpu_count)
print("OS ",os_cpu_count)
