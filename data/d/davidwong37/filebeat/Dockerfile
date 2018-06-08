# Filebeat running on Alpine  
# - Need glibc to work  
# - Need to copy filebeat.yml to installation dir  
#FROM alpine  
FROM frolvlad/alpine-glibc  
  
ENV FILEBEAT_VERSION=1.2.2 \  
FILEBEAT_SHA1=048ca4399b2936d5234a4c313610f6d93d8a0966  
  
# setup location for installation  
ENV INSTALL_LOCATION /opt  
WORKDIR ${INSTALL_LOCATION}  
  
RUN set -x && \  
apk --no-cache add --virtual .build-dependencies curl && \  
curl -L -O
https://download.elastic.co/beats/filebeat/filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz
&& \  
echo "${FILEBEAT_SHA1} filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz" | sha1sum
-c - && \  
tar xzvf filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz && \  
cp filebeat-${FILEBEAT_VERSION}-x86_64/filebeat /bin && \  
rm -rf filebeat* && \  
apk del .build-dependencies  
  
# For testing  
# -----------  
#COPY filebeat.yml /opt/  
#CMD [ "filebeat", "-e", "-configtest" ]  
CMD [ "filebeat", "-e" ]  

