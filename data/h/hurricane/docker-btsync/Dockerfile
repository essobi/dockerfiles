# Builds a docker image for btsync  
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
# No ports exposed requried, it's assumed that this container will never be
interlinked with another.  
# ports should be accessed using p flag at runtime.  
VOLUME /config  

