FROM phusion/baseimage  
MAINTAINER Tomasz Jonik <tomasz@hurricane.works>  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
# Install nodejs + npm  
RUN apt-get update \  
&& apt-get install -y g++ make python nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

