FROM phusion/baseimage:0.9.19  
  
MAINTAINER Lazar Travica <trav326@gmail.com>  
  
# Install `python2.7` and symlink to `python` in path  
RUN apt-get update && \  
apt-get install -y python2.7 && \  
ln -s /usr/bin/python2.7 /usr/bin/python  
  
# Clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

