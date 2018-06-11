FROM phusion/baseimage  
MAINTAINER cdp181 <chris@smokingcures.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -q  
  
# Install Dependencies  
RUN apt-get install -qy perl libcompress-raw-zlib-perl libhtml-parser-perl
libhttp-cookies-perl liblwpx-paranoidagent-perl libconfig-json-perl libjson-
xs-perl build-essential cpanminus  
  
RUN mkdir /zap2xml  
ADD zap2xml.pl /zap2xml/zap2xml.pl  
  
# Database directory for config  
VOLUME /data  

