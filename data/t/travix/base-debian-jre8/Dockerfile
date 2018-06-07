FROM travix/base-debian:latest  
  
MAINTAINER Travix  
  
# install dependencies  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jre-headless \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

