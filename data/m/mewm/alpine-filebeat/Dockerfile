FROM zot24/glibc  
MAINTAINER Dennis Micky Jensen <root@mewm.org>  
  
ENV FILEBEAT_SRC_SHA1=3fde7f5f5ea837140965a193bbb387c131c16d9c \  
FILEBEAT_VERSION=1.2.3  
RUN set -ex \  
&& apk --no-cache add --virtual .build-dependencies \  
curl \  
\  
&& curl -fsSL
http://download.elastic.co/beats/filebeat/filebeat-${FILEBEAT_VERSION}-x86_64.tar.gz
-o /tmp/filebeat.tar.gz \  
\  
&& cd /tmp \  
&& echo "${FILEBEAT_SRC_SHA1} *filebeat.tar.gz" | sha1sum -c - \  
&& tar -xzf filebeat.tar.gz \  
\  
&& cd filebeat-* \  
&& cp filebeat /bin \  
\  
&& rm -rf /tmp/filebeat* \  
&& apk del .build-dependencies  
  
CMD [ "filebeat", "-e" ]  

