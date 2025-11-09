import json
import random
import time
from datetime import datetime
from config import Config
from mqtt_client import MQTTClient

client = MQTTClient("publisher_temperatura")
client.connect()

time.sleep(2)

print("Publicando datos de temperatura...\n")

for i in range(10):
    data = {
        "sensor_id": "TEMP-001",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mensaje": i,
        "temperatura": round(random.uniform(18.0, 32.0), 2),
        "unidad": "°C"
    }

    msg = json.dumps(data)
    client.publish(Config.TOPIC_TEMPERATURA, msg)
    print(f'Mensaje {i}: {data["temperatura"]}°C')
    time.sleep(2)

print("\n10 mensajes de temperatura enviados")
client.disconnect()