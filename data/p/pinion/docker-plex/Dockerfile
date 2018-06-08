FROM phusion/baseimage:0.9.11  
MAINTAINER pinion <pinion@gmail.com>  
#Thanks to Eric Schultz <eric@startuperic.com>  
#Thanks to Tim Haak <tim@haak.co.uk>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN apt-get update -qq  
  
# Install PMS dependencies  
RUN apt-get install -qy --force-yes avahi-daemon avahi-utils  
  
# Add and install the latest PMS release for Plex Pass  
ADD https://downloads.plex.tv/plex-media-
server/0.9.11.1.678-c48ffd2/plexmediaserver_0.9.11.1.678-c48ffd2_amd64.deb
plex.deb  
RUN dpkg -i plex.deb  
  
VOLUME /config  
VOLUME /data  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 32400  
ENTRYPOINT ["/start.sh"]  

