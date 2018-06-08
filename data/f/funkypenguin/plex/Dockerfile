FROM phusion/baseimage:0.9.16  
MAINTAINER David Young <davidy@funkypenguin.co.nz>  
#Based on the work of needo <needo@superhero.org>  
#Based on the work of Eric Schultz <eric@startuperic.com>  
#Thanks to Tim Haak <tim@haak.co.uk>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# chfn workaround - Known issue within Dockers  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
# Install Plex  
RUN apt-get -q update  
RUN apt-get install -qy gdebi-core wget  
  
# Add a generic htpc user, which we'll reuse for all HTPC containers, and set
UID predictable value (the meaning of 2 lives)  
RUN useradd htpc -u 4242  
  
ADD installplex.sh /  
RUN bash /installplex.sh  
  
VOLUME /config  
VOLUME /data  
  
## Expose ports  
# DLNA  
EXPOSE 1900/udp  
EXPOSE 32469  
# Plex Companion  
EXPOSE 3005  
# Plex for Roku via Plex Companion  
EXPOSE 8324  
# GDM Network Discovery  
EXPOSE 32410/udp  
EXPOSE 32412/udp  
EXPOSE 32413/udp  
EXPOSE 32414/udp  
  
# And the actual Plex Media server  
EXPOSE 32400  
EXPOSE 32401  
# Define /config in the configuration file not using environment variables  
ADD plexmediaserver /etc/default/plexmediaserver  
  
# Add firstrun.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add Plex to runit  
RUN mkdir /etc/service/plex  
ADD plex.sh /etc/service/plex/run  
RUN chmod +x /etc/service/plex/run  

