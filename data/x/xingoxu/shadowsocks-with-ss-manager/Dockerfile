FROM ubuntu:latest  
MAINTAINER xingoxu <xingoxu@gmail.com>  
RUN apt-get update && \  
apt-get install curl git sudo -y && \  
apt-get install --no-install-recommends autoconf libtool asciidoc zlib1g-dev
libssl-dev libpcre3 libpcre3-dev build-essential libpcre3 asciidoc
libpcre3-dev zlib1g-dev libssl-dev automake libudns-dev libev-dev xmlto build-
essential autoconf libtool libssl-dev libpcre3-dev asciidoc xmlto zlib1g-dev
libev-dev libudns-dev libsodium-dev -y  
  
RUN curl -sSL https://tls.mbed.org/download/mbedtls-2.4.0-gpl.tgz | tar xz \  
&& cd mbedtls-2.4.0 \  
&& make SHARED=1 CFLAGS=-fPIC \  
&& make install  
  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git
/tmp/shadowsocks-libev  
WORKDIR /tmp/shadowsocks-libev  
RUN git submodule update \--init --recursive \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
sudo apt-get install -y nodejs && \  
npm i -g shadowsocks-manager  

