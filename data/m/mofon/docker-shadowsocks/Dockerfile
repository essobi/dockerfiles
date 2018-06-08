# This dockerfile uses the ubuntu image  
# VERSION 1 - EDITION 1  
# Author: Yourtion  
# Command format: Instruction [arguments / command] ..  
# Base image to use, this must be set as the first line  
FROM ubuntu  
  
MAINTAINER Yourtion <yourtion@gmail.com>  
  
# Commands to update the image  
RUN apt-get -y update && apt-get -y upgrade  
  
# Install shadowsocks-libev  
RUN apt-get install build-essential autoconf libtool libssl-dev git -y  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git
/root/shadowsocks-libev  
RUN cd /root/shadowsocks-libev && git checkout v2.4.4 && ./configure && make  
RUN cd /root/shadowsocks-libev/src && install -c ss-server /usr/bin  
RUN apt-get purge git build-essential autoconf libtool libssl-dev -y && apt-
get autoremove -y && apt-get autoclean -y  
RUN rm -rf /root/shadowsocks-libev  
  
ENV SS_PASSWORD 1234567  
ENV SS_METHOD aes-256-cfb  
  
EXPOSE 8388  
ENTRYPOINT /usr/bin/ss-server -s 0.0.0.0 -p 8338 -k ${SS_PASSWORD} -m
${SS_METHOD}

