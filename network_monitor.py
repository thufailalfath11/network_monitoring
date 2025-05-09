#!/usr/bin/env python3
import psutil
import time
from datetime import datetime

LOG_FILE = "/var/log/network_monitor.log"

def log_network_usage():
    prev = psutil.net_io_counters()
    while True:
        time.sleep(5)
        curr = psutil.net_io_counters()
        sent = (curr.bytes_sent - prev.bytes_sent) / 1024  # in KB
        recv = (curr.bytes_recv - prev.bytes_recv) / 1024
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] Sent: {sent:.2f} KB, Received: 
{recv:.2f} KB\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_line)
        prev = curr

if __name__ == "__main__":
    log_network_usage()

