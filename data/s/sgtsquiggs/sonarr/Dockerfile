FROM sgtsquiggs/alpine.mono:3.4  
MAINTAINER sgtsquiggs  
  
# environment settings  
ENV XDG_DATA_HOME="/config"  
ENV XDG_CONFIG_HOME="/config"  
RUN \  
# install packages  
apk add \--no-cache \  
\--virtual=build-dependencies \  
curl \  
tar \  
xz &&\  
  
# install sonarr  
mkdir -p \  
/app/sonarr &&\  
curl -o \  
/tmp/sonarr-src.tar.gz -L \  
http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz &&\  
tar xzf /tmp/sonarr-src.tar.gz \  
-C /app/sonarr \  
\--strip-components=1 &&\  
  
# cleanup  
apk del build-dependencies &&\  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads /tv  
EXPOSE 8989  

