import datetime
import json

from kafka import KafkaProducer
import config

producer = None
try:
    print(f"[KafkaProducer] Intentando conectar con Kafka ({config.KAFKA_IP}:{config.KAFKA_PORT})...")
    producer = KafkaProducer(
        bootstrap_servers = [f"{config.KAFKA_IP}:{config.KAFKA_PORT}"],
        value_serializer= lambda  v: json.dumps(v).encode("utf-8")
    )
    print("[KafkaProducer] Conectado a Kafka")
except Exception as e:
    print(e)
    producer=None

def make_request(cp_id: str):
    if producer is None:
        print("[KafkaProducer] No se puede establecer conexión con Kafka")
        return
    date = datetime.datetime.now()
    timestamp = date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"[KafkaProducer] Mandando request ({config.DRIVER_ID},{cp_id},{timestamp})")
    producer.send("requests", value={
        "driver": config.DRIVER_ID,
        "cp": cp_id,
        "timestamp": timestamp
    })
    producer.flush()

