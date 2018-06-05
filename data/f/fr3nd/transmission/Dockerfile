FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
ENV TRANSMISSION_VERSION 2.92  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
build-essential \  
intltool \  
libcurl4-openssl-dev \  
libevent-dev \  
libglib2.0-dev \  
libminiupnpc-dev \  
libminiupnpc-dev \  
libssl-dev \  
libtool \  
pkg-config \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
RUN mkdir -p /usr/src/transmission  
WORKDIR /usr/src/transmission  
RUN curl -L
https://transmission.cachefly.net/transmission-${TRANSMISSION_VERSION}.tar.xz
| \  
tar xvJ --strip-components=1 && \  
./configure --enable-daemon --enable-cli --prefix=/usr && \  
make && \  
make install && \  
rm -rf /usr/src/transmission  
WORKDIR /  
  
EXPOSE 9091 51413 51413/udp  

