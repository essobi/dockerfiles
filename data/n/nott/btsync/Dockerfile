FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y install tar  
  
ADD https://download-cdn.getsyncapp.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz /usr/bin/btsync.tar.gz  
ADD btsync.conf /etc/btsync.conf  
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz && \  
useradd -d /data -m btsync  
  
EXPOSE 8017 55555  
VOLUME ["/data"]  
  
USER btsync  
  
CMD ["btsync", "--config", "/etc/btsync.conf", "--nodaemon"]

