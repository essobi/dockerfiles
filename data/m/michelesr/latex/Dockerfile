FROM debian:8  
MAINTAINER Michele Sorcinelli "mikefender@cryptolab.net"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y texlive-full && \  
rm -rf /var/lib/apt/lists/*  
  
RUN adduser latex --shell /bin/bash  
RUN mkdir /code/ && chown latex: -R /code/  
  
USER latex  
WORKDIR /code/  

