FROM debian:stable-slim  
  
ENV LANG C.UTF-8 LC_ALL C.UTF-8  
ARG DEBIAN_FRONTEND="noninteractive"  
RUN apt-get update -y &&\  
apt-get install -y \  
apt-transport-https \  
curl \  
gnupg2 \  
udev \  
jq &&\  
useradd --system --uid 797 --create-home --shell /usr/sbin/nologin plex &&\  
curl $(curl -s -L https://plex.tv/api/downloads/1.json | jq -r
'.computer.Linux.releases | .[0] | .url') -o plex.deb &&\  
dpkg -i plex.deb &&\  
apt-get clean &&\  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
VOLUME /Movies /TV /config  
  
ENV PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/config  
  
EXPOSE 32400  
USER plex  
  
WORKDIR /usr/lib/plexmediaserver  
  
CMD [ "/usr/lib/plexmediaserver/Plex Media Server" ]

