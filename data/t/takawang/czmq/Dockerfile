FROM ubuntu:14.04  
MAINTAINER Taka Wang <taka@cmwang.net>  
  
## Set environment variable  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV ZMQ_VER 3.2.5  
ENV ZMQ_SRC
https://github.com/zeromq/zeromq3-x/releases/download/v$ZMQ_VER/zeromq-$ZMQ_VER.tar.gz  
ENV CZMQ_GIT git://github.com/zeromq/czmq.git  
  
## Install required development packages  
RUN apt-get update  
RUN apt-get install -y git wget build-essential autoconf libtool pkg-config
cmake valgrind  
  
## Install libzmq  
WORKDIR /  
RUN wget $ZMQ_SRC  
RUN tar xvzf zeromq-$ZMQ_VER.tar.gz  
WORKDIR /zeromq-$ZMQ_VER  
RUN ./configure && \  
make && \  
make install && \  
ldconfig  
  
## Install CZMQ  
WORKDIR /  
RUN git clone $CZMQ_GIT  
WORKDIR /czmq  
RUN ./autogen.sh && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
## Clean up  
RUN rm -rf /czmq /zeromq-$ZMQ_VER zeromq-$ZMQ_VER.tar.gz  
WORKDIR /

