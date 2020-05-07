FROM nvidia/cuda:10.1-base-ubuntu18.04
MAINTAINER bongjoon.hyun@gmail.com

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3 python3-pip

# PyTorch
RUN pip3 install torch torchvision

# OpenCV
RUN pip3 install opencv-python

# pycocotools
RUN pip3 install cython
RUN pip3 install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

# detectron2
RUN git clone https://github.com/facebookresearch/detectron2.git
WORKDIR detectron2
RUN python3 setup.py build develop
