FROM ubuntu  
  
RUN mkdir -p /sync/files  
WORKDIR /sync  
RUN apt-get update && apt-get -y install curl wget gettext  
  
RUN cd $(mktemp -d); curl "https://download-
cdn.getsync.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz" | tar xz; \  
cp btsync /sync  
  
ADD btsync.conf.tmpl /sync/btsync.conf.tmpl  
  
ENV BT_SECRET CHANGEME  
ENV BT_NAME Server  
ENV BT_PORT 9999  
VOLUME /sync/files  
  
CMD cat btsync.conf.tmpl | envsubst > btsync.conf; /sync/btsync --nodaemon
--log \--config /sync/btsync.conf  

