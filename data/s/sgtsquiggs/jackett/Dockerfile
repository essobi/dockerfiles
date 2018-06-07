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
tar &&\  
  
# install jackett  
mkdir -p \  
/app/jackett &&\  
latest_tag=$(curl -sX GET
"https://api.github.com/repos/Jackett/Jackett/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') &&\  
curl -o \  
/tmp/jackett.tar.gz -L \  
https://github.com/Jackett/Jackett/releases/download/$latest_tag/Jackett.Binaries.Mono.tar.gz
&&\  
tar xf /tmp/jackett.tar.gz \  
-C /app/jackett \  
\--strip-components=1 &&\  
  
# cleanup  
apk del build-dependencies &&\  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads  
EXPOSE 9117  

