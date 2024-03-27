#!/usr/bin/env bash

# copy this tile to run.sh and add configuration

TANK_SENDER_DIR="/path/to/tank-sender"
export MQTT_USER="user"
export MQTT_PASS="password"
export MQTT_HOST="mqtt-host.example.com"
export MQTT_PORT="1883"
export TEMP_SENSORS="Label 1:SENSOR_ID_1, Label 2:SENSOR_ID2"

cd "$TANK_SENDER_DIR"
venv/bin/python3 tank-sender.py