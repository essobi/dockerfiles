# Ryu SDN Framework  
#  
# VERSION 0.0.1  
FROM ubuntu:15.10  
MAINTAINER FUJITA Tomonori <fujita.tomonori@lab.ntt.co.jp>  
  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends python-setuptools python-pip
python-eventlet python-lxml python-msgpack unzip wget iproute2 git  
RUN apt-get install -qy ca-certificates  
  
ENV HOME /root  
WORKDIR /root  
  
RUN git clone https://github.com/osrg/ryu  
RUN cd ryu && python setup.py install  

