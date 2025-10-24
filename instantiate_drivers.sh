#!/bin/bash

if [ -z "$1" ]; then
  echo "Uso: $0 <numero_de_instancias>"
  exit 1
fi


run_in_terminal() {
  CMD=$1
  if command -v gnome-terminal &>/dev/null; then
    gnome-terminal -- bash -c "$CMD; exec bash"
  elif command -v xterm &>/dev/null; then
    xterm -e "$CMD; bash"
  elif command -v konsole &>/dev/null; then
    konsole -e bash -c "$CMD; exec bash"
  elif command -v screen &>/dev/null; then
    screen -dmS multi_instance bash -c "$CMD; exec bash"
    screen -r multi_instance
  else
    echo "No compatible terminal emulator found"
    exit 1
  fi
}

count=$1
for (( i=1; i<=count; i++ ))
do
  driverid=$(printf "driver%03d" "$i")
  port=$((8000+i))

  run_in_terminal "docker run -e PORT=$port -p $port:$port --network ev_network -it --name driver$i ev_driver ev_kafka 9092 $driverid"
done
