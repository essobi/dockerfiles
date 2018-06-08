FROM debian:jessie  
  
RUN groupadd -g 821 docker  
RUN useradd -u 821 -g 821 docker  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get clean \  
&& mkdir /opt/sync \  
&& curl https://download-cdn.getsyncapp.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz | tar -zx -C /opt/sync \  
&& mkdir /config \  
&& chown docker:docker /config \  
&& mkdir /data \  
&& chown docker:docker -R /data \  
&& chown docker:docker -R /opt/sync  
  
VOLUME /config  
  
USER docker  
CMD ["/opt/sync/btsync", "--config", "/config/btsync.conf", "--nodaemon"]  

