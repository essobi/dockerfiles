# Start with Ubuntu base image  
FROM halo9pan/cuda-scipy  
MAINTAINER Halo9Pan <halo9pan@gmail.com>  
  
RUN pip install -U theano && pip install -U matplotlib && pip list  
  
ENV
THEANO_FLAGS='device=gpu,floatX=float32,nvcc.root=/opt/CUDA,nvcc.fastmath=True'  

