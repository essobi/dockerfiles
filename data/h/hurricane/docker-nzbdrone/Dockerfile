# Builds a docker image for Sonarr  
FROM phusion/baseimage:0.9.16  
MAINTAINER Carlos Hernandez <carlos@techbyte.ca>  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#########################################  
## RUN INSTALL SCRIPT ##  
#########################################  
COPY install.sh /tmp/  
RUN chmod +x /tmp/install.sh && /tmp/install.sh && rm /tmp/install.sh  
  
#########################################  
## VOLUMES ##  
#########################################  
VOLUME /config  
EXPOSE 8083  

