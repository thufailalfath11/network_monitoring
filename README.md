1. Install Dependensi
sudo apt update
sudo apt install python3-pip
pip3 install psutil

2. Clone repositori
git clone https://github.com/thufailalfath11/network_monitoring

3. pindahkan systemd Service
sudo mv network-monitor.service /etc/systemd/system/network-monitor.service

4.  Reload & Jalankan Service
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable network-monitor.service
sudo systemctl start network-monitor.service


📖 5. Cek Status & Log
sudo systemctl status network-monitor.service
tail -f /var/log/network_monitor.log
