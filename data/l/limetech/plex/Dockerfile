FROM phusion/baseimage:0.9.22  
MAINTAINER Lime Technology <erics@lime-technology.com>  
#Based on the work of needo <needo@superhero.org>  
#Based on the work of Eric Schultz <eric@startuperic.com>  
#Thanks to Tim Haak <tim@haak.co.uk>  
# Set correct environment variables  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" LC_ALL="C.UTF-8"
LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
# Install Plex  
ADD install.sh /  
RUN bash /install.sh  
  
# Define /config in the configuration file not using environment variables  
ADD plexmediaserver /etc/default/plexmediaserver  
  
VOLUME /config  
VOLUME /data  
  
EXPOSE 1900/udp 32469 3005 8324 32410/udp 32412/udp 32413/udp 32414/udp 32400  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]

