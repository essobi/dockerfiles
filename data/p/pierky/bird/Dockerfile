FROM debian:stable  
  
MAINTAINER Pier Carlo Chiodi <pierky@pierky.com>  
  
EXPOSE 179  
RUN apt-get update && apt-get install -y \  
autoconf \  
bison \  
build-essential \  
curl \  
flex \  
libreadline-dev \  
libncurses5-dev \  
m4 \  
unzip  
  
WORKDIR /root  
RUN curl -O -L ftp://bird.network.cz/pub/bird/bird-1.6.4.tar.gz  
RUN tar -xvzf bird-1.6.4.tar.gz  
  
# This directory must be mounted as a local volume with '-v
`pwd`/bird:/etc/bird:rw' docker's command line option.  
# The host's file at `pwd`/bird/bird.conf is used as the configuration file
for BIRD.  
RUN mkdir /etc/bird  
  
RUN cd bird-1.6.4 && \  
autoreconf && \  
./configure && \  
make && \  
make install  
  
RUN cd bird-1.6.4 && \  
autoreconf && \  
./configure --enable-ipv6 && \  
make && \  
make install  
  
CMD bird -c /etc/bird/bird.conf -d  

