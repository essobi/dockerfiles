FROM insideo/jre8:8u152  
MAINTAINER ccondit@randomcoder.com  
  
RUN \  
opkg update && \  
opkg install kafka runas && \  
opkg clean && \  
addgroup -S -g 103 kafka && \  
mkdir -p /var/lib/kafka && \  
adduser -h /var/lib/kafka -g "Kafka user" -s /bin/sh -G kafka -S -D -u 103
kafka && \  
chown -R kafka:kafka /var/lib/kafka && \  
echo "" >> /etc/kafka/server.properties && \  
echo "delete.topic.enable=true" >> /etc/kafka/server.properties  
  
COPY docker-entrypoint.sh /  
  
ENV KAFKA_DATA_DIR=/data  
ENV KAFKA_LOG_DIR=/logs  
ENV KAFKA_HEAP_OPTS=-Xmx256m  
ENV KAFKA_ADVERTISED_HOST=  
ENV KAFKA_ADVERTISED_PORT=9092  
ENV KAFKA_PORT=9092  
ENV KAFKA_ZK_CHROOT=  
  
VOLUME /data  
VOLUME /logs  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9092  
  
CMD [ "/usr/share/kafka/bin/kafka-server-start.sh",
"/etc/kafka/server.properties" ]  

