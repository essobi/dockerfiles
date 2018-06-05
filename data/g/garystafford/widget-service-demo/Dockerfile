FROM frolvlad/alpine-oraclejdk8:slim  
  
MAINTAINER Gary A. Stafford  
ENV REFRESHED_AT 2016-09-30  
ARG BUILD_DATE=""  
ARG VCS_REF=""  
ARG VERSION=""  
LABEL \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Widget Service Demo" \  
org.label-schema.description="Widget Service build using Docker Hub automated
build" \  
org.label-schema.license=Apache-2.0 \  
org.label-schema.url="https://github.com/garystafford/widget-service-demo" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/garystafford/widget-service-demo"
\  
org.label-schema.vendor="Gary A. Stafford" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
# install jar from github  
ENV GITHUB_REPO=https://github.com/garystafford/widget-service-demo.git  
  
RUN set -ex \  
&& apk --no-cache add --virtual .build-dependencies curl git \  
&& mkdir /git_tmp \  
&& git clone \--branch build-artifacts --single-branch --depth 1
${GITHUB_REPO} git_tmp \  
&& mv git_tmp/*.jar app.jar \  
&& rm -rf git_tmp \  
&& touch app.jar \  
&& touch widget-service.log  
  
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

