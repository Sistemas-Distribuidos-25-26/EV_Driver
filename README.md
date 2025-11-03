# EV_Driver

## Método de uso

Utilizando Docker:

```commandline
docker build -t ev_driver ./
docker run --network <network> --name <name> -e PORT=<port> -p <port>:<port> -it ev_driver <kafka_ip> <kafka_port> <driver_id>
```

O con scripts de automatización:

```commandline
docker build -t ev_driver ./
./instantiate_drivers.sh <instances>
```