# Tanks Sender

Sender of temperature readings over MQTT message queue

### Installation

Requires Python 3.4+ and a Raspberry PI with Dallas DS18B20 temperature sensors

Install Python 3.
```shell
sudo apt-get install python3 python3-pip python3-venv
```

Clone this repository:
```bash
git clone https://github.com/jonas-lindmark/tank-sender.git
cd tank-sender
```

Create a python virtual environment and install dependencies.
```shell
python3 -m venv ./venv
venv/bin/pip3 install -r requirements.txt
```

### Configure script

