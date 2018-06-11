FROM akohlbecker/base:latest  
  
# Install required packages  
RUN apt-get update && \  
apt-get install -y curl jq && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Create plex user (media group needs to be "plex" for the install to work)  
RUN groupadd --gid 2000 plex && \  
useradd --uid 2005 --gid 2000 --create-home plex && \  
mkdir /data && \  
chown -R plex:plex /data  
  
# Hack to avoid install to fail due to upstart not being installed.  
# We won't use upstart anyway.  
RUN DOWNLOAD_VERSION=`curl --silent https://plex.tv/api/downloads/1.json | jq
--raw-output ".computer.Linux.version"` && \  
echo "https://downloads.plex.tv/plex-media-
server/$DOWNLOAD_VERSION/plexmediaserver_${DOWNLOAD_VERSION}_amd64.deb" && \  
curl -L "https://downloads.plex.tv/plex-media-
server/$DOWNLOAD_VERSION/plexmediaserver_${DOWNLOAD_VERSION}_amd64.deb" -o
plexmediaserver.deb && \  
dpkg -i plexmediaserver.deb && \  
rm -f plexmediaserver.deb  
  
# The most important port to make sure your firewall allows is the main TCP
port the Plex Media Server uses for communication:  
# TCP: 32400 (for access to the Plex Media Server) [required]  
# The following ports are also used for different services:  
# UDP: 1900 (for access to the Plex DLNA Server)  
# TCP: 3005 (for controlling Plex Home Theater via Plex Companion)  
# UDP: 5353 (for older Bonjour/Avahi network discovery)  
# TCP: 8324 (for controlling Plex for Roku via Plex Companion)  
# UDP: 32410, 32412, 32413, 32414 (for current GDM network discovery)  
# TCP: 32469 (for access to the Plex DLNA Server)  
EXPOSE 32400/tcp 1900/udp 3005/tcp 5353/udp 8324/tcp 32410/udp 32412/udp
32413/udp 32414/udp 32469/tcp  
  
# location of configuration, default is  
# "${HOME}/Library/Application Support"  
RUN echo "export PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/data" >>
/etc/default/plexmediaserver  
VOLUME /data  
  
USER plex  
CMD test -f /data/Plex\ Media\ Server/plexmediaserver.pid && rm -f /data/Plex\
Media\ Server/plexmediaserver.pid; \  
/usr/sbin/start_pms  

