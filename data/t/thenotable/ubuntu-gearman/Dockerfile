FROM ubuntu:14.04  
MAINTAINER Daniel Kennedy dkennedy4@gmail.com  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
binutils-doc \  
software-properties-common \  
libboost-all-dev \  
gperf \  
libevent-dev \  
uuid-dev \  
wget \  
libmysqlclient-dev \  
libmemcached-dev \  
libsqlite3-dev \  
libpq-dev \  
libdrizzle-dev  
  
# Install Gearman Job Server  
RUN wget
https://launchpad.net/gearmand/1.2/1.1.12/+download/gearmand-1.1.12.tar.gz  
RUN tar xzf gearmand-1.1.12.tar.gz  
RUN cd gearmand-1.1.12 && ./configure && make && make install  
RUN mkdir /usr/local/var/  
RUN mkdir /usr/local/var/log/  
RUN touch /usr/local/var/log/gearmand.log

