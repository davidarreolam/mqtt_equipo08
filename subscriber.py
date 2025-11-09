from config import Config
from mqtt_client import MQTTClient
import time

client = MQTTClient("mqtt_client")
client.connect()

time.sleep(2)

print(f'Subscribiendo a topico de temperatura')
client.subscribe(Config.TOPIC_TEMPERATURA)
print(f'Subscribiendo a topico de humedad')
client.subscribe(Config.TOPIC_HUMEDAD)

print(f"Escuchando en topicos: {Config.TOPIC_TEMPERATURA}, {Config.TOPIC_HUMEDAD}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
