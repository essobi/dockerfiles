FROM phusion/baseimage:0.9.17  
MAINTAINER Scottst <scott.st@gmail.com>  
LABEL BASEIMAGE="phusion/baseimage:0.9.17"  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"
TERM=xterm  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#########################################  
## RUN INSTALL SCRIPT ##  
#########################################  
ADD * /tmp/  
RUN chmod +x /tmp/install.sh && /tmp/install.sh && rm /tmp/install.sh  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
VOLUME ["/mnt/lftp"]  

