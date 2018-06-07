# Build mosquitto from source  
# file is using http://mosquitto.org/files/source/mosquitto-1.2.3.tar.gz  
FROM ubuntu:precise  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
RUN \  
apt-get update ;\  
apt-get upgrade -y ;\  
apt-get install wget build-essential libwrap0-dev libssl-dev python-distutils-
extra -y  
  
RUN \  
mkdir -p /usr/local/src ;\  
cd /usr/local/src ;\  
wget http://mosquitto.org/files/source/mosquitto-1.2.3.tar.gz ;\  
tar xvzf ./mosquitto-1.2.3.tar.gz ;\  
cd /usr/local/src/mosquitto-1.2.3 ;\  
make ;\  
make install  
  
RUN adduser --system --disabled-password --disabled-login mosquitto  
EXPOSE 1883  
CMD ["/usr/local/sbin/mosquitto"]  

