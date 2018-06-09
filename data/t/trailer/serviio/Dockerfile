FROM jrottenberg/ffmpeg  
MAINTAINER headbanger84  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk-headless curl tar  
# apt-get autoremove && \  
# apt-get clean  
ENV SERVIIO_VERSION 1.8  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os
http://download.serviio.org/releases/serviio-${SERVIIO_VERSION}-linux.tar.gz
&& \  
tar zxvf serviio-${SERVIIO_VERSION}-linux.tar.gz && \  
mv serviio-${SERVIIO_VERSION} /opt/serviio && \  
rm -rf ${DIR}  
  
#VOLUME /opt/serviio/log  
#VOLUME /opt/serviio/library  
# serviio requires TCP port 8895 and UDP 1900 for content and  
# 23423 (console) and 23424 (API & mediabrowser) api  
EXPOSE 23424:23424/tcp 23423:23423/tcp 8895:8895/tcp 1900:1900/udp  
  
WORKDIR /opt/serviio  
ENTRYPOINT ["bin/serviio.sh"]  
VOLUME /config /transcode /log /media  

