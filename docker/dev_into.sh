#!/bin/bash

xhost +

docker run \
  -it \
  --runtime=nvidia \
  -v /home/autoware/fcos/EE898_PA1_2020_rev2/skeleton:/fcos \
  bongjoonhyun/fcos:latest \
  /bin/bash