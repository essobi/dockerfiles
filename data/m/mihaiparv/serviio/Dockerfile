FROM jrottenberg/ffmpeg  
MAINTAINER mihai.parv  
  
RUN yum install -y java-1.8.0-openjdk tar && \  
yum clean all && \  
rm -rf /var/lib/yum/yumdb/*  
  
ENV SERVIIO_VERSION 1.5.2  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os
http://download.serviio.org/releases/serviio-${SERVIIO_VERSION}-linux.tar.gz
&& \  
tar zxvf serviio-${SERVIIO_VERSION}-linux.tar.gz && \  
mv serviio-${SERVIIO_VERSION} /opt/serviio && \  
rm -rf ${DIR}  
  
VOLUME /opt/serviio/log  
VOLUME /opt/serviio/library  
VOLUME /mnt/storage  
  
# serviio requires TCP port 8895 and UDP 1900 for content and 23423 for rest
api  
EXPOSE 23423:23423/tcp 8895:8895/tcp 1900:1900/udp  
  
WORKDIR /opt/serviio  
ENTRYPOINT ["bin/serviio.sh"]

