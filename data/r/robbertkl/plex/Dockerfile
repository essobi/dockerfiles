FROM robbertkl/base-s6  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
# Install latest plexmediaserver from plex.tv  
RUN DOWNLOAD_URL=`curl -sSL "https://plex.tv/api/downloads/1.json" | python -c
'import sys,json; data=json.loads(sys.stdin.read()); print [release["url"] for
release in data["computer"]["Linux"]["releases"] if "Ubuntu 64" in
release["label"]][0];'` \  
&& curl -sSL "${DOWNLOAD_URL}" -o plexmediaserver.deb \  
&& touch /bin/start \  
&& chmod +x /bin/start \  
&& dpkg -i plexmediaserver.deb \  
&& rm -f /bin/start plexmediaserver.deb  
  
# Configure services  
COPY etc /etc  
  
# Setup logging and persistent storage  
RUN mkdir -p "/config/Plex Media Server/Logs" \  
&& touch "/config/Plex Media Server/Logs/Plex Media Server.log" \  
&& echo "/config/Plex Media Server/Logs/Plex Media Server.log" >>
/etc/services.d/logs/stdout  
COPY [ "Preferences.xml", "/config/Plex Media Server/" ]  
VOLUME /config  
  
# Environment variables  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6 \  
PLEX_MEDIA_SERVER_MAX_STACK_SIZE=8192 \  
PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/config \  
PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver \  
LD_LIBRARY_PATH=/usr/lib/plexmediaserver \  
TMPDIR=/tmp  
  
# Expose  
EXPOSE 32400  

