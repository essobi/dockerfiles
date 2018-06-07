FROM openjdk:8-jre-alpine  
  
# https://artifacts.elastic.co/GPG-KEY-logstash  
ARG LOGSTASH_VERSION="5.6.3"  
ARG LOGSTASH_DIR="/usr/share/logstash"  
ENV TZ="UTC"  
ADD
https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz
${LOGSTASH_DIR}/logstash.tar.gz  
COPY logstash.conf /usr/share/logstash/config/logstash.conf  
  
WORKDIR ${LOGSTASH_DIR}  
RUN apk add --no-cache --virtual build-dependencies \  
tar &&\  
apk add --no-cache --virtual runtime-dependencies \  
bash &&\  
addgroup -g 1000 logstash &&\  
adduser -u 1000 -G logstash -s /bin/sh -D logstash &&\  
tar -xzvf logstash.tar.gz --strip 1 &&\  
rm logstash.tar.gz &&\  
mkdir -p ./plugins ./data ./logs ./config/scripts &&\  
chown -R logstash:logstash . &&\  
apk del --purge build-dependencies &&\  
rm -rf /tmp/* &&\  
rm -rf /var/cache/apk/*  
  
USER logstash  
  
EXPOSE 12201  
EXPOSE 9600  
CMD /usr/share/logstash/bin/logstash -f
/usr/share/logstash/config/logstash.conf  

