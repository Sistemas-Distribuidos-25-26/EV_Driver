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
            data = message.value
            if message.topic == "notifications":
                notiftype = data.get("type")
                target = data.get("target")
                destination = data.get("destination")
                if destination != config.DRIVER_ID:
                    continue
                config.error_text = f"{notiftype}: {target}"
                config.notification_text = None
            else:
                ordertype = data.get("type")
                source = data.get("from")
                destination = data.get("to")
                if destination != config.DRIVER_ID:
                    continue

                if ordertype == "prepare":
                    config.error_text = None
                    config.notification_text = "¡Todo listo! Ya puedes iniciar la carga."
