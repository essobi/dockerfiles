FROM linuxserver/baseimage  
MAINTAINER Orkun Sensebat <ihate88@gmail.com>  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Install Deluge  
RUN add-apt-repository ppa:deluge-team/ppa > /dev/null && \  
apt-get update -q && \  
apt-get install -qy deluged deluge-web deluge-console && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add default configuration  
ADD core.conf /core.conf  
  
#Ports and Volumes  
VOLUME /config  
VOLUME /downloads  
# expose port for http  
EXPOSE 8112  
# expose port for deluge daemon  
EXPOSE 58846  
# expose port for incoming torrent data (tcp and udp)  
EXPOSE 58946  
EXPOSE 58946/udp  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run  
RUN chmod -v +x /etc/my_init.d/*.sh  

