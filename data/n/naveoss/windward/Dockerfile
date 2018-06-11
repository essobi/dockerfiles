FROM ubuntu:14.04  
MAINTAINER Jason Rivers <docker@jasonrivers.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV WINDWARD_SERVER_NAME "Windward Server"  
ENV WINDWARD_SERVER_WORLD "World"  
ENV WINDWARD_SERVER_PORT 5127  
ENV WINDWARD_SERVER_PUBLIC 1  
RUN apt-get update && \  
apt-get install -y \  
mono-runtime \  
libmono2.0-cil \  
wget \  
unzip  
  
RUN mkdir -p /data/windward && \  
useradd -u 1000 -s /bin/bash -d /data/windward windward && \  
chown windward:windward /data/windward  
  
EXPOSE 5127  
ADD windward.sh /usr/local/bin/windward  
  
USER windward  
VOLUME /data/windward  
WORKDIR /data/windward  
  
CMD ["windward"]  

