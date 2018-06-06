FROM node:7  
MAINTAINER Martin Hlavac <info@mhlavac.net>  
  
RUN apt-get update -y && \  
apt-get install -y apt-utils autoconf automake build-essential g++ git
libkrb5-dev libsodium-dev libtool make pkg-config unzip uuid-dev wget  
  
WORKDIR /home  
RUN wget http://download.zeromq.org/zeromq-4.1.3.tar.gz && \  
tar xf zeromq-4.1.3.tar.gz && \  
cd zeromq-4.1.3 && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
rm -rf zeromq-4.1.3*  
  
RUN npm install node-gyp -g  
ADD . /app  

