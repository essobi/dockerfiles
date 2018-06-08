FROM ubuntu:14.04  
MAINTAINER Wataru MIYAGUNI <gonngo@gmail.com>  
  
# Install dependency packages  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install git curl wget telnet ntp  
  
# Timezone setting  
RUN echo 'Asia/Tokyo' > /etc/timezone  
RUN date  
RUN dpkg-reconfigure --frontend noninteractive tzdata  

