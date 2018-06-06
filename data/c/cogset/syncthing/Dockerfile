# Syncthing  
# Cogset Open Source Group  
FROM debian:jessie  
  
MAINTAINER Cogset <cogset@funcuter.org>  
  
ENV SYNCTHING_VERSION v0.14.28  
# Install  
RUN buildDeps="wget ca-certificates" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& wget -O syncthing.tar.gz
"https://github.com/syncthing/syncthing/releases/download/$SYNCTHING_VERSION/syncthing-
linux-amd64-$SYNCTHING_VERSION.tar.gz" \  
&& mkdir -p /usr/local/syncthing \  
&& tar -xzf syncthing.tar.gz -C /usr/local/syncthing --strip-components=1 \  
&& rm syncthing.tar.gz \  
&& ln -s /usr/local/syncthing/syncthing /usr/local/bin/syncthing \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
# Configure  
&& mkdir -p /etc/syncthing  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8384 22000  
CMD ["syncthing"]  

