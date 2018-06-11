FROM debian:jessie  
  
MAINTAINER "yewton" <yewton@gmail.com>  
  
RUN apt-key adv --recv-keys \--keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo deb http://dl.hhvm.com/debian jessie main >
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update && apt-get install -y hhvm ca-certificates --no-install-
recommends && apt-get clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  

