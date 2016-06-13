#!/bin/sh
RATE=${RATE:-10}
HITS=${HITS:-500}
if [ -z ${THESERVER+x} ]; then
  docker run --link cycloneserver -e "RATE=$RATE" -e "HITS=$HITS" --name reto3load reto3load
else
  docker run -e "THESERVER=$THESERVER" -e "RATE=$RATE" -e "HITS=$HITS" --name reto3load reto3load
fi
