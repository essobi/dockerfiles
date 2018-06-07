#!/usr/bin/env docker  
  
FROM mychiara/base:1.0.1  
MAINTAINER Andy Ruck mychiara+docker __at__ gmail.com  
  
RUN apt-get update && \  
usermod -u 1000 www-data && \  
usermod -u 1002 www-data && \  
adduser www-data www-data --no-create-home && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

