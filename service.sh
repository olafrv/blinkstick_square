#!/bin/bash

SERVICE_NAME="blinkstick"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"
PYTHON_EXEC="$(pwd)/.venv/bin/uvicorn"  # or python3
SCRIPT_PATH="--host 0.0.0.0 server:app"  # or server.py

# Create systemd service file
# User 'root' is needed to bind 
# the TCP 8000 port to 0.0.0.0
echo "[Unit]
Description=BlickStick API Service
After=network.target

[Service]
ExecStart=$PYTHON_EXEC $SCRIPT_PATH
WorkingDirectory=$(pwd)
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target" | sudo tee $SERVICE_FILE > /dev/null

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# Check status
sudo systemctl status $SERVICE_NAME --no-pager
