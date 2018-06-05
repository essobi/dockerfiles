#  
# Tested-Transcoder Docker  
# Based on the original tested-transcoder  
# Please visit tested at www.tested.com  
# or directly to the transcoder project  
# https://github.com/andymccurdy/tested-transcoder  
#  
# Modified by: Chris Andersen  
# On : 04/01/2016  
#  
# My first attempt to make a docker, so it is likely broken  
# Pull in ubuntu:latest image  
# Declare Maintainer  
FROM phusion/baseimage:latest  
MAINTAINER Chris Andersen  
RUN apt-get install -y software-properties-common  
RUN mkdir -p /etc/my_init.d  
COPY init/Startup.sh /etc/my_init.d/  
RUN chmod +x /etc/my_init.d/Startup.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
VOLUME ["/media/transcoder", "/config"]  
  

