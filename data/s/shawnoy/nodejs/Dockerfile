FROM alpine:3.6  
LABEL maintainer "shawnoy@outlook.com"  
  
RUN apk --no-cache add libressl g++ yarn && \  
apk --no-cache \  
\--virtual build-essential \  
add \  
python \  
make \  
linux-headers \  
clang  
  
ARG WORKDIR=/tmp  
ARG NODE_VERSION="8.9.1"  
RUN cd $WORKDIR && \  
wget https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz && \  
tar zxf node-v$NODE_VERSION.tar.gz && \  
cd node-v$NODE_VERSION && \  
./configure && \  
make -j "$(getconf _NPROCESSORS_ONLN)" && \  
make install && \  
rm -rf $WORKDIR/* && \  
apk del build-essential  

