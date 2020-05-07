#!/bin/bash

xhost +

docker run \
  bongjoonhyun/fcos:latest \
  /bin/bash
