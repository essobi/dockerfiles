FROM phusion/baseimage:latest  
MAINTAINER Mofe Lee <mofe@me.com>  
  
RUN apt-get update && \  
apt-get install -y python-pip  
RUN pip install genpac  
  
# Configure container to run as an executable  
# ENTRYPOINT ["/usr/local/bin/ssserver"]  

