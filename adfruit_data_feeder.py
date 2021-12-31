import os
import time
import sys
#import Adafruit_DHT as dht
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

        # payload["Battery_percentage"] = battery.percent
        # payload["Battery_secs_left"] = battery.secsleft if str(battery.secsleft).isdigit() else "Charging"
        # payload["Power_plugged"] = battery.power_plugged
        # payload["cpu_details"] = cpu_details.current
        # payload["cpu_max"] = cpu_details.max
        # payload["cpu_min"] = cpu_details.min
        # print(payload)

        # Sending humidity and temperature data to ADAFRUIT_HOST
        client.publish('vinayakaswamy123/feeds/battery_percentage',battery.percent)
        client.publish('vinayakaswamy123/feeds/cpu_current',cpu_details.current)
        client.publish('vinayakaswamy123/feeds/Battery_secs_left', battery.secsleft if str(battery.secsleft).isdigit() else "Charging")
        client.publish('vinayakaswamy123/feeds/Power_plugged', battery.power_plugged)
        client.publish('vinayakaswamy123/feeds/cpu_max', cpu_details.max)
        client.publish('vinayakaswamy123/feeds/cpu_min', cpu_details.min)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()