FROM takawang/golang:x86  
MAINTAINER Taka Wang <taka@cmwang.net>  
  
## Set environment variable  
ENV DEBIAN_FRONTEND noninteractive  
ENV ZMQ_VER 3.2.5  
ENV ZMQ_SRC
https://github.com/zeromq/zeromq3-x/releases/download/v$ZMQ_VER/zeromq-$ZMQ_VER.tar.gz  
  
RUN apt-get update && apt-get install -y pkg-config  
  
## Install libzmq  
WORKDIR /  
RUN wget $ZMQ_SRC && \  
tar xvzf zeromq-$ZMQ_VER.tar.gz && \  
rm zeromq-$ZMQ_VER.tar.gz  
  
# build libzmq  
WORKDIR /zeromq-$ZMQ_VER  
RUN ./configure && \  
make && \  
make install && \  
ldconfig  
  
# clean  
WORKDIR /  
RUN rm -rf /zeromq-$ZMQ_VER  
  
WORKDIR /go  
RUN go get github.com/takawang/zmq3

