#!/bin/bash

xhost +

docker run \
  -it \
  --ipc=host \
  -v ~/fcos/EE898_PA1_2020_rev2/skeleton:/fcos \
  -v ~/fcos/visualizer:/visualizer \
  bongjoonhyun/fcos_cpu:latest \
  /bin/bash
