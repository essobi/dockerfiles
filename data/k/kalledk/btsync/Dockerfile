FROM kalledk/debian:jessie  
  
# Get gosu  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -yq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove \  
ca-certificates \  
wget  
  
# Install btsync  
ADD https://download-cdn.getsync.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz /tmp/btsync.tar.gz  
RUN tar xOzf /tmp/btsync.tar.gz btsync > /usr/bin/btsync \  
&& chmod +x /usr/bin/btsync \  
&& rm /tmp/btsync.tar.gz \  
&& useradd -m -d /btsync btsync \  
&& mkdir -p /btsync/conf \  
&& mkdir -p /btsync/sync  
  
# Add configuration files and entrypoint  
ADD files/* /btsync/  
  
VOLUME ["/btsync/sync", "/btsync/conf"]  
  
EXPOSE 8888 55555  
ENTRYPOINT ["/btsync/btsync.sh"]  
CMD ["sync"]  

