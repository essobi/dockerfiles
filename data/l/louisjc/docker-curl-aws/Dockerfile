FROM ubuntu:trusty  
MAINTAINER louisjc  
  
RUN apt-get update \  
&& apt-get install -y curl python-pip \  
&& pip install awscli \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

