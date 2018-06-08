# Dockerfile for running a SRCDS server using pufferd.  
FROM ubuntu:16.04  
RUN useradd -m -d /server pufferd  
WORKDIR /server  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y openssl curl tar git \  
lib32gcc1 lib32tinfo5 lib32z1 lib32stdc++6 \  
libtinfo5:i386 libncurses5:i386 libcurl3-gnutls:i386 && \  
rm -rf /var/lib/apt/lists/*  
  
USER pufferd:pufferd  
ENV HOME /server  

