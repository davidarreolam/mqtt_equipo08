import json
import random
import time
from datetime import datetime
from config import Config
from mqtt_client import MQTTClient

client = MQTTClient("publisher_humedad")
client.connect()

time.sleep(2)

print("Publicando datos de humedad...\n")

for i in range(10):
    data = {
        "sensor_id": "HUM-001",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mensaje": i,
        "humedad": round(random.uniform(40.0, 80.0), 2),
        "unidad": "%"
    }

    msg = json.dumps(data)
    client.publish(Config.TOPIC_HUMEDAD, msg)
    print(f'Mensaje {i}: {data["humedad"]}%')
    time.sleep(2)

print("\n10 mensajes de humedad enviados")
client.disconnect()