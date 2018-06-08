# Builds a docker image for ddclient  
FROM phusion/baseimage:0.9.18  
MAINTAINER Mace Capri <macecapri@gmail.com>  
  
  
###############################################  
## ENVIRONMENTAL CONFIG ##  
###############################################  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
###############################################  
## INSTALL ENVIORMENT AND SOFTWARE ##  
###############################################  
COPY install.sh /tmp/  
RUN chmod +x /tmp/install.sh && sleep 1 && /tmp/install.sh && rm
/tmp/install.sh  
  
  
###############################################  
## PORTS AND VOLUMES ##  
###############################################  
  
EXPOSE 8082  
EXPOSE 6881  
  
VOLUME /config  
VOLUME /downloads  
VOLUME /watched  

