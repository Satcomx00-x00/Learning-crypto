import time

# exposants:
op_to_compute = 2 ** 80
ref_op_per_sec= 2 ** 30
# compute time to compute the op_to_compute
compute_time = op_to_compute / ref_op_per_sec
print(f"compute_time: {compute_time} seconds")
compute_time = compute_time / 3600
print(f"compute_time: {compute_time} hours")

