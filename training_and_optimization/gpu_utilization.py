import subprocess

def monitor_gpu_utilization():
    # Use subprocess module to run commands like 'nvidia-smi' to monitor GPU utilization
    gpu_info = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'])
    gpu_utilization = float(gpu_info.decode('utf-8').strip())
    return gpu_utilization

def adjust_batch_size(current_batch_size, max_gpu_utilization):
    # Dynamically adjust batch size based on GPU utilization
    if monitor_gpu_utilization() > max_gpu_utilization:
        new_batch_size = int(current_batch_size * 0.9)  # Decrease batch size by 10%
        return new_batch_size
    else:
        return current_batch_size

if __name__ == "__main__":
    # Example usage
    current_batch_size = 64
    max_gpu_utilization = 80  # Adjust as needed
    adjusted_batch_size = adjust_batch_size(current_batch_size, max_gpu_utilization)
    print("Adjusted batch size:", adjusted_batch_size)
