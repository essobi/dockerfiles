FROM openjdk:8-jre-alpine  
  
# TODO: https://artifacts.elastic.co/GPG-KEY-elasticsearch  
ARG ELASTICSEARCH_VERSION="5.6.3"  
ARG ELASTICSEARCH_DIR="/usr/share/elasticsearch"  
ADD
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz
${ELASTICSEARCH_DIR}/elasticsearch.tar.gz  
  
WORKDIR ${ELASTICSEARCH_DIR}  
RUN apk add --no-cache --virtual build-dependencies \  
tar &&\  
apk add --no-cache --virtual runtime-dependencies \  
bash &&\  
addgroup -g 1000 elasticsearch &&\  
adduser -u 1000 -G elasticsearch -s /bin/bash -D elasticsearch &&\  
tar -xzvf elasticsearch.tar.gz --strip 1 &&\  
rm elasticsearch.tar.gz &&\  
mkdir -p ./plugins ./data ./logs ./config/scripts &&\  
chown -R elasticsearch:elasticsearch . &&\  
apk del --purge build-dependencies &&\  
rm -rf /tmp/* &&\  
rm -rf /var/cache/apk/*  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200  
EXPOSE 9300  
USER elasticsearch  
COPY elasticsearch.yml ${ELASTICSEARCH_DIR}/config/elasticsearch.yml  
CMD /usr/share/elasticsearch/bin/elasticsearch  

