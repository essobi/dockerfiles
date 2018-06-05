# Bittorrent Sync  
#  
# VERSION 0.0.1  
FROM debian:sid  
MAINTAINER Deni Bertovic "deni@kset.org"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y curl  
RUN curl -o /usr/bin/btsync.tar.gz http://download-
lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable  
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz  
  
RUN mkdir -p /btsync/.sync  
  
EXPOSE 8888  
EXPOSE 55555  
CMD ["btsync", "--config", "/btsync/btsync.conf", "--nodaemon"]  

