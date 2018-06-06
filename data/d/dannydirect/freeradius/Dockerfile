###############################################################################  
# Name: Dockerfile  
# Author: Daniel Middleton <daniel-middleton.com>  
# Description: Dockerfile used to build dannydirect/freeradius  
# Usage: docker build -t dannydirect/freeradius:latest .  
###############################################################################  
  
FROM phusion/baseimage:latest  
  
MAINTAINER Daniel Middleton <daniel-middleton.com>  
  
# Drop entrypoint script in place  
ADD entrypoint.sh /opt/docker-freeradius/entrypoint.sh  
  
# Install dependancies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install build-essential \  
libmysqlclient-dev \  
libperl-dev \  
libssl-dev \  
wget  
  
# Download and extract FreeRADIUS source  
#RUN wget -O /tmp/freeradius.tar.gz \  
# ftp://ftp.freeradius.org/pub/freeradius/freeradius-server-3.0.4.tar.gz && \  
# tar -xzvf /tmp/freeradius.tar.gz -C /tmp  
  
# WTF is this directory?  
#RUN cp /var/www/html/cake2/rd_cake/Setup/Radius/rlm_raw_patch ./freeradius-
server-3.0.4  
  
# Hand over to entrypoint.sh  
ENTRYPOINT ["/opt/docker-freeradius/entrypoint.sh"]  

