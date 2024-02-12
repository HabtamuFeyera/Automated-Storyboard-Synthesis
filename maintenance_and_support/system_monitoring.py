import psutil
import smtplib

def monitor_system():
    # Monitor CPU usage
    cpu_usage = psutil.cpu_percent()

    # Monitor memory usage
    memory_usage = psutil.virtual_memory().percent

    # Monitor disk usage
    disk_usage = psutil.disk_usage('/').percent

    # Monitor network traffic
    network_traffic = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    # Example: Send email alert if any metric exceeds threshold
    if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
        send_alert_email(cpu_usage, memory_usage, disk_usage, network_traffic)

def send_alert_email(cpu_usage, memory_usage, disk_usage, network_traffic):
    # Send email alert to administrators
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('admin@example.com', 'password')
    message = f"CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%, Disk usage: {disk_usage}%, Network traffic: {network_traffic} bytes"
    server.sendmail('admin@example.com', 'admin@example.com', message)
    server.quit()

if __name__ == "__main__":
    monitor_system()
