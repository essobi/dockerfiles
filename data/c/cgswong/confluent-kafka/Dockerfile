# Builds a docker image running Confluent's distribution of Apache Kafka.  
FROM cgswong/confluent-platform:2.0.1  
ENV CONFLUENT_USER confluent  
ENV CONFLUENT_GROUP confluent  
ENV kafka_log_dir "/var/lib/kafka"  
ENV KAFKA_CFGDIR /etc/kafka  
ENV JMX_PORT 19092  
COPY kafka-docker.sh /usr/local/bin/  
COPY log4j.properties /etc/kafka/  
  
RUN groupadd -r ${CONFLUENT_GROUP} &&\  
useradd -r -g ${CONFLUENT_GROUP} ${CONFLUENT_USER} &&\  
mkdir -p ${kafka_log_dir} ${KAFKA_CFGDIR} &&\  
chown -R ${CONFLUENT_USER}:${CONFLUENT_GROUP} ${kafka_log_dir} ${KAFKA_CFGDIR}
/var/log/kafka /usr/local/bin/kafka-docker.sh &&\  
chmod +x /usr/local/bin/kafka-docker.sh  
  
USER ${CONFLUENT_USER}  
VOLUME ["${kafka_log_dir}", "${KAFKA_CFGDIR}"]  
# Expose client port (9092/tcp), JMX  
EXPOSE 9092 ${JMX_PORT}  
  
ENTRYPOINT ["/usr/local/bin/kafka-docker.sh"]  

