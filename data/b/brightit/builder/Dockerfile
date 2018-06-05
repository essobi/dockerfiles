FROM node:6.9  
MAINTAINER Bright IT <support-docker@bright-it.com>  
  
RUN echo deb http://ftp.debian.org/debian jessie-backports main >>
/etc/apt/sources.list  
RUN apt-get update && apt-get -t jessie-backports install -y --no-install-
recommends \  
openjdk-7-jdk \  
maven \  
scala \  
&& rm -rf /var/lib/apt/lists/*  

