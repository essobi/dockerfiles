FROM debian:latest  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y wget ruby && \  
wget -q "https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu" -O /tmp/plex.deb && \  
dpkg --install /tmp/plex.deb && \  
rm -f /tmp/plex.deb && \  
apt-get -fy install && \  
mkdir -p --mode 0755 /Library /media/films /media/music /media/photos
/media/tv /media/videos && \  
apt-get remove -y ruby && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY start.sh /  
  
ENV \  
PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6 \  
PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver \  
PLEX_MEDIA_SERVER_MAX_STACK_SIZE=3000 \  
PLEX_MEDIA_SERVER_TMPDIR=/tmp  
  
VOLUME /Library /media/films /media/music /media/photos /media/tv
/media/videos  
  
EXPOSE 1900/udp 3005/tcp 8324/tcp 32400/tcp 32410/udp 32412/udp 32413/udp
32414/udp 32469/tcp  
  
ENTRYPOINT ["/bin/bash", "/start.sh"]  
CMD ["run"]  

