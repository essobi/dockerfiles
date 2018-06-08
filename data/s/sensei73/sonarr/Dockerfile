FROM phusion/baseimage:latest  
MAINTAINER sensei73 <sensei73@gmail.com>  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#########################################  
## FILES, SERVICES AND CONFIGURATION ##  
#########################################  
# Add services to runit  
ADD nzbdrone.sh /etc/service/nzbdrone/run  
  
RUN chmod +x /etc/service/*/run /etc/my_init.d/*  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
  
VOLUME /config /downloads /tv  
EXPOSE 8989  
#########################################  
## RUN INSTALL SCRIPT ##  
#########################################  
  
ADD install.sh /tmp/  
RUN chmod +x /tmp/install.sh && /tmp/install.sh && rm /tmp/install.sh  

