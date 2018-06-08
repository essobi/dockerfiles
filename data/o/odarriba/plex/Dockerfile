FROM odarriba/supervisord:latest  
  
# Install required packages  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y curl  
  
# Create the user 'plex'  
RUN adduser --disabled-password plex  
  
WORKDIR /tmp  
  
# Download and install latest version of Plex  
RUN DOWNLOAD_URL=`curl -Ls https://plex.tv/api/downloads/1.json | grep -o
'[^"'"'"']*amd64.deb' | grep -v binaries` && \  
echo $DOWNLOAD_URL && \  
curl -L $DOWNLOAD_URL -o plexmediaserver.deb && \  
dpkg -i plexmediaserver.deb && \  
rm -f plexmediaserver.deb  
  
# Create the writable config directory in case the volume isn't mounted  
RUN mkdir /config && \  
chown -R plex:plex /config && \  
chown -R plex:plex /media  
  
# Configure autostart using supervisord  
ADD config/plex.conf /etc/supervisor/conf.d/plex.conf  
  
# Volumes available  
VOLUME /config  
VOLUME /media  
  
# Port exposed  
EXPOSE 32400  
# Environment variables to configure PMS  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS 6  
ENV PLEX_MEDIA_SERVER_MAX_STACK_SIZE 3000  
ENV PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR /config  
ENV PLEX_MEDIA_SERVER_HOME /usr/lib/plexmediaserver  
ENV LD_LIBRARY_PATH /usr/lib/plexmediaserver  
ENV TMPDIR /tmp  
  
WORKDIR /usr/lib/plexmediaserver  

