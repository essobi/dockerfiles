FROM debian:jessie  
MAINTAINER William Blankenship <william.jblankenship@gmail.com>  
  
RUN apt-get update && \  
apt-get install --force-yes -y \  
autoconf \  
build-essential \  
cmake \  
gcc \  
g++ \  
git \  
libtool \  
make \  
libncurses5-dev \  
openssl \  
libssl-dev \  
libmysqlclient15-dev \  
libmysql++-dev \  
libreadline6-dev \  
zlib1g-dev \  
libbz2-dev \  
libboost-dev \  
libboost-thread-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libzmq-dev  
  
RUN mkdir -p /build/etc/ \  
&& mkdir -p /usr/src/app  
  
ADD worldserver /usr/src/app/worldserver  
ADD worldserver.conf /build/etc/worldserver.conf  
  
WORKDIR /usr/src/app  
  
CMD ["./worldserver"]  

