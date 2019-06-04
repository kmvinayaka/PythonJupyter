import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import psutil

THINGSBOARD_HOST = 'ec2-35-154-132-166.ap-south-1.compute.amazonaws.com'
ACCESS_TOKEN = 'cpu'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

payload = {}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        
        battery = psutil.sensors_battery()
        cpu_details = psutil.cpu_freq()
      
        payload["Battery_percentage"] = battery.percent
        payload["Battery_secs_left"] = battery.secsleft if str(battery.secsleft).isdigit() else "Charging"
        payload["Power_plugged"] = battery.power_plugged
        payload["cpu_details"]= cpu_details.current
        payload["cpu_max"] = cpu_details.max
        payload["cpu_min"] = cpu_details.min
        print(payload)

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(payload), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
