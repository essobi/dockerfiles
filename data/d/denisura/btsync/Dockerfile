FROM ubuntu:14.04  
MAINTAINER Denis Uraganov <github@uraganov.net>  
  
ENV BTSYNC_LISTENING_PORT=55555 \  
BTSYNC_USE_UPNP=false \  
BTSYNC_DOWNLOAD_LIMIT=0 \  
BTSYNC_UPLOAD_LIMIT=0 \  
BTSYNC_SECRET="" \  
BTSYNC_USE_RELAY_SERVER=true \  
BTSYNC_USE_TRACKER=true \  
BTSYNC_USE_DHT=false \  
BTSYNC_SEARCH_LAN=true \  
BTSYNC_USE_SYNC_TRASH=false  
  
RUN apt-get update && apt-get install -y curl \  
&& curl -o /usr/bin/btsync.tar.gz https://download-
cdn.getsyncapp.com/stable/linux-glibc-x64/BitTorrent-Sync_glibc23_x64.tar.gz \  
&& cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz  
  
RUN mkdir -p /btsync/.sync  
RUN mkdir -p /var/run/btsync  
RUN mkdir -p /data  
RUN touch /btsync/secret  
RUN touch /btsync/ro_secret  
RUN touch /btsync/btsync.conf  
  
EXPOSE 55555  
VOLUME ["/data"]  
  
ADD ./docker-entrypoint.sh /docker-entrypoint  
RUN chmod +x /docker-entrypoint  
  
ENTRYPOINT ["/docker-entrypoint"]  
CMD ["btsync-init"]  
  

