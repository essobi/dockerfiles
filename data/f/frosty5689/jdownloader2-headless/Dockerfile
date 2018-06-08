FROM frolvlad/alpine-oraclejre8:latest  
  
MAINTAINER frosty5689 <frosty5689@gmail.com>  
  
RUN apk add --no-cache --update \  
ca-certificates \  
tzdata \  
libstdc++ \  
ttf-dejavu \  
&& update-ca-certificates  
  
# Create directory, downloader JD" and start JD2 for the initial update and
creation of config files.  
RUN \  
apk add --no-cache --update --virtual build-dependencies wget && \  
mkdir -p /opt/JDownloader/ && \  
wget -O /opt/JDownloader/JDownloader.jar --user-
agent="https://hub.docker.com/r/frosty5689/jdownloader2-headless/"
\--progress=bar:force http://installer.jdownloader.org/JDownloader.jar && \  
java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar && \  
apk del build-dependencies  
  
ADD run/* /opt/JDownloader/  
  
VOLUME ["/opt/JDownloader/cfg", "/root/Downloads"]  
  
# Run this when the container is started  
CMD ["/opt/JDownloader/start.sh"]  
  

