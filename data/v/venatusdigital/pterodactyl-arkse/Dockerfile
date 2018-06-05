FROM ubuntu:latest  
  
MAINTAINER Venatus Digital  
  
RUN dpkg --add-architecture i386 && \  
apt update && \  
apt upgrade -y && \  
apt install -y dos2unix libcompress-raw-zlib-perl wget tar curl gcc g++
lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 libtinfo5:i386 libncurses5:i386
libcurl3-gnutls:i386 && \  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

