import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import psutil

ADAFRUIT_HOST = 'io.adafruit.com'
ACCESS_TOKEN = '*******************************'
USER_NAME = "*******************"

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=60

sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
client.username_pw_set(USER_NAME,ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(ADAFRUIT_HOST, 1883)

client.loop_start()

try:
    while True:

        battery = psutil.sensors_battery()
        cpu_details = psutil.cpu_freq()
        # Sending humidity and temperature data to ADAFRUIT_HOST
        client.publish(f'{USER_NAME}/feeds/battery_percentage',battery.percent)
        client.publish(f'{USER_NAME}/feeds/cpu_current',cpu_details.current)
        client.publish(f'{USER_NAME}/feeds/Battery_secs_left', battery.secsleft if str(battery.secsleft).isdigit() else "Charging")
        client.publish(f'{USER_NAME}/feeds/Power_plugged', battery.power_plugged)
        client.publish(f'{USER_NAME}/feeds/cpu_max', cpu_details.max)
        client.publish(f'{USER_NAME}/feeds/cpu_min', cpu_details.min)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
