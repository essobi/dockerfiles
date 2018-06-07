############################################################  
# Deluge Daemon with Web interface  
# Based on Debian  
############################################################  
  
#Set the base image to Debian  
FROM debian:8  
  
#File Author / Maintainer  
MAINTAINER Deon Cooper  
  
#Update the repository sources list  
RUN apt-get update  
  
################## BEGIN INSTALLATION ######################  
  
# Install Deluge and Deluge Web components  
RUN apt-get install -y deluged python-mako deluge-web  
  
# Expose the default ports  
# Web interface  
EXPOSE 8112  
  
# Remote Client interface  
EXPOSE 58846  
  
# Setup Data for persistance  
RUN mkdir /data  
RUN mkdir /config  
RUN ln -s /config /root/.config  
  
#Set default container command  
ENTRYPOINT /usr/bin/deluge-web  

