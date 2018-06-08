FROM buildpack-deps:jessie  
MAINTAINER Allan Lei <allan.lei@orbweb.com>  
  
  
# dpkg-dev libtool yasm nasm wget curl  
RUN apt-get update && \  
apt-get -y install mingw-w64 && \  
apt-get autoremove -y && \  
apt-get autoclean -y

