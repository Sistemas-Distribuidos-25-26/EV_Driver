from gui import run
from sys import argv
import config
import threading
from kafka_consumer import receive_notifications

if len(argv) < 4:
    print("Uso: EV_Driver [IP_Kafka] [Puerto_Kafka] [Identificador]")
    exit(-1)

config.KAFKA_IP = argv[1]
config.KAFKA_PORT = argv[2]
config.DRIVER_ID = argv[3]

notification_thread = threading.Thread(target=receive_notifications, daemon=True)
notification_thread.start()

run()