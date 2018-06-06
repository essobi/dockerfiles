FROM debian:wheezy  
MAINTAINER Chris Hardekopf <chrish@basis.com>  
  
# Download the current btsync  
ADD https://download-cdn.getsync.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz /opt/  
# Install it in opt  
RUN cd /opt/ && \  
tar xzf BitTorrent-Sync_x64.tar.gz && \  
rm BitTorrent-Sync_x64.tar.gz  
  
# Sync volume  
VOLUME [ "/opt/.sync" ]  
  
# Set the working directory  
WORKDIR /opt/  
  
# Set up the entrypoint  
ENTRYPOINT [ "/opt/btsync", "--nodaemon" ]  
# Default the configuration location  
CMD [ "--config", "/opt/btsync.conf" ]  
  

