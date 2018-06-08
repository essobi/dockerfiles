FROM ubuntu:14.04  
MAINTAINER david.jo <thristydavidjo@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y python  
RUN apt-get install -y python-pip python-dev python-virtualenv  
ENV
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp27-none-
linux_x86_64.whl  
RUN pip install --upgrade $TF_BINARY_URL  
COPY data/ /data  
  
VOLUME ["/data"]  
  

