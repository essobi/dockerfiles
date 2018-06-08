FROM ubuntu:16.04  
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>  
  
# Set version  
ARG PLEX_VERSION=1.5.5.3634-995f1dead  
  
# Plex environment variables  
ENV PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR
/var/lib/plexmediaserver/Library/Application Support  
ENV PLEX_MEDIA_SERVER_HOME /usr/lib/plexmediaserver  
ENV PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS 6  
ENV PLEX_MEDIA_SERVER_MAX_STACK_SIZE 3000  
ENV PLEX_MEDIA_SERVER_TMPDIR /tmp  
ENV LD_LIBRARY_PATH ${PLEX_MEDIA_SERVER_HOME}  
ENV PLEX_MEDIA_SERVER_INFO_DEVICE docker  
  
# Create media directory  
RUN mkdir -p /vol/media  
  
# Set deb URL  
ARG PLEX_DEB_URL=https://downloads.plex.tv/plex-media-
server/${PLEX_VERSION}/plexmediaserver_${PLEX_VERSION}_amd64.deb  
  
# Upgrade packages and install dependencies  
RUN apt-get update && apt-get -y upgrade \  
&& apt-get -y install avahi-utils dbus wget \  
&& rm -rf /var/lib/apt/lists/*  
# Download and install the Plex Media Server deb  
RUN TEMP_FILE=$(mktemp) && wget ${PLEX_DEB_URL} -O ${TEMP_FILE} \  
&& dpkg -i ${TEMP_FILE} && rm ${TEMP_FILE}  
  
# Expose ports, see: https://goo.gl/bV6Krz  
EXPOSE 32400 1900/udp 3005 5353/udp 32410/udp 32412/udp 32413/udp 32414/udp
32469  
# Set running user  
USER plex  
  
# Set running user  
USER plex  
  
# Define docker volumes  
VOLUME /var/lib/plexmediaserver /vol/media  
# Set the working dir  
WORKDIR /var/lib/plexmediaserver  
# Default command  
CMD ["/usr/lib/plexmediaserver/Plex Media Server"]  

