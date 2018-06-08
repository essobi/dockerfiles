FROM phusion/baseimage:0.9.18  
MAINTAINER mezz64 <jtmihalic@gmail.com>  
  
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
#RUN chmod +x /tmp/install.sh && /tmp/install.sh && rm /tmp/install.sh  
RUN chmod +x /tmp/install.sh; sleep 1; /tmp/install.sh; rm /tmp/install.sh  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
VOLUME /config /music  
EXPOSE 3483 3483/udp 9000 9090

