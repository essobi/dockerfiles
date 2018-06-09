FROM debian:wheezy  
  
MAINTAINER michael@schuerig.de  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Create a new user account with UID/GID at least 10000.  
# This makes it easier to keep host and docker accounts apart.  
RUN useradd --home /var/xmedia -u 2000 -M xmedia && \  
mkdir -p /var/xmedia && chown xmedia /var/xmedia && chmod 0770 /var/xmedia  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
apt-get update && \  
apt-get dist-upgrade --yes --no-install-recommends --no-install-suggests && \  
apt-get install --yes --no-install-recommends --no-install-suggests
openjdk-7-jre-headless locales && \  
apt-get clean  
  
ENV SUBSONIC_VERSION 6.0  
ADD http://subsonic.org/download/subsonic-$SUBSONIC_VERSION.deb
/tmp/subsonic-$SUBSONIC_VERSION.deb  
RUN dpkg -i /tmp/subsonic-$SUBSONIC_VERSION.deb && rm -f /tmp/*.deb  
  
# Create hardlinks to the transcoding binaries.  
# This way we can mount a volume over /var/subsonic.  
# Apparently, Subsonic does not accept paths in the Transcoding settings.  
# If you mount a volume over /var/subsonic, create symlinks  
# <host-dir>/var/subsonic/transcode/ffmpeg -> /usr/local/bin/ffmpeg  
# <host-dir>/var/subsonic/transcode/lame -> /usr/local/bin/lame  
#RUN ln /var/subsonic/transcode/ffmpeg /var/subsonic/transcode/lame
/usr/local/bin  
VOLUME /config  
  
COPY startup.sh /startup.sh  
  
EXPOSE 4040 4443  
RUN locale-gen en_US.UTF-8  
  
USER xmedia  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
CMD []  
ENTRYPOINT ["/startup.sh"]  

