
[Unit]
Description=Simple Network Monitoring Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/network_monitor/network_monitor.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
