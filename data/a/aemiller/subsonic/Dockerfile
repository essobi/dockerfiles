# Dockerfile for the Subsonic media server  
# Author: Adam Miller <luphytwo@gmail.com>  
# Based off of mschuerig/subsonic-docker-image  
# Run after build with:  
# docker run -d -p <port>:4040 -v "/path/to/music:/var/music:ro"
luphy/subsonic  
FROM ubuntu:16.04  
MAINTAINER adam@adammiller.io  
  
# Noninteractive debconfig  
ENV DEBIAN_FRONTEND noninteractive  
  
# Specify the version of Subsonic to be downloaded  
ENV SUBSONIC_VERSION 6.1.3  
# Create a new user account with UID/GID at least 10000.  
# This makes it easier to keep host and docker accounts apart.  
RUN useradd --home /var/subsonic -M subsonic -K UID_MIN=10000 -K GID_MIN=10000
&& \  
mkdir -p /var/subsonic && chown subsonic /var/subsonic && chmod 0770
/var/subsonic  
  
# Set the correct locale and install java and locales  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
apt-get update && apt-get install -y \  
openjdk-8-jre-headless \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set locale encoding related vars for Subsonic to properly treat special
chars  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Download the specified version from sourceforge  
ADD
http://downloads.sourceforge.net/project/subsonic/subsonic/$SUBSONIC_VERSION/subsonic-$SUBSONIC_VERSION.deb
/tmp/subsonic-$SUBSONIC_VERSION.deb  
  
# Install subsonic  
RUN dpkg -i /tmp/subsonic-$SUBSONIC_VERSION.deb && rm -f /tmp/*.deb  
  
# Create hardlinks to the transcoding binaries.  
# This way we can mount a volume over /var/subsonic.  
# Apparently, Subsonic does not accept paths in the Transcoding settings.  
# If you mount a volume over /var/subsonic, create symlinks  
# <host-dir>/var/subsonic/transcode/ffmpeg -> /usr/local/bin/ffmpeg  
# <host-dir>/var/subsonic/transcode/lame -> /usr/local/bin/lame  
RUN ln /var/subsonic/transcode/ffmpeg /var/subsonic/transcode/lame
/usr/local/bin  
  
# Create a volume for the subsonic configuration files  
VOLUME /var/subsonic  
  
# Import the start script  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Expose the port subsonic listens on  
EXPOSE 4040  
# Specify the subsonic user  
USER subsonic  
  
# Add the start script as an entrypoint  
CMD []  
ENTRYPOINT ["/start.sh"]  

