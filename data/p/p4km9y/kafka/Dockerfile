FROM java:8-alpine  
MAINTAINER p4km9y  
  
ARG KAFKA_HEAP_OPTS  
ENV KAFKA_HEAP_OPTS ${KAFKA_HEAP_OPTS:-"-Xmx378m -Xms192m"}  
  
ENV KAFKA_VERSION 1.0.0  
ENV KAFKA_BROKER_ID -1  
ENV LOG_RETENTION_HOURS 240  
# ENV ZOOKEEPER_CONNECT ""  
RUN apk add --update curl tini bash && \  
rm -rf /var/cache/apk/*  
  
RUN current=http://www.apache.org/dist/kafka/${KAFKA_VERSION} && \  
ref=$(wget -qO - ${current} | grep -v src\\\\. | grep -v doc | sed -n
's/.*href="\\(kafka.*\\.tgz\\)".*/\1/p' | tail -1) && \  
mkdir /opt && \  
wget -O - ${current}/${ref} | gzip -dc | tar x -C /opt/ -f - && \  
dir=`ls /opt | grep kafka` && \  
ln -s /opt/${dir} /opt/kafka && \  
mkdir /opt/kafka/data  
  
RUN addgroup -S kafka && \  
adduser -S -H -h /opt/kafka -g kafka kafka && \  
chown -R kafka:kafka /opt/kafka/  
  
USER kafka  
  
VOLUME ["/opt/kafka/data"]  
  
EXPOSE 9092  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties \  
\--override log.dirs=/opt/kafka/data \  
\--override delete.topic.enable=true \  
\--override log.retention.hours=$LOG_RETENTION_HOURS \  
\--override advertised.host.name=`ip -4 addr show scope global dev eth0 | grep
inet | awk '{print \$2}' | cut -d / -f 1 | head -1` \  
\--override zookeeper.connect=$ZOOKEEPER_CONNECT \  
\--override broker.id=$KAFKA_BROKER_ID  

