FROM ubuntu:xenial  
  
LABEL maintainer="Trent Foxingworth"  
  
# Install dependencies  
RUN \  
apt update && \  
apt install -y udev curl  
  
# Install PMS  
RUN \  
curl -L "https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu" -o ~/pms.deb && \  
dpkg -i ~/pms.deb && \  
rm ~/pms.deb  
  
# Mount points  
RUN \  
mkdir -p ~/Library/Application\ Support/Plex\ Media\ Server/ && \  
ln -s ~/Library/Application\ Support/Plex\ Media\ Server/ /config  
VOLUME /config /media  
  
# Start PMS  
CMD LD_LIBRARY_PATH=/usr/lib/plexmediaserver /usr/lib/plexmediaserver/Plex\
Media\ Server  
  
# Ports  
EXPOSE 32400  
# Mark as unhealthy if PMS stops responding  
HEALTHCHECK \--interval=5m --timeout=5s \  
CMD curl -f http://localhost:32400/ || exit 1

