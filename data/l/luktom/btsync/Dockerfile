# Instructions from the blog post at
http://blog.bittorrent.com/2013/10/22/sync-hacks-deploy-bittorrent-sync-with-
docker/  
FROM ubuntu:14.04  
MAINTAINER Joan Marc Carbo Arnau <jmcarbo@gmail.com>  
RUN apt-get update && apt-get install -y curl  
ADD http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable
/tmp/btsync.tar.gz  
RUN cd /usr/bin && tar -xzvf /tmp/btsync.tar.gz && rm /tmp/btsync.tar.gz  
RUN mkdir -p /btsync/.sync  
RUN mkdir -p /var/run/btsync  
RUN mkdir -p /btsync/.sync  
RUN mkdir -p /data  
EXPOSE 8888  
EXPOSE 55555  
ADD start-btsync /usr/bin/start-btsync  
RUN chmod +x /usr/bin/start-btsync  
  
VOLUME ["/data"]  
ENTRYPOINT ["start-btsync"]  

