FROM ubuntu:latest  
MAINTAINER Hammy223  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update package list and install wget  
RUN apt-get update && apt-get install -y wget  
  
# Get perforce packages  
RUN wget -q http://package.perforce.com/perforce.pubkey -O - | apt-key add -
&& \  
echo 'deb http://package.perforce.com/apt/ubuntu trusty release' >
/etc/apt/sources.list.d/perforce.sources.list && \  
apt-get update  

