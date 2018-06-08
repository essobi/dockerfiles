FROM lsiobase/mono  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL maintainer="jdfalk"  
  
# set environment variables  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_CONFIG_HOME="/config/xdg"  
LABEL Name="Sonarr"  
  
# add mediainfo repo  
ADD . /tmp  
  
# add sonarr repository  
RUN \  
curl https://mediaarea.net/repo/deb/repo-mediaarea_1.0-5_all.deb -o /tmp/repo-
mediaarea.deb && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \  
echo "deb http://apt.sonarr.tv/ master main" > \  
/etc/apt/sources.list.d/sonarr.list && \  
echo "**** install packages ****" && \  
apt-get update && \  
apt-get install -y apt-transport-https && \  
dpkg -i /tmp/repo-mediaarea.deb && \  
apt-get update && \  
apt-get install -y \  
nzbdrone mediainfo && \  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8080  
VOLUME /config  
  
HEALTHCHECK \--interval=200s --timeout=100s CMD curl --fail
http://localhost:8080 || exit 1  

