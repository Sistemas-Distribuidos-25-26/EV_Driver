import time
import config
from kafka_producer import make_request

def initiate_testing():
    try:
        requests = open("tests.txt", "r").read().split('\n')
        for cp in requests:
            while not config.FINISHED:
                time.sleep(1)
            make_request(cp)
            time.sleep(4)

    except IOError:
        return