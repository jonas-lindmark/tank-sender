# Tanks Sender

Sender of temperature readings over MQTT message queue

### Installation

Requires Python 3.4+ and a Raspberry PI with Dallas DS18B20 temperature sensors

Install Python 3.
```shell
sudo apt-get install python3 python3-pip python3-venv python3-paho-mqtt
```

Clone this repository:
```bash
git clone https://github.com/jonas-lindmark/tank-sender.git
cd tank-sender
```

### Configure script

Copy `run-template.sh` to `run.sh` and update configuration for MQTT server (homeassistant etc.).

Set up cronjob to post temperature readings.