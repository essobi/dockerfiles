# Builds the Widget Service Docker Image on Docker Hub  
FROM frolvlad/alpine-oraclejdk8:slim  
  
MAINTAINER Gary A. Stafford <garystafford@rochester.rr.com>  
ENV REFRESHED_AT 2016-09-13  
# install jar from github  
ENV GITHUB_REPO=https://github.com/garystafford/microservice-docker-demo-
widget/raw/build-artifacts \  
APP_FILE=widget-service-0.1.0.jar  
  
RUN set -ex \  
&& apk --no-cache add --virtual .build-dependencies curl \  
&& curl -fsSL ${GITHUB_REPO}/${APP_FILE} -o /app.jar \  
&& sh -c 'touch /app.jar' \  
&& touch /widget-service.log  
  
# install filebeat  
ENV FILEBEAT_SRC_SHA1=3fde7f5f5ea837140965a193bbb387c131c16d9c \  
FILEBEAT_VERSION=1.2.3 \  
FILEBEAT_URL=http://download.elastic.co/beats/filebeat  
  
RUN set -ex \  
&& curl -fsSL ${FILEBEAT_URL}/filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz -o
/tmp/filebeat.tar.gz \  
&& cd /tmp \  
&& echo "${FILEBEAT_SRC_SHA1} *filebeat.tar.gz" | sha1sum -c - \  
&& tar -xzf filebeat.tar.gz \  
&& cd filebeat-* \  
&& cp filebeat /bin \  
&& rm -rf /tmp/filebeat* \  
&& mkdir -p /etc/pki/tls/certs  
  
# configure filebeat  
COPY filebeat.yml /etc/filebeat/filebeat.yml  
COPY filebeat.template.json /etc/filebeat/filebeat.template.json  
COPY logstash-beats.crt /etc/pki/tls/certs/logstash-beats.crt  
  
# start filebeat  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
CMD [ "/usr/local/bin/start.sh" ]  

