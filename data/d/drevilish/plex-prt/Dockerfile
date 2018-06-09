FROM linuxserver/baseimage  
MAINTAINER DrEVILish  
  
ENV BASE_APTLIST="dbus avahi-daemon nfs-common git nodejs"  
# Install Plex  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -q update && \  
apt-get install $BASE_APTLIST -qy && \  
curl -L 'https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu' -o /tmp/plexmediaserver.deb && \  
dpkg -i /tmp/plexmediaserver.deb && rm -f /tmp/plexmediaserver.deb && \  
cd /tmp && \  
git clone http://github.com/drevilish/node-prt && \  
npm install -g socket.io-client && \  
mv /usr/lib/plexmediaserver/Resources/Plex\ New\ Transcoder
/usr/lib/plexmediaserver/Resources/plex_transcoder_original && \  
cp /tmp/node-prt/prt-trigger/index.js /usr/lib/plexmediaserver/Resources/Plex\
New\ Transcoder && \  
cp -R /tmp/node-prt/prt-server /app/prt-server && \  
cd /app/prt-server && \  
npm install && \  
chown -R abc:abc /app/prt-server && \  
rm -rf /tmp/node-prt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#Adding Custom files  
COPY init/ /etc/my_init.d/  
COPY services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  
# Define /config in the configuration file not using environment variables  
COPY plexmediaserver /defaults/plexmediaserver  
  
#Mappings and ports  
VOLUME ["/config", "/transcode"]  
EXPOSE 32400 32400/udp 32469 32469/udp 5353/udp 1900/udp 8594  

