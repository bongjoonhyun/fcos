#!/bin/bash

#docker build -t bongjoonhyun/fcos_gpu -f gpu.dockerfile .
docker build -t bongjoonhyun/fcos_cpu -f cpu.dockerfile .

#docker push bongjoonhyun/fcos_gpu
#docker push bongjoonhyun/fcos_cpu
