import datetime
import json

from kafka import KafkaProducer
import config

producer = KafkaProducer(
    bootstrap_servers = [f"{config.KAFKA_IP}:{config.KAFKA_PORT}"],
    value_serializer= lambda  v: json.dumps(v).encode("utf-8")
)

def make_request(cp_id: str):
    date = datetime.datetime.now()

    producer.send("requests", value={
        "driver": config.DRIVER_ID,
        "cp": cp_id,
        "timestamp": date
    })
    producer.flush()

