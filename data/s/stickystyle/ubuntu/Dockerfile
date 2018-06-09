FROM ubuntu:14.04  
MAINTAINER Ryan Parrish <ryan@stickystyle.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG en_US.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update && \  
apt-get -y --no-install-recommends install dnsutils  
  
ADD aptproxy.sh /usr/local/bin/  
ADD 31autoproxy /etc/apt/apt.conf.d/  
  
RUN apt-get -y --no-install-recommends install \  
software-properties-common \  
wget \  
curl \  
supervisor  
  
RUN apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  

