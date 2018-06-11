FROM debian:jessie  
MAINTAINER Tom Davidson <tom@tomdavidson.org>  
  
RUN apt-get update && apt-get -y install \  
curl \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

