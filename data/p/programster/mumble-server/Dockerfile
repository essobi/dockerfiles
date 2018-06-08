# Builds a basic docker image that can run Mumble  
#  
# Author: Isaac Bythewood  
# Edited by: Programster [ http://programster.blogspot.co.uk/ ]  
# Updated: Jan 19th 2014  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
# Base system is the LTS version of Ubuntu.  
from ubuntu:12.04  
MAINTAINER programster  
  
# Make sure we don't get notifications we can't answer during building.  
env DEBIAN_FRONTEND noninteractive  
  
# Add our entire folder so that users can use the container to re-build their
own from scratch  
add mumble /home/mumble  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
# An annoying error message keeps appearing unless you do this.  
run dpkg-divert --local \--rename --add /sbin/initctl  
run ln -s /bin/true /sbin/initctl  
  
# Download and install everything from the repos.  
run apt-get update && apt-get dist-upgrade -y  
run apt-get install mumble-server supervisor pwgen -y  
  
# Load in all of our config files.  
RUN cp -f /home/mumble/supervisor/supervisord.conf
/etc/supervisor/supervisord.conf  
RUN cp -f /home/mumble/supervisor/conf.d/murmurd.conf
/etc/supervisor/conf.d/murmurd.conf  
RUN cp -f /home/mumble/mumble/mumble-server.ini /etc/mumble-server.ini  
  
# Fix all permissions  
run chmod +x /home/mumble/startup.sh  
  
# 80 is for nginx web, /data contains static files and database /start runs
it.  
expose 64738  
volume ["/data"]  
cmd ["/home/mumble/startup.sh"]  
  

