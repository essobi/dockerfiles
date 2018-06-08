FROM golang:1.5.1  
MAINTAINER Héctor Ramón Jiménez <hector0193@gmail.com>  
  
# Install generic dependencies  
RUN apt-get update && apt-get install -y build-essential pkg-config cmake
uuid-dev nginx  
  
# Install libsodium  
RUN curl
https://download.libsodium.org/libsodium/releases/libsodium-1.0.5.tar.gz | tar
xvz && \  
cd libsodium-1.0.5 && ./configure && make install && ldconfig && \  
cd / && rm -rf libsodium-1.0.5  
  
# Install ZeroMQ  
RUN curl http://download.zeromq.org/zeromq-4.1.3.tar.gz | tar xvz && \  
cd zeromq-4.1.3 && ./configure && make install && ldconfig && \  
cd / && rm -rf zeromq-4.1.3  

