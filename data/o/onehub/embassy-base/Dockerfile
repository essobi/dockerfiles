FROM phusion/passenger-ruby21:0.9.15  
MAINTAINER Leigh Caplan <lcaplan@onehub.com>  
  
# Set correct environment variables  
ENV HOME /root  
  
# Install C Build Toolchain for Attache  
# Install curl tar gzip to download Applications  
# Install Ruby Runtime for Ambassador  
RUN apt-get update && apt-get install -y automake check curl gzip libtool
libstdc++6-4.8-dbg uuid-dev pkg-config libmsgpack-dev build-essential  
  
# Download ZeroMQ & CZMQ  
RUN mkdir /zeromq  
RUN curl -s -S http://download.zeromq.org/zeromq-4.0.4.tar.gz -o
/zeromq/zeromq-4.0.4.tar.gz  
RUN curl -s -S http://download.zeromq.org/czmq-2.2.0.tar.gz -o
/zeromq/czmq-2.2.0.tar.gz  
  
# Unpack ZeroMQ & CZMQ  
RUN tar -zxvf /zeromq/zeromq-4.0.4.tar.gz -C /zeromq  
RUN tar -zxvf /zeromq/czmq-2.2.0.tar.gz -C /zeromq  
  
# Build and Install ZeroMQ  
WORKDIR /zeromq/zeromq-4.0.4  
RUN ./configure && make && make install  
  
# Build and Install CZMQ  
WORKDIR /zeromq/czmq-2.2.0  
RUN ./configure && make && make install  
  
# Update libraries  
RUN ldconfig -v  
  
# Reset WORKDIR  
WORKDIR /  
  
# Install Bundler  
RUN gem install bundler  
  
# Build out cache and working directories.  
RUN mkdir -p /tmp/feeds  
RUN mkdir -p /sync/data  
RUN mkdir -p /sync/workspace  

