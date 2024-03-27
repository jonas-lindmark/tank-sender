#!/usr/bin/env python3
import json

import paho.mqtt.client as paho
import time
from os import environ as env

client = paho.Client()
client.username_pw_set(env['MQTT_USER'], env['MQTT_PASS'])
client.connect(env['MQTT_HOST'], int(env['MQTT_PORT']))
client.loop_start()

# Unpack "Key 1: value1, Key 2: value2" to dictionary
sensors = dict([(k.strip(), v.strip()) for e in env["TEMP_SENSORS"].split(",") for k, v in [e.split(":")]])


def post_mqtt_message(message):
    client.publish('tank/temp', message, qos=1)


def read_temp_raw(sensor):
    with open('/sys/bus/w1/devices/%s/w1_slave' % sensor, 'r') as file:
        lines = file.readlines()
        return lines


def read_temp(sensor):
    lines = read_temp_raw(sensor)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(sensor)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def main():
    temp_readings = dict([(label, read_temp(sensor)) for label, sensor in sensors.items()])
    print(temp_readings)
    post_mqtt_message(json.dumps(temp_readings))


if __name__ == '__main__':
    main()
