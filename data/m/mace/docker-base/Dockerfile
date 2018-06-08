# Builds a docker base image with supervisor  
FROM ubuntu:15.10  
MAINTAINER mace <macecapri@gmail.com>  
  
  
###############################################  
## ENVIRONMENTAL CONFIG ##  
###############################################  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
  
  
###############################################  
## INTALL ENVIORMENT ##  
###############################################  
COPY install.sh /tmp/  
RUN chmod +x /tmp/install.sh && sleep 1 && /tmp/install.sh && rm
/tmp/install.sh && /startup/01_startup.sh  
  
  
  

