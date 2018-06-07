FROM debian:jessie  
MAINTAINER Cody Mize <me@codymize.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DISPLAY unix$DISPLAY  
RUN apt-get update && \  
apt-get -y install gnomint && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/bin/gnomint"]  

