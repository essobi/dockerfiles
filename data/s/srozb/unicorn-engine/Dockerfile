FROM ubuntu:15.10  
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>  
  
# Tunables  
ENV VER 0.9  
# Prepare deps  
RUN apt-get update -y && apt-get install -y python-dev libglib2.0-dev wget
less vim  
  
# Get the Unicorn-Engine sources  
WORKDIR /usr/src  
RUN wget https://github.com/unicorn-engine/unicorn/archive/$VER.tar.gz && tar
-xzf $VER.tar.gz  
  
# Build the Unicorn-Engine  
WORKDIR /usr/src/unicorn-$VER  
RUN ./make.sh && ./make.sh install  
  
# Build the Python bindings  
WORKDIR /usr/src/unicorn-$VER/bindings/python  
RUN make install  
  
# Cleanup  
RUN rm -rf /usr/src/*  
  
WORKDIR /root  

