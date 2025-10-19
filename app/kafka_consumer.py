from pydoc import describe

from kafka import KafkaConsumer
import config
from json import loads
import time

consumer = None
try:
    consumer = KafkaConsumer(
        "orders", "notifications",
        bootstrap_servers=[f"{config.KAFKA_IP}:{config.KAFKA_PORT}"],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda m: loads(m.decode('utf-8'))
    )
except:
    consumer = None

def receive_notifications():
    while True:
        if not consumer:
            print("[KafkaConsumer] Error al conectar con Kafka")
            time.sleep(5)
            continue
        for message in consumer:
            if message.topic == "notifications":
                data = message.value
                notiftype = data.get("type")
                target = data.get("target")
                destination = data.get("destination")
                if destination != config.DRIVER_ID:
                    continue
                config.error_text = f"{notiftype}: {target}"
