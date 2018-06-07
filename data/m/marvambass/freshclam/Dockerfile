FROM ubuntu:14.04  
MAINTAINER MarvAmBass  
  
RUN apt-get update; apt-get install -y \  
clamav-freshclam  
  
RUN freshclam  
  
VOLUME /var/lib/clamav  
  
CMD freshclam -d; tail -f /var/log/clamav/freshclam.log  

