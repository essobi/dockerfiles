FROM ubuntu:14.04  
MAINTAINER Mehmet Bora Ezer <bora@qualifylabs.com>  
  
RUN \  
apt-get -y update && \  
apt-get install -y python-dev python-pip libjpeg8-dev zlib1g-dev zip && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install virtualenv==15.0.3  
  
RUN mkdir /python  
VOLUME /python  
WORKDIR /python  

