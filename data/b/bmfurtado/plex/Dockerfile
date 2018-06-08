FROM ubuntu:trusty  
MAINTAINER Bruno Furtado <bmfurtado@geekoo.eu>  
  
ENV PLEX_MEDIA_SERVER_PIDFILE=/var/run/plexmediaserver/plexmediaserver.pid  
  
RUN apt-get update && \  
apt-get install -qy --force-yes curl && \  
curl -o /tmp/package.deb https://downloads.plex.tv/plex-media-
server/0.9.15.2.1663-7efd046/plexmediaserver_0.9.15.2.1663-7efd046_amd64.deb
&& \  
dpkg -i /tmp/package.deb && \  
mkdir -p /var/run/plexmediaserver && \  
chown plex: /var/run/plexmediaserver && \  
ln -s /var/lib/plexmediaserver /plex-config  
  
ADD start-plex /usr/local/bin/start-plex  
  
RUN chmod 755 /usr/local/bin/start-plex  
  
VOLUME /plex-config  
VOLUME /plex-data  
  
EXPOSE 32400  
USER plex  
  
CMD ["/usr/local/bin/start-plex"]  

