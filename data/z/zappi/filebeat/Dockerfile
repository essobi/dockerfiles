FROM alpine:3.5  
MAINTAINER ZappiStore DevOps <devops@zappistore.com>  
  
ARG BUILD_DEPS="ca-certificates wget"  
ARG FILEBEAT_VERSION=5.1.2  
ARG FILEBEAT_PKG="filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz"  
ARG
FILEBEAT_SHA=2b63d1963e25064d7dfcba945cce9742527cf84847e11fc73d579326e7fdb464  
  
RUN apk update && \  
apk upgrade && \  
apk add ${BUILD_DEPS} && \  
wget --progress=dot:mega
https://artifacts.elastic.co/downloads/beats/filebeat/${FILEBEAT_PKG} && \  
echo "${FILEBEAT_SHA} *${FILEBEAT_PKG}" | sha256sum -c - && \  
tar xzf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \  
mv filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat /usr/local/bin && \  
mkdir -p /etc/filebeat && \  
cp filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat.full.yml
/etc/filebeat/filebeat.yml && \  
apk del ${BUILD_DEPS} && \  
rm -rf /var/cache/apk/* /filebeat-*  
  
ENTRYPOINT ["filebeat"]  
  
CMD ["-e", "-c", "/etc/filebeat/filebeat.yml"]  

