import json
import paho.mqtt.client as mqtt
from config import Config

class MQTTClient:
    def __init__(self, client_id):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)
        self.client.username_pw_set(Config.USERNAME, Config.PASSWORD)
        self.client.tls_set()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        """Callback a la hora de conectar al broker"""
        if rc == 0:
            print("Conectado al broker")
        else:
            print(f"Error de conexión: {rc}")

    def on_message(self, client, userdata, msg):
        """Callback a la hora de recibir un mensaje"""
        datos = json.loads(msg.payload.decode())
        print(f"\nMensaje {datos['mensaje']}")
        if "temperatura" in datos:
            print(f"Temperatura: {datos['temperatura']}°C")
        if "humedad" in datos:
            print(f"Humedad: {datos['humedad']}%")
        print(f"Timestamp: {datos['timestamp']}")

    def on_publish(self, client, userdata, mid):
        """Callback a la hora de publicar un mensaje"""
        pass

    def connect(self):
        """Conecta al publisher/subscriber al broker"""
        self.client.connect(Config.BROKER, Config.PORT, 60)
        self.client.loop_start()

    def disconnect(self):
        """Desconecta al publisher/subscriber al broker"""
        print('Desconectando del broker')
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, topic, message):
        """Publica un mensaje en un topico"""
        self.client.publish(topic, message)

    def subscribe(self, topic):
        """Subscribe el cliente a un topico"""
        self.client.subscribe(topic)