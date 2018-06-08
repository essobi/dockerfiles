# Docker container with utorrent  
FROM debian:jessie  
MAINTAINER Andy Taylor "andy0taylor@gmail.com"  
#RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
#  
# Add utorrent dist  
#  
ADD
http://download.ap.bittorrent.com/track/beta/endpoint/utserver/os/linux-x64-debian-7-0
/tmp/utserver.tar.gz  
  
#  
# Add utorrent init script and config.  
#  
ADD utserver.sh /opt/utorrent/utserver.sh  
ADD utserver.conf /opt/utorrent/utserver.conf  
  
#  
# Unpack utorrent and change permissions  
#  
VOLUME ["/utorrent", "/data"]  
EXPOSE 8080 6881 6882 6883 6884 6885 6886  
RUN tar vxzf /tmp/utserver.tar.gz --strip-components 1 -C /opt/utorrent && \  
rm -f /tmp/utserver.tar.gz && \  
chown -R 777 /utorrent && \  
chmod 777 /opt/utorrent/utserver.sh && \  
apt-get update && \  
apt-get install libssl1.0.0  
  
#  
# Start utorrent.  
#  
#WORKDIR /utorrent  
#USER utorrent  
CMD ["/opt/utorrent/utserver.sh"]  
  

