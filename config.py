import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BROKER = os.getenv("MQTT_BROKER")
    PORT = 8883
    USERNAME = os.getenv("MQTT_USERNAME")
    PASSWORD = os.getenv("MQTT_PASSWORD")

    TOPIC_TEMPERATURA = "sensor_temperatura"
    TOPIC_HUMEDAD = "sensor_humedad"