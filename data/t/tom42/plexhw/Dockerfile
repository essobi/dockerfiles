# Start with the official image  
FROM tom42/plex  
  
# Install the 1.4 Beta  
RUN curl -J -L -o /tmp/plexmediaserver.deb https://downloads.plex.tv/plex-
media-
server/1.8.1.4140-82ea538ca/plexmediaserver_1.8.1.4140-82ea538ca_amd64.deb  
RUN dpkg -i /tmp/plexmediaserver.deb  
  
# Disable the update functionality, as to not blow away the 1.4 version with
an older 1.3 version  
RUN /bin/rm /etc/cont-init.d/50-plex-update  

