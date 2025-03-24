#!/bin/bash

# NOTE: 
# Here the host, port, User and Group vales could be all changed.
# If you are NOT using uvicorn the ports are on 'server.py'

SERVICE_NAME="blinkstick"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

PYTHON_EXEC="$(pwd)/.venv/bin/uvicorn"
SCRIPT_PATH="--host 0.0.0.0 --port 8000 server:app"

# Uncomment these lines to not use uvicorn
# PYTHON_EXEC="$(pwd)/.venv/bin/python3"
# SCRIPT_PATH="server.py"

# Create systemd service file
echo "[Unit]
Description=BlickStick API Service
After=network.target

[Service]
ExecStart=$PYTHON_EXEC $SCRIPT_PATH
WorkingDirectory=$(pwd)
Restart=always
User=pi
Group=pi

[Install]
WantedBy=multi-user.target" | sudo tee $SERVICE_FILE > /dev/null

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# Check status
sudo systemctl status $SERVICE_NAME --no-pager
